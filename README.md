
# 🐍 Learn Python for DevOps — Calendar-Driven Tracker 🌟

Welcome to **learn-python-devops**, a structured 9-week learning journey designed to master Python specifically for DevOps roles. 🚀  
This repository helps you:

- 📅 Track your learning with a visual calendar  
- 📝 Auto-generate daily Markdown files (like logs/notes)  
- 🔄 Keep your progress up-to-date with GitHub Actions  

---

## 📌 Project Purpose 🎯

This project was created to:

- Visually monitor and reflect Python learning progress for DevOps 📊  
- Enable a clean separation of daily learning logs in `Days/` 🗂️  
- Automatically update your `README.md` with a clickable calendar view 🖼️  
- Commit changes using GitHub Actions automatically 🤖  

It's inspired by tools like Obsidian-style learning calendars and markdown-first documentation workflows. ✨

---

## 🧠 How It Works 🛠️

`generate_calendar.py` does the magic: 🪄

- Builds a Markdown calendar for the specified learning window 📆  
- Each day links to a note file like `Days/2025-07-22.md` 📄  
- If that file doesn’t exist, it creates it 🆕  
- Emojis like ✅, 🚧, or ❌ represent the status for the day 🎨  

A GitHub Action (`calendar.yml`) automatically runs this script ⚙️  
It auto-commits changes to the repo including new day files and calendar updates 🔄  

---

## 📁 Directory Structure 🗂️

```
learn-python-devops/
│
├── Days/ 📂
│   ├── 2025-07-22.md ← Day-wise notes auto-generated 📄
│   └── ...
│
├── .github/workflows/ ⚙️
│   └── calendar.yml ← GitHub Actions workflow
│
├── generate_calendar.py ← Python script to build the calendar 🐍
├── README.md ← Contains calendar + documentation 📜
└── ...
```

---

<!--calendar-start-->
<!--calendar-end-->

## 📅 Example Calendar Output (in `README.md`) 🗓️

```
July 2025 🌞

Mo Tu We Th Fr Sa Su
  1  2  3  4  5  6
  7  8  9 10 11 12 13
 14 15 16 17 18 19 20
 21 22🚧 23 24 25 26 27
 28 29 30 31
```

---

## 🚀 How to Use This 🏃‍♂️

### 🔧 1. Clone and Set Start Date 📥
```bash
git clone https://github.com/Sn3hashis/learn-python-devops.git
cd learn-python-devops
```

Edit `generate_calendar.py` and update:

```python
start_date = datetime.date(2025, 7, 22)
total_days = 63  # 9 weeks
```

### 🖥️ 2. Run Locally (Optional) 🖱️
```bash
python generate_calendar.py
```

This will:

- Create/update a day file for today (`Days/YYYY-MM-DD.md`) 📝  
- Update the Markdown calendar in `README.md` 🗓️  

### ⚙️ 3. Enable GitHub Actions 🔄

The workflow file at `.github/workflows/calendar.yml` runs on every push.

Ensure this is set:

```yaml
permissions:
  contents: write
```

Auto-commit step:

```yaml
- uses: stefanzweifel/git-auto-commit-action@v4
  with:
    commit_message: 📅 Update calendar and daily note files
    file_pattern: .
```

---

## 💥 Issues Encountered & Fixes Applied 🛠️

| Issue | Fix |
|------|-----|
| ❌ ImportError: cannot import name 'month_name' from 'calendar' | Script was named `calendar.py`, conflicting with Python’s built-in module. Renamed to `generate_calendar.py`. |
| ❌ FileNotFoundError: No such file or directory: 'Days/2025-07-22.md' | Added `os.makedirs("Days", exist_ok=True)` in script |
| ❌ GitHub Actions auto-commit failed with exit code 1 | Added `permissions: contents: write` in workflow |
| ❌ Actions committed only README.md | Changed `file_pattern: README.md` to `file_pattern: .` |

---

## 🧪 Testing Locally 🧑‍🔬

Run the script:
```bash
python generate_calendar.py
```

Verify:
- ✅ New `Days/YYYY-MM-DD.md` file is created  
- ✅ `README.md` calendar is updated with a clickable emoji  

---

## 🧠 Emoji Legend 🎨

| Emoji | Meaning |
|-------|---------|
| ✅ | Completed |
| 🚧 | In Progress |
| ❌ | Not Started |

You can manually mark each `Days/YYYY-MM-DD.md` with a line like:  
`✅ Completed learning modules for Day 1`

Future versions may parse this automatically. 🔮

---

## 💡 Future Ideas 🚀

- Detect emoji from daily file content automatically 🧠  
- Add support for weekly summaries 📈  
- GitHub Pages view with custom styles 🎨  
- UI for adding notes or emojis per day 🖌️  

---

## 👨‍💻 Author & Credits 🙌

Made by [@sn3hashis](https://github.com/sn3hashis) 🌟  
Inspired by daily learning trackers, Zettelkasten/Obsidian markdown workflows, and calendar-based visual trackers.

**Tech used:**
- Python 3.10+ 🐍  
- GitHub Actions ⚙️  
- Markdown 📝  
- Emoji & date utils 😊  

---

## 🏁 License 📜

MIT License – feel free to fork and use for your own DevOps journey. 🌍
