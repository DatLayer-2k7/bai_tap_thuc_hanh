"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"

# Tạo thư mục cha nếu chưa tồn tại
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi hai dòng với encoding="utf-8"
lines = [
    "Xin chào, Python!",
    "Đây là bài tập đọc/ghi file UTF-8.",
]
with path.open("w", encoding="utf-8") as file:
    file.write("\n".join(lines))

# Đọc file và in từng dòng kèm số thứ tự
with path.open("r", encoding="utf-8") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.rstrip()}")

print(path)
