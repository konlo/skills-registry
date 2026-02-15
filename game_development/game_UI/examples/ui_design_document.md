# 🎨 UI Design Document: GoStop

## UX Core Philosophy
- **Speed is King:** Players should never wait for animations to finish to input their next move.
- **Clarity over Flash:** Every pixel must serve the game state.

---

## 1. Primary Player Actions
| Rank | Action | Frequency | UI Location / Trigger |
| :--- | :--- | :--- | :--- |
| **1** | **Play Card (Hand -> Field)** | Every Turn | Drag & Drop / Tap Hand Card |
| **2** | **Select Stack (Bomb/Chong)** | ~10% of Turns | Center Overlay (Contextual) |
| **3** | **Go / Stop Decision** | End of Game | Large Modal Buttons |

> **Optimization Rule:** The bottom 30% of the screen is reserved EXCLUSIVELY for "Play Card".

---

## 2. Visual Focus Hierarchy
1.  **Primary Focus (The Playing Field):** The 12 stations where cards match.
    - *Why:* This is where the game happens.
2.  **Secondary Focus (My Hand):** The cards I can play.
    - *Why:* This is my agency.
3.  **Tertiary Focus (Score & Status):** Current score, Go count.
    - *Why:* Important for decisions, but not for moment-to-moment play.

---

## 3. Action → Feedback Mapping

| User Action | Immediate Visual Feedback | Audio Feedback | Animation |
| :--- | :--- | :--- | :--- |
| **Tap Hand Card** | Card lifts slightly + Glow border | "Click" (Subtle) | Scale up 1.1x (50ms) |
| **Match Card** | Cards merge & move to score pile | "Snap" (Sharp) | Ark movement (200ms) |
| **Score Points** | Score number pulses Red | "Ding" | Pulse 1.2x (150ms) |
| **'Go' Selected** | Screen flash + Speed lines | "Go!" Voice | Burst effect (300ms) |
| **'Stop' Selected** | Dim background + Spotlight | "Stop!" Voice | Fade out (500ms) |

---

## 4. Animation Rules & Timing
- **Card Movement:** `spring(response: 0.3, dampingFraction: 0.7)`
    - *Feeling:* Snappy, physical.
- **Score Updates:** `easeInOut(duration: 0.2)`
    - *Feeling:* Immediate but noticeable.
- **Transitions (Turn Change):** `linear(duration: 0.1)`
    - *Feeling:* Almost instant.

> **Constraint:** No animation shall exceed 300ms.

---

## 5. Preview Strategy (SwiftUI)

### Required States for verification
1.  `#Preview("Empty Table")`: New game state.
2.  `#Preview("Mid-Game Complex")`: Many cards on field, high scores.
3.  `#Preview("End Game Decision")`: User must choose Go or Stop.
4.  `#Preview("Win Animation")`: Victory screen overlay.

```swift
// Example Preview Provider
#Preview {
    GameView(state: .mockMidGameReference)
}
```

---

## 6. Non-Goals (Visuals)
- No photorealistic wood textures (clean flat/gradient style).
- No complex 3D card flips (simple 2D sprite swaps).
- No avatar customization in the main game view.
