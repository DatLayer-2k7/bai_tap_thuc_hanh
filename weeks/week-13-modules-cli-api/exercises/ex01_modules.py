"""Exercise 01: imports, modules and main guard."""

# TODO: import choose_action từ bot_course.core.
from bot_course.core import choose_action
# TODO: chỉ gọi function bên trong main().
def main() -> None:
    """Call the bot decision function from inside the main entry point."""
    result = choose_action(1, 4)
    print(result)
# TODO: thêm guard if __name__ == "__main__".
if __name__ == "__main__":
    main()
