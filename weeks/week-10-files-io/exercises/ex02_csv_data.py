"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]

# Tạo thư mục cha trước khi mở file
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi header và rows bằng csv.DictWriter
fieldnames = ["bot", "wins"]
with path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Đọc rows bằng csv.DictReader rồi in kết quả
with path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

print(csv.__name__, path, rows)
