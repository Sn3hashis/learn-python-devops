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

<!--calendar-start-->
### July 2025 🌞

| Mo | Tu | We | Th | Fr | Sa | Su |
|----|----|----|----|----|----|----|
|      |      |      |      |      |      |      |
|      |      |      |      |      |      |      |
|      |      |      |      |      |      |      |
|      | [22🚧](./Days/2025-07-22.md) | [23🚧](./Days/2025-07-23.md) | [24🚧](./Days/2025-07-24.md) | [25🚧](./Days/2025-07-25.md) | [26🚧](./Days/2025-07-26.md) | [27🚧](./Days/2025-07-27.md) |
| [28🚧](./Days/2025-07-28.md) | [29🚧](./Days/2025-07-29.md) | [30🚧](./Days/2025-07-30.md) | [31🚧](./Days/2025-07-31.md) |      |      |      |


### August 2025 🌞

| Mo | Tu | We | Th | Fr | Sa | Su |
|----|----|----|----|----|----|----|
|      |      |      |      | [1🚧](./Days/2025-08-01.md) | [2🚧](./Days/2025-08-02.md) | [3🚧](./Days/2025-08-03.md) |
| [4🚧](./Days/2025-08-04.md) | [5🚧](./Days/2025-08-05.md) | [6🚧](./Days/2025-08-06.md) | [7🚧](./Days/2025-08-07.md) | [8🚧](./Days/2025-08-08.md) | [9🚧](./Days/2025-08-09.md) | [10🚧](./Days/2025-08-10.md) |
| [11🚧](./Days/2025-08-11.md) | [12🚧](./Days/2025-08-12.md) | [13🚧](./Days/2025-08-13.md) | [14🚧](./Days/2025-08-14.md) | [15🚧](./Days/2025-08-15.md) | [16🚧](./Days/2025-08-16.md) | [17🚧](./Days/2025-08-17.md) |
| [18🚧](./Days/2025-08-18.md) | [19🚧](./Days/2025-08-19.md) | [20🚧](./Days/2025-08-20.md) | [21🚧](./Days/2025-08-21.md) | [22🚧](./Days/2025-08-22.md) | [23🚧](./Days/2025-08-23.md) | [24🚧](./Days/2025-08-24.md) |
| [25🚧](./Days/2025-08-25.md) | [26🚧](./Days/2025-08-26.md) | [27🚧](./Days/2025-08-27.md) | [28🚧](./Days/2025-08-28.md) | [29🚧](./Days/2025-08-29.md) | [30🚧](./Days/2025-08-30.md) | [31🚧](./Days/2025-08-31.md) |


### September 2025 🌞

| Mo | Tu | We | Th | Fr | Sa | Su |
|----|----|----|----|----|----|----|
| [1🚧](./Days/2025-09-01.md) | [2🚧](./Days/2025-09-02.md) | [3🚧](./Days/2025-09-03.md) | [4🚧](./Days/2025-09-04.md) | [5🚧](./Days/2025-09-05.md) | [6🚧](./Days/2025-09-06.md) | [7🚧](./Days/2025-09-07.md) |
| [8🚧](./Days/2025-09-08.md) | [9🚧](./Days/2025-09-09.md) | [10🚧](./Days/2025-09-10.md) | [11🚧](./Days/2025-09-11.md) | [12🚧](./Days/2025-09-12.md) | [13🚧](./Days/2025-09-13.md) | [14🚧](./Days/2025-09-14.md) |
| [15🚧](./Days/2025-09-15.md) | [16🚧](./Days/2025-09-16.md) | [17🚧](./Days/2025-09-17.md) | [18🚧](./Days/2025-09-18.md) | [19🚧](./Days/2025-09-19.md) | [20🚧](./Days/2025-09-20.md) | [21🚧](./Days/2025-09-21.md) |
| [22🚧](./Days/2025-09-22.md) |      |      |      |      |      |      |
|      |      |      |      |      |      |      |
<!--calendar-end-->