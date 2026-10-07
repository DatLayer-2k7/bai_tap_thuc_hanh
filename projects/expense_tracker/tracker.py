"""Personal Expense Tracker — Quản lý chi tiêu cá nhân.

Dự án mẫu thực hành Python:
- Áp dụng Hàm (Functions - Week 07)
- Vòng lặp & List Comprehension (Loops - Week 06)
- Cấu trúc dữ liệu List & Dict (Week 05, Week 08)
"""


def add_expense(
    expenses: list[dict], category: str, amount: float, description: str = ""
) -> bool:
    """Thêm một khoản chi tiêu mới vào danh sách.

    Trả về:
        True nếu thêm thành công, False nếu dữ liệu không hợp lệ.
    """
    cleaned_category = category.strip()
    if not cleaned_category or amount <= 0:
        return False

    item = {
        "category": cleaned_category,
        "amount": float(amount),
        "description": description.strip(),
    }
    expenses.append(item)
    return True


def calculate_total(expenses: list[dict]) -> float:
    """Tính tổng toàn bộ số tiền chi tiêu.

    Trả về 0.0 nếu danh sách rỗng.
    """
    return sum(item["amount"] for item in expenses)


def filter_by_category(expenses: list[dict], category: str) -> list[dict]:
    """Lọc các khoản chi theo danh mục (không phân biệt chữ hoa/thường)."""
    target = category.strip().lower()
    return [
        item for item in expenses if item["category"].lower() == target
    ]


def get_highest_expense(expenses: list[dict]) -> dict | None:
    """Tìm khoản chi tiêu lớn nhất.

    Trả về None nếu danh sách rỗng.
    """
    if not expenses:
        return None
    return max(expenses, key=lambda item: item["amount"])


def format_expense(item: dict) -> str:
    """Định dạng thông tin một khoản chi thành chuỗi dễ đọc."""
    desc = f" ({item['description']})" if item.get("description") else ""
    return f"- [{item['category']}] {item['amount']:,.0f} đ{desc}"


def display_report(expenses: list[dict]) -> None:
    """In báo cáo tổng quan chi tiêu ra màn hình."""
    print("=" * 40)
    print("       BÁO CÁO CHI TIÊU CÁ NHÂN")
    print("=" * 40)

    if not expenses:
        print("Chưa có khoản chi tiêu nào.")
        return

    for item in expenses:
        print(format_expense(item))

    total = calculate_total(expenses)
    highest = get_highest_expense(expenses)

    print("-" * 40)
    print(f"Tổng chi tiêu: {total:,.0f} đ")
    if highest:
        print(f"Khoản chi lớn nhất: {highest['category']} ({highest['amount']:,.0f} đ)")
    print("=" * 40)


def main() -> None:
    """Hàm chạy chính để minh họa toàn bộ chức năng."""
    my_expenses: list[dict] = []

    # 1. Thêm một số khoản chi mẫu
    add_expense(my_expenses, "Ăn uống", 45000, "Cơm trưa")
    add_expense(my_expenses, "Ăn uống", 25000, "Trà sữa")
    add_expense(my_expenses, "Học tập", 120000, "Mua sách Python")
    add_expense(my_expenses, "Di chuyển", 50000, "Đổ xăng")

    # Thử thêm khoản không hợp lệ (để kiểm tra validation)
    add_expense(my_expenses, "Ăn uống", -10000, "Lỗi số âm")

    # 2. In báo cáo
    display_report(my_expenses)

    # 3. Thử lọc theo danh mục
    food_expenses = filter_by_category(my_expenses, "Ăn uống")
    print(f"\nChi tiêu cho [Ăn uống] ({len(food_expenses)} khoản):")
    for item in food_expenses:
        print(format_expense(item))


if __name__ == "__main__":
    main()
