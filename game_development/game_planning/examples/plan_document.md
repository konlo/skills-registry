# 🎮 Game Design Plan Document

## 1. Game Overview

- **Working Title:** GoStop (temporary)
- **Genre:** Traditional Card Game / Casual Strategy
- **Platform:** iOS (iPhone)
- **Target Audience:**
  - Age: 20–60
  - Familiar with GoStop rules
  - Casual players seeking short sessions

---

## 2. Core Player Fantasy

> “I am a clever GoStop player who makes smart decisions and enjoys small victories.”

---

## 3. Core Gameplay Loop (CRITICAL)



Draw / Play Card
→ Match or Event Occurs
→ Immediate Feedback (score, animation, sound)
→ Small Reward or Tension
→ Player Chooses Next Action


This loop must complete in **under 5 seconds**.

---

## 4. Session Design

- **Average Session Length:** 3–5 minutes
- **Session Start:** Immediate card dealing
- **Session End:** Win, lose, or stop decision

---

## 5. Game Rules Scope

### Included (v1.0)
- Basic GoStop rules (2-player)
- Go / Stop decision logic
- Score calculation (Gwang, Tti, Pe, Godori)
- Simple AI opponent

### Excluded (Intentionally)
- Online multiplayer
- 3+ player rules
- Complex regional house rules
- Betting with real money

---

## 6. Progression & Retention

- Player tracks win streaks
- Unlockable card backs (visual reward)
- Daily play satisfaction, not obligation

---

## 7. AI Design Role

- AI acts as **competent opponent**
- Deterministic rules engine (no cheating)
- Plays fast (< 1s decision time)

---

## 8. Success Metric (North Star)

> **Metric:** "One More Round" Rate > 30%

- Percentage of sessions where the player starts a new game immediately after finishing one.
- This confirms the core loop is addictive and fun.

---

## 9. First 30 Seconds Experience

1. **SPLASH (0s):** Clean logo, "Tap to Play"
2. **ACTION (2s):** User taps "Play" → Cards dealt immediately with satisfying 'snap' sound
3. **FIRST TURN (5s):** User matches a pair → Bright visual feedback + Haptic
4. **FEELING:** "I understand this, it involves no friction."

---

## 10. Non-Goals (Explicitly Out of Scope)

This game will **NOT** attempt to be:
- ❌ A gambling app (No real money, no in-app currency for betting)
- ❌ A social network (No chat, no friends list)
- ❌ A massive RPG (No leveling up characters, no inventory)

---

## 11. UX Principles

- One-hand play (Thumb zone priority)
- Minimal UI (No clutter)
- Clear feedback for every action
- No tutorials longer than 10 seconds

---

## 12. Technical Boundaries

- Deterministic game engine
- UI separated from logic
- AI decisions never modify rules

---

## 13. Next Steps

- `game_engine_design.skill`
- `ui_flow_design.skill`
- `gostop_rules_core.skill`
