"""Unit tests cho Expense Tracker.

Kiểm tra tính đúng đắn của logic:
- Trường hợp hợp lệ (normal case)
- Dữ liệu không hợp lệ (invalid case)
- Danh sách rỗng (boundary/empty case)
"""
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from tracker import (
    add_expense,
    calculate_total,
    filter_by_category,
    get_highest_expense,
)


def test_add_valid_expense():
    """Kiểm tra thêm khoản chi hợp lệ."""
    data = []
    success = add_expense(data, "Ăn uống", 50000, "Bún bò")
    assert success is True
    assert len(data) == 1
    assert data[0]["amount"] == 50000


def test_add_invalid_amount_rejected():
    """Kiểm tra từ chối số tiền <= 0."""
    data = []
    success = add_expense(data, "Ăn uống", -20000)
    assert success is False
    assert len(data) == 0


def test_add_empty_category_rejected():
    """Kiểm tra từ chối danh mục chỉ toàn khoảng trắng hoặc rỗng."""
    data = []
    success = add_expense(data, "   ", 30000)
    assert success is False
    assert len(data) == 0


def test_calculate_total():
    """Kiểm tra tính tổng chi tiêu."""
    data = [
        {"category": "Ăn uống", "amount": 30000, "description": ""},
        {"category": "Học tập", "amount": 70000, "description": ""},
    ]
    assert calculate_total(data) == 100000
    # Test danh sách rỗng
    assert calculate_total([]) == 0.0


def test_filter_by_category():
    """Kiểm tra lọc danh mục không phân biệt hoa thường."""
    data = [
        {"category": "Ăn uống", "amount": 20000, "description": ""},
        {"category": "Học tập", "amount": 50000, "description": ""},
        {"category": "ăn uống", "amount": 30000, "description": ""},
    ]
    result = filter_by_category(data, "ĂN UỐNG")
    assert len(result) == 2


def test_get_highest_expense():
    """Kiểm tra tìm khoản chi tiêu lớn nhất."""
    data = [
        {"category": "Ăn uống", "amount": 20000, "description": ""},
        {"category": "Học tập", "amount": 90000, "description": ""},
        {"category": "Di chuyển", "amount": 40000, "description": ""},
    ]
    highest = get_highest_expense(data)
    assert highest is not None
    assert highest["amount"] == 90000

    # Test danh sách rỗng
    assert get_highest_expense([]) is None


if __name__ == "__main__":
    test_add_valid_expense()
    test_add_invalid_amount_rejected()
    test_add_empty_category_rejected()
    test_calculate_total()
    test_filter_by_category()
    test_get_highest_expense()
    print(" Tất cả 6 test cases đều PASS!")
