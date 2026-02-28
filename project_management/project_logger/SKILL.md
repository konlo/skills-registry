---
name: project_logger
description: Automatically record all user requests and project progress into a single log file.
---

# project_logger.skill

## Purpose
Ensure every user interaction, request, and project advancement is meticulously documented in a single `project_progress.md` file. This provides a clear audit trail and helps maintain context across sessions.

## 1. Skill Scope
This skill provides instructions for:
1. Initializing the `project_progress.md` file.
2. Logging every user request with a timestamp.
3. Documenting the agent's actions, decisions, and outcomes.
4. Keeping a persistent record of the project's journey.

## 2. Usage Instructions

When this skill is active, the agent MUST follow these steps for **EVERY** request:

1. **Check for Log File**: Look for `project_progress.md` in the project root. If it doesn't exist, create it using the template provided below.
2. **Log the Request**: Before performing any major task, append the user's request to the log file.
   - Use the format: `## [YYYY-MM-DD HH:MM:SS] User Request: <Request Content>`
3. **Log the Process & Artifacts**: During and after the task, document the steps taken and any artifact updates.
   - Use the format: `- **Action**: <Description of what was done>`
   - Use the format: `- **Artifact Update**: <Summary of changes in implementation_plan.md, task.md, etc.>`
   - Use the format: `- **Outcome**: <Result of the action>`
4. **Update Status**: If the overall project status changes, update the "Current Status" section at the top of the file.
5. **Handle Summary Requests**: If asked to "summarize today's work" or similar:
   - Read the `project_progress.md` file.
   - Extract all entries for the requested date (defaulting to the current date).
   - Provide a structured, bulleted summary of the User Requests, Actions, and Outcomes.

## 3. Log File Template (`project_progress.md`)

```markdown
# Project Progress Log

## Current Status
- **Last Updated**: [YYYY-MM-DD]
- **Status**: [In Progress / On Hold / Completed]
- **Summary**: [Brief summary of the current state]

---

## Log Entries

### [2026-02-27 20:30:00] User Request: Create a Project Logger Skill
- **Action**: Created `project_management/project_logger/SKILL.md`.
- **Outcome**: Skill established to automate project logging.
```

## 4. Best Practices
- **Be Concise**: Write clear and actionable logs.
- **Stay Consistent**: Always use the same format for timestamps and headers.
- **Record Decisions**: If a significant design choice is made, document the rationale.
- **Link Resources**: Link to relevant artifacts or important code files in the log.
