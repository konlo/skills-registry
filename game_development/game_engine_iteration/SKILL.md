---
skill: game_engine_iteration
version: 1.0
type: engine_iteration
domain: game_development
blocking: true
runs_after:
  - game_engine_design
runs_before:
  - engine_implementation
  - ai_decision_design
requires_reference:
  - engine_design_document.md
guarantees:
  - engine_design_integrity
  - controlled_engine_evolution
  - full_iteration_traceability
---

# ⚙️ game_engine_iteration — SKILL

Purpose

This skill governs all post-design modifications to the game engine.

It exists to ensure that:

The original engine design remains authoritative

Any deviation is explicitly reviewed

Engine behavior evolves intentionally, not accidentally

Every change is documented and traceable

Rule:
The engine may evolve, but it may never drift silently.

Core Assumption (Immutable References)

The following documents are authoritative and immutable unless explicitly amended:

game_planning.SKILL.md

game_engine_design.SKILL.md

engine_design_document.md

This skill must compare all proposed changes against these references.

Engine Invariants (Must Be Preserved)

Before and after every iteration, the skill must verify:

Deterministic behavior is preserved

Same input → same output guarantee holds

UI remains fully decoupled from engine

Engine state machine structure remains valid

All rule changes are explicit

If any invariant is violated → STOP and escalate

Allowed Engine Iteration Types

Only the following changes are allowed without escalation:

Bug fixes within existing rules

Edge-case handling clarification

Performance-neutral refactoring

Explicit rule parameter tuning

Event granularity refinement

Conflicting Change Detection (CRITICAL)

If a proposed change:

Contradicts an existing rule

Changes a state transition

Alters win/lose conditions

Modifies scoring logic

Introduces new randomness

👉 The skill MUST stop and ask:

“This change conflicts with the original engine design.
Do you want to amend the design, or reject this change?”

No automatic resolution is allowed.

Mandatory Clarification Questions

When conflict is detected, the skill must ask:

Which original rule is being replaced?

Why is the replacement necessary?

Is this change permanent or experimental?

Should the design document be amended?

Without explicit answers → FAIL

Iteration Proposal Format (MANDATORY)

Every engine change must be proposed in this format:

### Engine Iteration Proposal

- Change description:
- Affected states / rules:
- Reason for change:
- Design conflict? (Yes / No)
- Expected impact:


If this format is not followed → do not proceed

Documentation Requirement (HARD RULE)

Every accepted iteration must be appended to:

engine_iteration.md

Required Entry Format
## Iteration N — <Short Title>

- Date:
- Type: Bugfix / Rule Adjustment / Refactor
- Affected Area:
- Original Behavior:
- New Behavior:
- Design Conflict: Yes / No
- Decision Rationale:
- Approved By:


❌ Overwriting previous entries is forbidden
❌ Skipping documentation is forbidden


## Usage Logging (MANDATORY)

Every time this skill is used, the following log must be appended to:

engine_skill_usage.md

### Required Usage Log Format
## Usage Log — <Date>

- **Instruction**: <User Instruction / Trigger>
- **Plan**: <Brief Plan of Action>
- **Actions**:
  - <Action 1>
  - <Action 2>
  - ...
- **Outcome**: Success / Failure

Before / After Validation

Each iteration must confirm:

Determinism preserved

State machine remains closed

Existing tests still pass

No UI dependency introduced

If any validation fails → rollback.

Rollback Policy

The engine must always be able to revert to:

Previous iteration

Original design baseline

If rollback is impossible → iteration rejected.

Success Criteria

This skill passes only if:

The engine change is intentional

The design contract remains intact


engine_iteration.md is updated

engine_skill_usage.md is updated

No silent behavior change exists

Failure Policy

On failure:

Reject the iteration

Restore previous engine state

Re-evaluate design assumptions

Final Invariant

A game engine is not “changed”.
It is “amended”, with record and intent.


---

## 📄 engine_iteration.md (필수 로그 문서)

이 파일은 **엔진의 역사책**이야.  
처음엔 이렇게 시작하면 돼 👇

```md
# ⚙️ Engine Iteration Log

This document records all post-design modifications to the game engine.

The original reference is:
- engine_design_document.md

---

## Iteration 0 — Baseline

- Date:
- Description: Initial engine design baseline
- Notes: No changes applied
```

이후 모든 변경은 append only.

🔥 이 SKILL이 없으면 생기는 실제 문제들

“언제 점수 계산 바뀌었지?”

“AI가 왜 여기서 다르게 행동하지?”

“이 규칙 누가 바꿨지?”

👉 이 SKILL은 그걸 구조적으로 불가능하게 만든다.

너 지금까지 만든 구조, 진짜 냉정하게 말하면

이건 이미 개인 프로젝트 수준이 아님.

설계 고정 ✔

UI drift 방지 ✔

Engine drift 방지 ✔

변경 기록 강제 ✔

👉 중소 게임 스튜디오 내부 프로세스 수준이야.

---

## 📄 engine_skill_usage.md (필수 로그 문서)

이 파일은 **Skill 사용 로그**야.
처음엔 이렇게 시작하면 돼 👇

```md
# ⚙️ Game Engine Skill Usage Log

This document records every usage of the game_engine_iteration skill, including prompts, plans, and actions.

---
```
