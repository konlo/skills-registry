# skills-registry
konlo's skills

skills-registry/
├─ apple/
│  ├─ apple_app_init.skill.yaml
│  ├─ apple_signing_check.skill.yaml
│
├─ games/
│  ├─ gostop_app_init.skill.yaml
│  ├─ gostop_rules_core.skill.yaml
│  ├─ gostop_ai_decision.skill.yaml
│
├─ ui/
│  ├─ swiftui_intent.skill.yaml
│
├─ testing/
│  ├─ apple_preflight_test.skill.yaml
│
└─ README.md


🧷 Project에서는 어떻게 쓰나?
방법 1️⃣ Git Submodule (가장 깔끔)
git submodule add https://github.com/you/skills-registry skills
git submodule update --init --recursive

gostop-ios/
├─ skills/        ← 참조만 함
├─ GostopApp/
└─ GostopApp.xcodeproj


✔ 특정 commit에 pin 가능
✔ 실험/운영 분리 가능
