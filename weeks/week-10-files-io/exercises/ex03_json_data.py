"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "replay.json"
replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}

# Tạo thư mục cha trước khi ghi file
path.parent.mkdir(parents=True, exist_ok=True)

# Lưu replay với ensure_ascii=False và indent=2
with path.open("w", encoding="utf-8") as file:
    json.dump(replay, file, ensure_ascii=False, indent=2)

# Tải lại và kiểm tra cả hai nhãn trước khi đọc turns
with path.open("r", encoding="utf-8") as file:
    loaded = json.load(file)

if loaded.get("format") == "COURSE LOCAL FORMAT" and loaded.get("production_compatibility") == "NOT VUACOC PRODUCTION FORMAT":
    print(loaded["turns"])

print(json.__name__, path, replay)
