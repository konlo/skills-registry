import logging
from main import TestAgent

logger = logging.getLogger("TestAgent.Scenarios")

def scenario_basic_launch_and_read(agent: TestAgent):
    """
    Scenario: Simply launch the app and read all its state information.
    Verifies that the read interface (get_all_information) works correctly.
    """
    logger.info("Running basic launch and read...")
    
    # 6. Read all information
    state = agent.get_all_information()
    
    # Assert something about the state (example)
    assert state is not None, "Failed to retrieve state!"
    assert "status" in state, "State missing 'status' field."
    
    logger.info(f"State successfully validated: {state}")

def scenario_setup_condition_and_act(agent: TestAgent):
    """
    Scenario: Set a specific mock condition in the App, then perform an action.
    Verifies that the interface to set conditions (set_condition) works correctly.
    """
    logger.info("Running condition setup and act scenario...")
    
    # 7. Request specific conditions and mock the situation
    setup_result = agent.set_condition({
        "mock_scenario": "game_over",
        "player1_score": 100,
        "player2_score": 50
    })
    logger.info(f"Condition set result: {setup_result}")
    
    # Send a user action to interact with the mocked state
    agent.save_snapshot("pre_action")
    action_result = agent.send_user_action("click_restart_button")
    agent.save_snapshot("post_action")
    
    logger.info(f"Action result: {action_result}")
    
    # Read state again to verify changes
    new_state = agent.get_all_information()
    assert new_state.get("game_status") == "restarted", f"App did not correctly restart. State: {new_state}"

def scenario_force_crash_capture(agent: TestAgent):
    """
    Scenario: Sends an invalid action to purposefully test crash and exception capturing.
    """
    logger.info("Running force crash scenario...")
    
    # Sending an action that should cause an error/crash in the app
    # The TestAgent's try/except will catch this and log it according to requirement #4
    response = agent.send_user_action("invalid_action_triggering_crash")
    
    if "error" in response:
        raise RuntimeError(f"App returned an error state: {response['error']}")
    
def scenario_safety_limit_trigger(agent: TestAgent):
    """
    Scenario: Attempts to run an infinite loop to verify safety limits.
    """
    logger.info("Running safety limit trigger scenario...")
    
    # Loop over the allowed max steps to see if our agent bails out gracefully
    # In a real app, an agent might get stuck in a visual loop.
    for step in range(agent.max_steps_per_scenario + 5):
        if step >= agent.max_steps_per_scenario:
            logger.warning("Safety limit reached. Triggering graceful abort.")
            agent.save_snapshot("safety_abort")
            raise RuntimeError(f"Infinite loop detected. Reached max steps ({agent.max_steps_per_scenario})")
            
        agent.send_user_action("click_useless_button")

def scenario_simulator_sync_test(agent: TestAgent):
    """
    Scenario: Connects to a real-time Simulator Bridge and verifies sync.
    This scenario is intended for use with connection_mode='http'.
    """
    logger.info("Running simulator sync test...")
    
    # 1. Fetch initial state from the simulator UI
    initial_state = agent.get_all_information()
    logger.info(f"Initial Simulator UI State: {initial_state}")
    
    # 2. Perform an action that should change the UI visually
    agent.send_user_action("play_random_card")
    
    # 3. Fetch state again to confirm UI/Engine synchronization
    new_state = agent.get_all_information()
    logger.info(f"Updated Simulator UI State: {new_state}")
    
    assert new_state != initial_state, "Simulator UI did not update after action!"

if __name__ == "__main__":
    # Example Usage:
    # 1. Provide the path to your Apple App's compiled test CLI or interface
    app_executable = "./example_app_cli" 
    
    agent = TestAgent(app_executable_path=app_executable, 
                      connection_mode="cli",
                      max_steps_per_scenario=100, 
                      rng_seed=42) # Deterministic seed
    
    scenarios_to_run = [
        scenario_basic_launch_and_read,
        scenario_setup_condition_and_act,
        scenario_force_crash_capture,
        scenario_safety_limit_trigger
    ]
    
    # 5. Repeat tests continuously or a set number of times
    REPEAT_COUNT = 3 # Set to a large number for prolonged stress testing
    
    # Example for Simulator Mode:
    # agent_sim = TestAgent(connection_mode="http", base_url="http://localhost:8080/api")
    # agent_sim.run_tests(scenarios=[scenario_simulator_sync_test], repeat_count=10)
    
    try:
        agent.run_tests(scenarios=scenarios_to_run, repeat_count=REPEAT_COUNT)
    except KeyboardInterrupt:
        logger.info("Testing interrupted by user.")
