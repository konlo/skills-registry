---
name: agent_orchestration
description: Manage multi-agent delegation, generate sync boards, and create agent-specific start prompts.
---

# agent_orchestration.skill

## Purpose
This skill coordinates multiple specialized agents (e.g., UI, Backend, Logic) to work in parallel. It provides a structured way to hand off tasks and maintain a shared state.

## 1. Core Artifacts

### 1.1 Agent Sync Board (`agent_sync_board.md`)
The Single Source of Truth for inter-agent coordination.

```markdown
# 📋 Agent Sync Board

## 📍 Current Phase
- [e.g., Phase 0: Contract Lock / Phase 1: Implementation]

## 🤝 Module Assignment
- **Agent 1 (UI/UX)**: [Task Summary]
- **Agent 2 (Backend/Protocol)**: [Task Summary]
- **Agent 3 (Game Logic)**: [Task Summary]

## 🚧 Shared Contracts
- [Link to protocol/contract files]

## ❓ Contract Questions (Pending)
- [Agent A -> Agent B]: [Question]

## 📦 Handoff Log
- [Agent ID]: [Handoff Description for others]
```

### 1.2 Agent Start Prompt (`.prompt.md`)
Each agent must receive a specific start prompt created by this skill.

## 2. Agent Prompt Template

When generating a prompt for a sub-agent, use this exact structure:

```markdown
# 🤖 Agent Allocation: [Agent Name/ID]

## 🎭 Role Definition
너는 [Agent ID]이다. [[Path/to/base_skill.md]]의 역할을 따른다.

## 📅 Context & Phase
이번 작업은 [Phase Name]이다.
1차 목표는 [Specific Goal]이다.

## 🔍 Scope (수정 범위)
- [File Path 1]
- [File Path 2]

## ✅ Todo (이번 턴에 할 일)
- [Action Item 1]
- [Action Item 2]
- `agent_sync_board.md`의 [Agent ID] 섹션과 Contract Questions를 업데이트해라.

## 🚫 Constraints (하지 말 것)
- [Forbidden Action 1]
- [Forbidden Action 2]

## 📤 Output Format (보고 형식)
끝나면 아래 형식으로 보고해라:
- **변경 파일**: 목록
- **주요 결정 사항**: 이번에 고정한 내용
- **타 에이전트 요청**: [Agent X]에게 필요한 계약 질문/요청
- **Handoff**: 다른 에이전트가 바로 쓸 수 있는 요약
```

## 3. Execution Procedure

1. **Module Breakdown**: Divide the project into independent modules (e.g., UI, Logic, Data).
2. **Board Initialization**: Create or update `agent_sync_board.md` in the project root.
3. **Prompt Generation**: Create a `.prompt.md` file for each assigned agent using the template above.
4. **Handoff Monitoring**: After an agent reports back, update the Sync Board and generate the next prompt if needed.

## 4. Success Criteria
- Each agent has a clear, non-overlapping scope.
- `agent_sync_board.md` reflects the real-time status of all agents.
- Cross-agent dependencies are explicitly documented as "Contract Questions".
