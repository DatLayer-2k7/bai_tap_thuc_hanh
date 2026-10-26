"""Exercise 01: imports, modules and main guard."""

import sys
from pathlib import Path

# Đảm bảo import được package bot_course từ thư mục tuần 13
WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

# 1. Import choose_action từ bot_course.core
from bot_course.core import choose_action  # noqa: E402


def main() -> None:
    """2. Chỉ gọi function bên trong main()."""
    position = 1
    goal = 4
    action = choose_action(position, goal)
    print(f"Vị trí: {position}, Đích: {goal} -> Hành động: {action}")


# 3. Guard if __name__ == "__main__"
if __name__ == "__main__":
    main()
