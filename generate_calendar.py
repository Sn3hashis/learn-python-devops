import datetime
import os
from calendar import monthrange, month_name

# CONFIGURATION
start_date = datetime.date(2025, 7, 22)  # Start date of your learning
total_days = 63  # Total number of days (e.g. 9 weeks)
days_dir = "Days"
readme_file = "README.md"

def get_day_status(day_file_path):
    if not os.path.exists(day_file_path):
        return "❌"
    with open(day_file_path, "r") as f:
        first_line = f.readline().strip()
        if first_line.startswith("✅"):
            return "✅"
        elif first_line.startswith("🚧"):
            return "🚧"
    return "❌"

def generate_day_file(day_file_path):
    if not os.path.exists(day_file_path):
        with open(day_file_path, "w") as f:
            f.write(f"🚧 Day started on {os.path.basename(day_file_path)[:-3]}\n\n")
            f.write("### What I learned today:\n\n- \n")
            f.write("\n### Notes:\n\n- \n")
            f.write("\n### Links:\n\n- \n")

def build_calendar(start_date, total_days):
    calendar_output = ""
    current_date = start_date
    end_date = start_date + datetime.timedelta(days=total_days)

    while current_date < end_date:
        year = current_date.year
        month = current_date.month
        month_title = f"### {month_name[month]} {year} 🌞\n\n"
        calendar_output += month_title
        calendar_output += "| Mo | Tu | We | Th | Fr | Sa | Su |\n"
        calendar_output += "|----|----|----|----|----|----|----|\n"

        first_day = datetime.date(year, month, 1)
        first_weekday = first_day.weekday()
        days_in_month = monthrange(year, month)[1]

        week = ["    "] * 7
        day_num = 1
        finished = False

        while not finished:
            for i in range(7):
                if (day_num == 1 and i < first_weekday) or day_num > days_in_month:
                    continue

                day_date = datetime.date(year, month, day_num)
                if not (start_date <= day_date < end_date):
                    week[i] = "    "
                else:
                    day_file = os.path.join(days_dir, f"{day_date}.md")
                    generate_day_file(day_file)
                    status = get_day_status(day_file)
                    week[i] = f"[{day_num}{status}](./{day_file})"

                day_num += 1
                if day_num > days_in_month:
                    finished = True

            calendar_output += "| " + " | ".join(cell.rjust(4) for cell in week) + " |\n"
            week = ["    "] * 7

        calendar_output += "\n\n"
        current_date = datetime.date(year, month, 1) + datetime.timedelta(days=32)
        current_date = current_date.replace(day=1)

    return calendar_output.strip()

def insert_calendar_into_readme(calendar_md, readme_path=readme_file):
    start_marker = "<!--calendar-start-->"
    end_marker = "<!--calendar-end-->"

    if not os.path.exists(readme_path):
        print(f"{readme_path} not found. Creating a new one.")
        with open(readme_path, "w") as f:
            f.write(f"{start_marker}\n{calendar_md}\n{end_marker}")
        return

    with open(readme_path, "r") as f:
        content = f.read()

    if start_marker not in content or end_marker not in content:
        content += f"\n\n{start_marker}\n{calendar_md}\n{end_marker}"
    else:
        pre = content.split(start_marker)[0]
        post = content.split(end_marker)[1]
        content = f"{pre}{start_marker}\n{calendar_md}\n{end_marker}{post}"

    with open(readme_path, "w") as f:
        f.write(content)

def main():
    os.makedirs(days_dir, exist_ok=True)
    calendar_md = build_calendar(start_date, total_days)
    insert_calendar_into_readme(calendar_md)
    print("✅ Calendar updated successfully.")

if __name__ == "__main__":
    main()
