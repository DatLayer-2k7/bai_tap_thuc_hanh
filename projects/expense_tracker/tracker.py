"""Personal Expense Tracker with validation and JSON persistence."""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

Expense = dict[str, Any]


def add_expense(expenses: list[Expense], category: str, amount: float, description: str = "") -> bool:
    """Add a valid expense; return False if its fields are invalid."""
    if not isinstance(category, str) or not category.strip():
        return False
    if isinstance(amount, bool) or not isinstance(description, str):
        return False
    try:
        numeric_amount = float(amount)
    except (TypeError, ValueError):
        return False
    if not math.isfinite(numeric_amount) or numeric_amount <= 0:
        return False
    expenses.append({"category": category.strip(), "amount": numeric_amount, "description": description.strip()})
    return True


def calculate_total(expenses: list[Expense]) -> float:
    """Return the sum of expense amounts; an empty list totals zero."""
    return sum(float(item["amount"]) for item in expenses)


def filter_by_category(expenses: list[Expense], category: str) -> list[Expense]:
    """Filter by category without case sensitivity or outer whitespace."""
    if not isinstance(category, str) or not category.strip():
        return []
    target = category.strip().casefold()
    return [item for item in expenses if str(item.get("category", "")).strip().casefold() == target]


def get_highest_expense(expenses: list[Expense]) -> Expense | None:
    """Return the largest expense, or None for an empty list."""
    return max(expenses, key=lambda item: float(item["amount"])) if expenses else None


def save_expenses(expenses: list[Expense], path: str | Path) -> None:
    """Write expenses to a UTF-8 JSON file."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2, allow_nan=False)


def load_expenses(path: str | Path) -> list[Expense]:
    """Load validated expenses; missing files start with an empty list."""
    source = Path(path)
    if not source.exists():
        return []
    try:
        with source.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {source}") from error
    if not isinstance(data, list):
        raise ValueError("Expense data must be a JSON list")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each expense must be a JSON object")
        category = item.get("category")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Each expense needs a non-empty category")
        amount = item.get("amount")
        if isinstance(amount, bool):
            raise ValueError("Expense amount must be a positive number")
        try:
            numeric_amount = float(amount)
        except (TypeError, ValueError) as error:
            raise ValueError("Expense amount must be a positive number") from error
        if not math.isfinite(numeric_amount) or numeric_amount <= 0:
            raise ValueError("Expense amount must be a positive number")
        item["amount"] = numeric_amount
        item.setdefault("description", "")
        if not isinstance(item["description"], str):
            raise ValueError("Expense description must be text")
    return data


def format_expense(item: Expense) -> str:
    """Format a single expense for terminal display."""
    description = f" ({item['description']})" if item.get("description") else ""
    return f"- [{item['category']}] {float(item['amount']):,.0f} đ{description}"


def display_report(expenses: list[Expense]) -> None:
    """Print expenses, total spending, and the largest expense."""
    print("=" * 40)
    print("       BÁO CÁO CHI TIÊU CÁ NHÂN")
    print("=" * 40)
    if not expenses:
        print("Chưa có khoản chi tiêu nào.")
        return
    for item in expenses:
        print(format_expense(item))
    print("-" * 40)
    print(f"Tổng chi tiêu: {calculate_total(expenses):,.0f} đ")
    highest = get_highest_expense(expenses)
    if highest is not None:
        print(f"Khoản chi lớn nhất: {highest['category']} ({float(highest['amount']):,.0f} đ)")
    print("=" * 40)


def main() -> None:
    """Run the menu-driven app and store data in expenses.json."""
    data_path = Path(__file__).with_name("expenses.json")
    try:
        expenses = load_expenses(data_path)
    except ValueError as error:
        print(f"Không thể đọc dữ liệu: {error}")
        print("Hãy sửa hoặc đổi tên file expenses.json trước khi chạy lại.")
        return

    while True:
        print("\n=== QUẢN LÝ CHI TIÊU ===")
        print("1. Thêm khoản chi")
        print("2. Xem báo cáo")
        print("3. Lọc theo danh mục")
        print("4. Xem tổng chi tiêu")
        print("5. Lưu dữ liệu")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            category = input("Danh mục: ")
            amount_text = input("Số tiền (VND): ").strip()
            description = input("Mô tả (có thể để trống): ")
            try:
                amount = float(amount_text)
            except ValueError:
                print("Số tiền phải là một con số.")
                continue
            if add_expense(expenses, category, amount, description):
                save_expenses(expenses, data_path)
                print("Đã thêm và lưu khoản chi.")
            else:
                print("Dữ liệu không hợp lệ; khoản chi chưa được thêm.")
        elif choice == "2":
            display_report(expenses)
        elif choice == "3":
            display_report(filter_by_category(expenses, input("Danh mục cần lọc: ")))
        elif choice == "4":
            print(f"Tổng chi tiêu: {calculate_total(expenses):,.0f} đ")
        elif choice == "5":
            save_expenses(expenses, data_path)
            print(f"Đã lưu dữ liệu tại {data_path}")
        elif choice == "0":
            save_expenses(expenses, data_path)
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ; hãy chọn lại.")


if __name__ == "__main__":
    main()
