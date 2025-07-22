#!/usr/bin/env python3
"""
calendar.py — generates a 9-week Markdown calendar and daily note files
for Python‑for‑DevOps learning tracker.
"""

import datetime
from calendar import month_name

START_DATE = datetime.date(2025, 7, 22)
WEEKS = 9
DAYS_PER_WEEK = 6  # Monday–Saturday

DAY_TITLES = [
    # Week 1
    "Install Python & IDE setup",
    "Data types: strings, numbers, lists, tuples, sets, dicts",
    "Operators & expressions",
    "Control flow: if, elif, else",
    "Loops: for, while",
    "Functions: def, args, return",
    # Week 2
    "Error handling: try/except/finally",
    "File I/O & context managers",
    "Comprehensions & lambdas",
    "Modules & imports",
    "Virtualenv, pip, logging, debugging",
    "Argparse & mini script",
    # Week 3
    "os & subprocess",
    "File ops: copy/move/delete",
    "Env vars & shell integration",
    "Scheduling: cron/schedule",
    "Practice: file rotation/backup",
    "Mini project: cleanup tool",
    # Week 4
    "HTTP basics & requests",
    "REST API: GET/POST/auth",
    "JSON/XML parsing",
    "Sockets & networking basics",
    "Practice: service monitor + notify",
    "Mini project: API status checker",
    # Week 5
    "IaC & Ansible basics",
    "Custom Ansible modules",
    "Fabric/Invoke remote exec",
    "Terraform/Salt with Python",
    "Practice: deployment script",
    "Mini project: Ansible tool",
    # Week 6
    "Docker fundamentals & SDK",
    "Docker: builds, pushes, image mgmt",
    "K8s basics & Python client",
    "Manage pods/deployments",
    "Practice: K8s auto-scaler",
    "Mini project: container automation",
    # Week 7
    "AWS intro & Boto3 setup",
    "Automating EC2, S3, IAM",
    "GCP & Azure SDK basics",
    "Auth best practices",
    "Practice: infra provisioning",
    "Mini project: cloud manager",
    # Week 8
    "Unit testing: unittest/pytest",
    "Linting/formatting: flake8/black",
    "Integrate Python in CI/CD pipelines",
    "Logging & monitoring integrations",
    "Practice: smoke testing pipeline",
    "Mini project: CI/CD test script",
    # Week 9
    "Multithreading & multiprocessing",
    "Async programming with asyncio",
    "Webhooks & event-driven scripting",
    "REST APIs with Flask/FastAPI",
    "Final project planning & testing",
    "Capstone: end‑to‑end automation"
]

def mk_calendar():
    cal_lines = []
    header = ["Week", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    cal_lines.append("| " + " | ".join(header) + " |")
    cal_lines.append("|" + "|".join(["------"] * len(header)) + "|")

    day = START_DATE
    idx = 0
    for week in range(WEEKS):
        row = [f"{week+1}"]
        for d in range(DAYS_PER_WEEK):
            title = DAY_TITLES[idx] if idx < len(DAY_TITLES) else ""
            date_str = day.isoformat()
            link = f"[⏳ Day {idx+1}](Days/{date_str}.md)<br>{title}"
            row.append(link)
            idx += 1
            day += datetime.timedelta(days=1)
        cal_lines.append("| " + " | ".join(row) + " |")
        # skip Sunday
        day += datetime.timedelta(days=1)
    return "\n".join(cal_lines)

def mk_readme():
    today = datetime.date.today().isoformat()
    return f"""# learn‑python‑devops

**Start Date:** {START_DATE.isoformat()}

## 🗓️ Python for DevOps – 9‑Week Tracker
_Calendar updates automatically via GitHub Actions_

{mk_calendar()}

---

## ✅ Progress Log
_(Commit daily notes and reflections to the `Days/` folder.)_

## 📚 Resources
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python for DevOps book](https://www.nogoodpublishers.com/) *(sample placeholder)*

"""

def mk_day_file(date, title, day_number):
    return f"""# Day {day_number} – {date.strftime('%B %d, %Y')}

## ✅ Topic
Day {day_number} – {title}

## 📝 Notes
- 

## ✅ Completed
- [ ] Studied module
- [ ] Completed mini practice
- [ ] Committed notes and log
"""

def main():
    today = datetime.date.today()
    readme = mk_readme()
    with open("README.md", "w") as f:
        f.write(readme)

    day = START_DATE
    for idx, title in enumerate(DAY_TITLES, start=1):
        # skip Sundays
        weekday = day.weekday()  # Mon=0...Sun=6
        if weekday >= 6:
            day += datetime.timedelta(days=(7 - weekday))
        fname = f"Days/{day.isoformat()}.md"
        content = mk_day_file(day, title, idx)
        with open(fname, "w") as f:
            f.write(content)
        day += datetime.timedelta(days=1)

if __name__ == "__main__":
    main()
