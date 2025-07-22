# 🐍 Learn Python for DevOps — Calendar-Driven Tracker

Welcome to **`learn-python-devops`**, a visual learning tracker powered by a smart Markdown calendar. This repository is part of a 9-week structured Python for DevOps journey, with auto-generated daily notes and visual progress indicators — perfect for publishing to GitHub Pages or using locally.

---

## 📌 Purpose

This repo aims to:

- Track **daily Python DevOps learning progress** visually.
- Auto-generate Markdown day files like `Days/2025-07-22.md` with notes or checklist areas.
- Update a dynamic calendar in `README.md` with clickable emojis (✅, 🚧).
- Auto-commit changes using **GitHub Actions** daily or on every push.

---

## 🧠 How It Works

- `generate_calendar.py`:
  - Builds a Markdown calendar for your learning period.
  - Links each day to a `Days/YYYY-MM-DD.md` file.
  - Adds emojis to track progress (`✅`, `🚧`, etc.).
  - Creates that day’s file if it doesn't exist yet.

- `.github/workflows/calendar.yml`:
  - Runs the script on every push to `main`.
  - Uses `git-auto-commit-action` to commit updates.
  - Requires repo permissions (`contents: write`).

---

## ⚙️ Setup Instructions

### 1. Clone the repo and set start date

```bash
git clone https://github.com/Sn3hashis/learn-python-devops.git
cd learn-python-devops