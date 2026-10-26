"""Exercise 03: inspect an offline HTTP fixture."""

import sys
from pathlib import Path

# Đảm bảo import được package bot_course từ thư mục tuần 13
WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.http_foundation import parse_json_response  # noqa: E402

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect a successful offline response fixture."""
    # 1. Parse status 200 và assert lesson == 13
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13, f"Expected lesson 13, got {data['lesson']}"
    print(f"Dữ liệu phản hồi status 200 hợp lệ: {data}")

    # 2. Quan sát ValueError với status 500
    try:
        parse_json_response(500, b'{"error": "internal error"}')
    except ValueError as exc:
        print(f"Bắt được ngoại lệ ValueError như kỳ vọng với status 500: {exc}")


if __name__ == "__main__":
    main()   
