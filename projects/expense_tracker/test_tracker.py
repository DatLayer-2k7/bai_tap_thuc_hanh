"""Unit tests for the Personal Expense Tracker."""
import json
from pathlib import Path

import pytest

from tracker import add_expense, calculate_total, filter_by_category, get_highest_expense, load_expenses, save_expenses


def test_add_valid_expense() -> None:
    expenses = []
    assert add_expense(expenses, " Ăn uống ", 50000, " Bún bò ") is True
    assert expenses == [{"category": "Ăn uống", "amount": 50000.0, "description": "Bún bò"}]


@pytest.mark.parametrize("amount", [0, -1, float("nan"), float("inf"), "abc", None, True])
def test_reject_invalid_amount(amount) -> None:
    expenses = []
    assert add_expense(expenses, "Ăn uống", amount) is False
    assert expenses == []


@pytest.mark.parametrize("category", ["", "   ", None])
def test_reject_invalid_category(category) -> None:
    expenses = []
    assert add_expense(expenses, category, 10000) is False
    assert expenses == []


def test_calculate_total_and_empty_list() -> None:
    data = [{"category": "Ăn uống", "amount": 30000}, {"category": "Học tập", "amount": 70000}]
    assert calculate_total(data) == 100000
    assert calculate_total([]) == 0


def test_filter_category_ignores_case_and_spaces() -> None:
    data = [{"category": "Ăn uống", "amount": 20000}, {"category": "Học tập", "amount": 50000}, {"category": "ăn uống", "amount": 30000}]
    assert len(filter_by_category(data, " ĂN UỐNG ")) == 2
    assert filter_by_category(data, "  ") == []


def test_get_highest_expense_and_empty_list() -> None:
    data = [{"category": "Ăn uống", "amount": 20000}, {"category": "Học tập", "amount": 90000}]
    assert get_highest_expense(data)["amount"] == 90000
    assert get_highest_expense([]) is None


def test_save_and_load_round_trip(tmp_path: Path) -> None:
    data = [{"category": "Học tập", "amount": 120000, "description": "Sách"}]
    destination = tmp_path / "nested" / "expenses.json"
    save_expenses(data, destination)
    assert load_expenses(destination) == data


def test_missing_file_returns_empty_list(tmp_path: Path) -> None:
    assert load_expenses(tmp_path / "missing.json") == []


def test_malformed_json_raises_value_error(tmp_path: Path) -> None:
    destination = tmp_path / "broken.json"
    destination.write_text("{not json", encoding="utf-8")
    with pytest.raises(ValueError, match="Invalid JSON"):
        load_expenses(destination)


def test_invalid_json_shape_is_rejected(tmp_path: Path) -> None:
    destination = tmp_path / "wrong-shape.json"
    destination.write_text(json.dumps({"category": "food"}), encoding="utf-8")
    with pytest.raises(ValueError, match="JSON list"):
        load_expenses(destination)
