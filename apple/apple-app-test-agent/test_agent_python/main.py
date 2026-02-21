import json
import logging
import os
import subprocess
import time
import traceback
import urllib.request
import urllib.error
from datetime import datetime

# Configure Artifact Directories
artifacts_dir = "artifacts"
log_dir = os.path.join(artifacts_dir, "logs")
crash_dir = os.path.join(artifacts_dir, "crash_dumps")
snapshot_dir = os.path.join(artifacts_dir, "state_snapshots")

for d in [artifacts_dir, log_dir, crash_dir, snapshot_dir]:
    os.makedirs(d, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"test_agent_{timestamp}.log")
crash_file = os.path.join(crash_dir, f"crash_report_{timestamp}.json")
repro_file = os.path.join(artifacts_dir, f"repro_steps_{timestamp}.json")

logger = logging.getLogger("TestAgent")
logger.setLevel(logging.DEBUG)

# File handler
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

class TestAgent:
    def __init__(self, 
                 app_executable_path: str = None, 
                 connection_mode: str = "cli",
                 base_url: str = "http://localhost:8080",
                 action_timeout_sec: float = 5.0,
                 max_steps_per_scenario: int = 100,
                 rng_seed: int = None):
        """
        Initializes the Test Agent.
        :param app_executable_path: Path to the Apple App executable (e.g. built CLI tool)
        :param connection_mode: "cli", "http", or "socket" (default uses subprocess CLI)
        :param base_url: The URL of the Simulator Bridge (if in http mode)
        :param action_timeout_sec: Maximum time to wait for the app to respond to an action.
        :param max_steps_per_scenario: Safety guard against infinite testing loops.
        :param rng_seed: Fixed seed for deterministic testing across runs.
        """
        self.app_executable_path = app_executable_path
        self.connection_mode = connection_mode
        self.base_url = base_url
        self.action_timeout_sec = action_timeout_sec
        self.max_steps_per_scenario = max_steps_per_scenario
        self.rng_seed = rng_seed
        self.process = None
        self.action_log = []
        logger.info(f"TestAgent initialized with mode: {connection_mode}")

    def start_app(self):
        """Starts the Apple App process."""
        self.action_log = [] # Reset log per scenario/run
        
        if self.connection_mode == "cli":
            if not self.app_executable_path:
                raise ValueError("app_executable_path is required for CLI connection mode.")
            logger.info(f"Starting app at {self.app_executable_path}")
            self.process = subprocess.Popen(
                [self.app_executable_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            time.sleep(1) # wait for startup
        else:
            logger.info(f"Connecting to app via {self.connection_mode}")
            # Implement HTTP or Socket connection here
            pass

    def stop_app(self):
        """Stops the Apple App."""
        logger.info("Stopping the app...")
        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None

    def _save_repro_steps(self):
        """Saves current action sequence for deterministic replay."""
        if self.action_log:
            with open(repro_file, 'w') as f:
                json.dump({"seed": self.rng_seed, "sequence": self.action_log}, f, indent=2)

    def _send_command(self, command: dict) -> dict:
        """Sends a JSON command to the app and returns the JSON response."""
        logger.debug(f"Sending command: {command}")
        
        # Keep track for replay / debugging
        if command.get("action") != "get_state":
            self.action_log.append(command)
        
        if self.connection_mode == "cli":
            if not self.process:
                raise RuntimeError("App is not running.")
            
            req_str = json.dumps(command) + "\n"
            self.process.stdin.write(req_str)
            self.process.stdin.flush()
            
            # Read response (Using naive readline here. In production, wrap in thread/poll with select for timeout)
            # A true timeout implementation would use select.select on self.process.stdout
            response_str = self.process.stdout.readline()
            if not response_str:
                stderr_output = self.process.stderr.read()
                raise RuntimeError(f"App closed unexpectedly. Stderr: {stderr_output}")
            
            try:
                resp = json.loads(response_str)
                logger.debug(f"Received response: {resp}")
                return resp
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Failed to parse JSON response: {response_str}") from e
        elif self.connection_mode == "http":
            req_data = json.dumps(command).encode('utf-8')
            req = urllib.request.Request(self.base_url, data=req_data, method='POST')
            req.add_header('Content-Type', 'application/json')
            
            try:
                with urllib.request.urlopen(req, timeout=self.action_timeout_sec) as response:
                    resp_str = response.read().decode('utf-8')
                    resp = json.loads(resp_str)
                    logger.debug(f"Received HTTP response: {resp}")
                    return resp
            except urllib.error.URLError as e:
                raise RuntimeError(f"HTTP Connection failed to {self.base_url}: {e.reason}") from e
            except Exception as e:
                raise RuntimeError(f"HTTP Request failed: {e}") from e
        else:
            # Implement Socket connection here
            pass
        return {}

    def get_all_information(self) -> dict:
        """
        6. Reads all state and information from the App.
        Returns the full current state for inspection.
        """
        logger.info("Requesting all information from app.")
        return self._send_command({"action": "get_state"})

    def set_condition(self, condition_data: dict) -> dict:
        """
        7. Provides an interface to set specific mock scenarios or conditions.
        :param condition_data: Data defining the state to set (e.g. {"player_score": 100})
        """
        logger.info(f"Setting specific condition: {condition_data}")
        return self._send_command({
            "action": "set_condition",
            "data": condition_data
        })
        
    def save_snapshot(self, tag: str, state_data: dict = None):
        """Saves a state snapshot to artifacts."""
        if not state_data:
            state_data = self.get_all_information()
        
        filename = os.path.join(snapshot_dir, f"snapshot_{tag}_{int(time.time()*1000)}.json")
        with open(filename, 'w') as f:
            json.dump(state_data, f, indent=2)
        logger.info(f"Snapshot saved: {filename}")

    def send_user_action(self, action_type: str, action_data: dict = None) -> dict:
        """Sends a simulated user interface interaction."""
        cmd = {"action": action_type}
        if action_data:
            cmd["data"] = action_data
        logger.info(f"Sending user action: {action_type} with data: {action_data}")
        return self._send_command(cmd)

    def run_tests(self, scenarios: list, repeat_count: int = 1):
        """
        5. Runs a suite of scenarios, potentially repeating them.
        """
        logger.info(f"Starting test run. Total scenarios: {len(scenarios)}, Repeat count: {repeat_count}")
        
        for iteration in range(repeat_count):
            logger.info(f"--- Starting Iteration {iteration + 1}/{repeat_count} ---")
            for idx, scenario_func in enumerate(scenarios):
                scenario_name = scenario_func.__name__
                logger.info(f"Running Scenario {idx + 1}: {scenario_name}")
                
                try:
                    self.start_app()
                    
                    # If deterministic replay is requested
                    if self.rng_seed is not None:
                        self.set_condition({"rng_seed": self.rng_seed})
                        
                    # Run the actual test scenario logic
                    scenario_func(self)
                    
                    # Save normal execution path
                    self._save_repro_steps()
                    logger.info(f"Scenario {scenario_name} completed successfully.")
                except Exception as e:
                    logger.error(f"Scenario {scenario_name} failed with exception: {e}")
                    self.handle_crash(e, scenario_name)
                finally:
                    self.stop_app()
                    
            logger.info(f"--- Finished Iteration {iteration + 1}/{repeat_count} ---")

    def handle_crash(self, exception: Exception, context: str):
        """
        4. Capture anomalies, exceptions, and crashes, saving them for debugging.
        """
        logger.critical(f"Handling crash/exception in {context}")
        
        crash_data = {
            "timestamp": datetime.now().isoformat(),
            "context": context,
            "error_type": type(exception).__name__,
            "error_message": str(exception),
            "traceback": traceback.format_exc()
        }
        
        # Try to capture last known state if possible
        try:
           crash_data["last_known_state"] = self.get_all_information()
        except Exception as state_exc:
           crash_data["last_known_state"] = f"Failed to retrieve state: {state_exc}"
           
        with open(crash_file, 'a') as f:
            f.write(json.dumps(crash_data, indent=2) + "\n")
            
        self._save_repro_steps()
            
        logger.critical(f"Crash report saved to: {crash_file}")
