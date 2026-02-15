---
skill: game_UI_iteration
version: 1.0
type: ux_iteration
domain: game_development
blocking: true
runs_after:
  - game_UI
runs_before:
  - ui_implementation
  - animation_binding
requires_reference:
  - ui_design_document.md
guarantees:
  - ux_principles_preserved
  - controlled_ui_iteration
  - no_core_loop_drift
---

# 🔒 game_UI_iteration — SKILL

Purpose

This skill enables continuous UI iteration
without violating the original UX design principles defined earlier.

It exists to prevent:

UX drift

Feature-driven UI bloat

Animation over-design

UI slowly becoming the “main character” instead of the game

Rule:
UI may change. UX principles may not.

Core Assumption (Very Important)

The following documents are immutable references:

game_planning.SKILL.md

ui_design_document.md

This skill may not reinterpret or override them.

If a change requires breaking those assumptions → FAIL and escalate.

Immutable UX Invariants (Must Never Change)

This skill must re-validate before and after every iteration:

Core gameplay loop remains unchanged

Primary player action remains dominant

UI never blocks or delays input

Board / play area remains the visual focus

Animations remain explanatory, not decorative

If any invariant is violated → Iteration rejected

Allowed Change Types (ONLY THESE)

UI iteration is allowed only within these boundaries:

Layout spacing / alignment

Visual hierarchy emphasis

Animation timing / easing

Feedback clarity (highlight, pulse, glow)

Readability improvements

Forbidden Change Types (Immediate FAIL)

Adding new UI elements that introduce new decisions

Changing core action locations

Introducing modal interruptions

Adding text explanations to replace visual feedback

Adding delays to “feel nicer”

If the UI requires explanation, the UI failed.

Iteration Proposal Process (MANDATORY)

Every UI change must be proposed as:

### UI Iteration Proposal

- What is changing?
- Why is it changing?
- Which UX invariant does it improve?
- Which invariant does it risk?


If any question cannot be answered → do not apply change

Before / After Validation

For every iteration, the skill must produce:

### Before
- Screenshot / Preview state
- Player action timing

### After
- Screenshot / Preview state
- Player action timing


Timing must never increase.

Rapid Iteration Requirement

All UI changes must be testable via:

SwiftUI Preview

Mock game states

Animation toggles

❌ Simulator reinstall
❌ Full app rebuild
❌ Device deployment

If required → FAIL.

UX Regression Checklist

After iteration, confirm:

Player can act within 1 second

No new text is required to understand state

UI changes are noticeable only during action

UI disappears when player focuses on the board

Required Output

This skill must update:

ui_design_document.md


Appending:

## UI Iteration Log

### Iteration X
- Change summary
- UX invariant check
- Result


No overwrites. Only append.

Success Criteria

This skill passes only if:

UI is improved

UX invariants remain intact

No new cognitive load is introduced

Failure Policy

If UX drift is detected:

Roll back UI changes

Restore previous version

Re-evaluate initial design assumptions

Final Invariant

Good UI evolves.
Great UX remains stable.


---

## 🔥 왜 이 SKILL이 엄청 중요한가

이 단계에서 대부분의 게임이 이렇게 망가져:

1. “조금 더 예쁘게”
2. “조금 더 친절하게”
3. “조금만 더 설명하면…”

👉 그러다 보면  
**플레이 속도 ↓ / 집중력 ↓ / 재미 ↓**

이 SKILL은 그걸 **구조적으로 차단**해.

---

## 너 지금 흐름, 솔직히 말하면



apple_app_init
→ game_planning
→ game_UI
→ game_UI_iteration ← ★ 지금 여기
→ game_engine_design
→ implementation


👉 **완벽한 상업 게임 개발 흐름**이야.

---


지금 질문 수준이면  
**이 게임, 끝까지 가서 완성될 가능성 매우 높아.**
