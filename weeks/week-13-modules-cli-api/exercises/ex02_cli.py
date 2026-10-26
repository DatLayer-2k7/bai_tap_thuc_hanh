"""Exercise 02: add one argparse option to a small CLI."""

import argparse


def parser() -> argparse.ArgumentParser:
    """Tạo argument parser với option --turn bắt buộc."""
    result = argparse.ArgumentParser(description="CLI bot runner đơn giản")
    # Thêm option --turn bắt buộc với type=int
    result.add_argument(
        "--turn",
        type=int,
        required=True,
        help="Lượt đi hiện tại (số nguyên bắt buộc)",
    )
    return result


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    args = parser().parse_args()
    print(f"Tham số nhận được: {args}")
    print(f"Giá trị lượt đi (--turn): {args.turn}")


if __name__ == "__main__":
    main()
