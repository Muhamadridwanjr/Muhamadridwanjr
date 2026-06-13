# 🤝 Contributing to Golden Dragon Ecosystem

First off — **thank you** for considering contributing to the Golden Dragon Ecosystem. Every pull request, bug report, documentation improvement, and idea makes this ecosystem better for every developer who uses it.

This document is your guide to becoming part of the GDE community. Please read it carefully before contributing.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Branching Strategy](#branching-strategy)
- [Commit Conventions](#commit-conventions)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Documentation Standards](#documentation-standards)
- [Community](#community)

---

## ⚖️ Code of Conduct

By participating in this project, you agree to uphold our community standards:

- **Be respectful** — Treat every contributor with dignity, regardless of background or experience level
- **Be constructive** — Criticism should be aimed at code and ideas, never at people
- **Be inclusive** — We welcome contributors from all backgrounds, especially from Indonesia and Southeast Asia
- **Be transparent** — Be honest about your intentions, capabilities, and changes
- **Be patient** — Open source is a volunteer effort; response times may vary

Violations of these standards may result in removal from the community.

---

## 🛠️ How to Contribute

There are many ways to contribute — coding isn't the only one:

| Contribution Type | How |
|---|---|
| 🐛 **Bug Fix** | Find an issue, fork, fix, PR |
| ✨ **New Feature** | Open a discussion first, then implement |
| 📖 **Documentation** | Improve clarity, fix typos, add examples |
| 🧪 **Tests** | Add missing test coverage |
| 🎨 **Design** | UI/UX improvements for dashboards |
| 💡 **Ideas** | Open a GitHub Discussion |
| 🌍 **Translation** | Help translate docs to Bahasa Indonesia |
| 🔍 **Code Review** | Review open pull requests |

---

## ⚙️ Development Setup

### Prerequisites

```bash
# Required
Python >= 3.10
Node.js >= 18.x
Docker >= 24.x
Git >= 2.40

# Recommended
VS Code with Python & Docker extensions
```

### Local Setup

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Muhamadridwanjr.git
cd Muhamadridwanjr

# 3. Add upstream remote
git remote add upstream https://github.com/Muhamadridwanjr/Muhamadridwanjr.git

# 4. Create virtual environment (Python projects)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 5. Install dependencies
pip install -r requirements.txt
# or
npm install

# 6. Copy environment config
cp .env.example .env
# Edit .env with your local settings

# 7. Run tests to verify setup
pytest tests/ -v
```

### Docker Setup (Preferred)

```bash
# Build and start all services
docker-compose up -d --build

# Check service status
docker-compose ps

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

---

## 🌿 Branching Strategy

We follow **GitHub Flow** — simple, clean, and effective.

```
main           → Production-ready code. Always deployable.
feature/*      → New features (feature/add-agent-memory)
fix/*          → Bug fixes (fix/webhook-timeout-error)
docs/*         → Documentation only (docs/update-contributing-guide)
refactor/*     → Code refactoring (refactor/cleanup-bot-handlers)
hotfix/*       → Critical production fixes (hotfix/security-patch)
```

### Rules:
- ❌ Never commit directly to `main`
- ✅ Always branch from `main` for new work
- ✅ Keep branches focused — one feature/fix per branch
- ✅ Delete your branch after the PR is merged

---

## 📝 Commit Conventions

We follow **Conventional Commits** specification for clean, machine-readable history:

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

### Types:

| Type | Use When |
|---|---|
| `feat` | Adding a new feature |
| `fix` | Fixing a bug |
| `docs` | Documentation changes only |
| `style` | Code formatting, no logic changes |
| `refactor` | Code restructuring, no feature/fix |
| `test` | Adding or updating tests |
| `chore` | Build process, tooling, CI/CD |
| `perf` | Performance improvements |
| `security` | Security fixes or hardening |

### Examples:

```bash
git commit -m "feat(bot): add webhook failover with exponential backoff"
git commit -m "fix(trading): resolve null pointer in signal parser"
git commit -m "docs(readme): add docker deployment section"
git commit -m "security(auth): enforce JWT expiry validation"
```

---

## 🔀 Pull Request Process

### Before Submitting

- [ ] Code follows the project's style guide
- [ ] Tests written and passing (`pytest tests/` or `npm test`)
- [ ] Documentation updated if needed
- [ ] No hardcoded secrets, tokens, or credentials
- [ ] Commits follow Conventional Commits format
- [ ] Branch is up-to-date with `main`

### PR Template

When opening a PR, fill in the template:

```markdown
## Summary
Brief description of what this PR does.

## Changes
- Added: [new feature/file]
- Modified: [changed behavior]
- Removed: [deleted code]

## Testing
- [ ] Unit tests added/updated
- [ ] Tested locally with Docker
- [ ] Edge cases considered

## Screenshots (if UI change)
Attach before/after screenshots.

## Related Issues
Closes #[issue number]
```

### Review Process

1. Submit PR → automated checks run
2. Maintainer assigned for review (within 48–72 hours)
3. Address review feedback via new commits (don't force-push during review)
4. Approval from 1+ maintainer required
5. Squash merge to `main` by maintainer

---

## 🐛 Reporting Bugs

### Before Reporting

- Search existing issues to avoid duplicates
- Confirm the bug exists on the latest version
- Try to reproduce in a clean environment

### Bug Report Template

```markdown
**Describe the Bug**
Clear, concise description of the problem.

**Steps to Reproduce**
1. Do this...
2. Then this...
3. See error

**Expected Behavior**
What should have happened.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python Version: [e.g., 3.11.2]
- Docker Version: [e.g., 24.0.7]
- Project Version/Commit: [e.g., v1.2.3 or abc1234]

**Logs**
Paste relevant error logs (use code blocks).

**Screenshots**
If applicable, add screenshots.
```

---

## 💡 Suggesting Features

We love new ideas. Before implementing, please:

1. **Open a Discussion** at [GitHub Discussions](https://github.com/Muhamadridwanjr/Muhamadridwanjr/discussions)
2. Describe the problem the feature solves
3. Propose a solution and consider alternatives
4. Wait for community feedback (at least 72 hours)
5. Get maintainer approval before starting implementation

Major features that affect architecture require an RFC (Request for Comment) document.

---

## 📚 Documentation Standards

Good documentation is as important as good code in this ecosystem:

- Write in **clear, simple English** (and Bahasa Indonesia where relevant)
- Include **code examples** for every public API
- Use **docstrings** for all functions and classes
- Keep **README files** up-to-date with every feature change
- Add **inline comments** for non-obvious logic only

---

## 🌏 Community

Join the Golden Dragon builder community:

- 💬 **Telegram**: [t.me/MuhamadRidwanjr](https://t.me/MuhamadRidwanjr)
- 🌐 **Website**: [muhamadridwanjr.xyz](https://muhamadridwanjr.xyz)
- 📋 **GitHub Discussions**: Use for questions, ideas, and community chat
- 🐛 **GitHub Issues**: Use for bugs and concrete feature requests

---

*🐉 Thank you for being part of the Golden Dragon Ecosystem. Together, we build systems that matter.*
