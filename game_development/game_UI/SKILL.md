---
skill: game_UI
version: 1.0
type: ux_design
domain: game_development
blocking: true
runs_after:
  - game_planning
runs_before:
  - ui_implementation
  - animation_design
  - interaction_binding
guarantees:
  - action_focused_ui
  - fast_iteration_ux
  - non_intrusive_game_experience
---

# 🎮 game_UI — SKILL

## Purpose

This skill defines the **UX-first UI blueprint** for a game.

It ensures that:
- UI never interrupts gameplay
- Every player action receives immediate visual feedback
- Animations clarify intent instead of distracting the player
- UI/UX can be iterated **without rebuilding or reinstalling the app**

> **Rule:**  
> If UI slows down understanding or action, it is a bug — not a feature.

## Core UX Philosophy (20 years of Apple game UX)

- Players look at the board, not the UI
- UI exists to explain actions, not decorate screens
- Animations are not “effects” — they are communication
- If it takes more than 1 second to understand, it’s wrong
- The best UX is often barely noticed

## Required UX Questions (MANDATORY)

This skill must explicitly answer and document:

### 1. Primary Player Actions

- What is the single most common action?
- What is the second most common action?
- What action ends a session?

👉 UI must be optimized only for these.

### 2. Visual Focus Hierarchy

“Where should the player’s eyes be, by default?”

Define:
- Primary focus (always visible)
- Secondary focus (contextual)
- Tertiary UI (rare, dismissible)

If everything looks important → FAIL.

### 3. Action → Feedback Mapping (CRITICAL)

For every player action, define:

| Action | Visual Feedback | Animation Duration |
| :--- | :--- | :--- |
| Card play | Card moves + snap | ≤ 300ms |
| Score change | Number pulse | ≤ 200ms |
| Go/Stop | Button emphasis | ≤ 150ms |

If an action has no feedback, UX is incomplete.

## Animation Rules (Apple UX Standard)

- Duration: 100ms – 300ms
- Use easing, never linear
- No animation should block input
- Animation must clarify state change

❌ “Looks cool” is not a valid reason  
✅ “Explains what happened” is valid

## Rapid Iteration UX Strategy (VERY IMPORTANT)

Never require reinstalling the app to test UI.

### Required Techniques

- SwiftUI Preview-driven UI
- State-based UI rendering
- Fake / Mock Game State injection
- Animation toggles (on/off)

### Mandatory Rule

UI must be previewable without the game engine running

## Preview-Driven UX Workflow

The skill must enforce:

1. UI screens designed as pure functions of state
2. Multiple preview states:
    - Game start
    - Mid-game
    - Win / Lose
3. Animation preview isolation

**Example: Preview States**
```swift
#Preview("Mid Game") {
  GameBoardView(state: .mockMidGame)
}
```

## UX Validation Checklist

This skill FAILS if:

- UI blocks the board
- Animations delay player input
- Player must read text to understand state
- UI requires engine execution to preview

## Required Visual Artifacts

This skill must produce:

- UI layout sketches
- Animation intent descriptions
- Preview state list

These must be stored in:
`ui_design_document.md`

## Non-Goals

This skill does NOT:
- Implement UI code
- Polish visuals
- Choose colors or themes
- Optimize performance

It defines UX structure only.

## Final Invariant

The player should feel faster than the game.
