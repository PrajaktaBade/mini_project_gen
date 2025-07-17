import pytest
from unittest.mock import patch, mock_open
from couriers_menu import (
    is_valid_phone,
    add_courier,
    update_courier,
    delete_courier,
    view_couriers
)

# Sample courier list
@pytest.fixture
def sample_couriers():
    return [
        {"name": "John Doe", "phone": "07123456789"},
        {"name": "Jane Smith", "phone": "07987654321"}
    ]


# -------------------------
# Test is_valid_phone
# -------------------------

@pytest.mark.parametrize("phone,expected", [
    ("07123456789", True),
    ("07123-456-789", True),
    ("07123", False),
    ("abcdefghijk", False),
    ("071234567890", False),
    ("0712345abcd", False),
])
def test_is_valid_phone(phone, expected):
    assert is_valid_phone(phone) == expected


# -------------------------
# Test add_courier
# -------------------------

def test_add_valid_courier(monkeypatch, sample_couriers):
    monkeypatch.setattr("couriers_menu.save_couriers", lambda x: None)

    with patch("builtins.print") as mock_print:
        add_courier(sample_couriers, "Alice", "07000000000")

    assert sample_couriers[-1] == {"name": "Alice", "phone": "07000000000"}
    mock_print.assert_any_call("✅ Added courier: Alice,📞07000000000")


def test_add_courier_duplicate_name(sample_couriers, monkeypatch):
    monkeypatch.setattr("couriers_menu.save_couriers", lambda x: None)

    with patch("builtins.print") as mock_print:
        add_courier(sample_couriers, "John Doe", "07111111111")

    mock_print.assert_any_call("⚠️ A courier with the same name already exists.")


def test_add_courier_invalid_phone(sample_couriers):
    with patch("builtins.print") as mock_print:
        add_courier(sample_couriers, "New Courier", "07abc")

    mock_print.assert_any_call(
        "❌ Invalid phone number.Please enter a valid number (11 digits including 0 at starting,digits only)."
    )


# -------------------------
# Test update_courier
# -------------------------

def test_update_courier_name(sample_couriers, monkeypatch):
    monkeypatch.setattr("couriers_menu.save_couriers", lambda x: None)

    with patch("builtins.print") as mock_print:
        update_courier(sample_couriers, 0, "Johnny", "")

    assert sample_couriers[0]["name"] == "Johnny"
    mock_print.assert_any_call("✏️Courier updated.")


def test_update_courier_duplicate_phone(sample_couriers):
    with patch("builtins.print") as mock_print:
        update_courier(sample_couriers, 0, "", "07987654321")

    mock_print.assert_any_call("⚠️ A courier with the same phone number already exists.")


# -------------------------
# Test delete_courier
# -------------------------

def test_delete_valid_courier(monkeypatch, sample_couriers):
    monkeypatch.setattr("couriers_menu.save_couriers", lambda x: None)

    with patch("builtins.input", return_value='y'):
        with patch("builtins.print") as mock_print:
            delete_courier(sample_couriers, 0)

    assert len(sample_couriers) == 1
    assert sample_couriers[0]["name"] == "Jane Smith"
    mock_print.assert_any_call("🗑️ Deleted courier: John Doe")


def test_delete_courier_cancel(monkeypatch, sample_couriers):
    monkeypatch.setattr("couriers_menu.save_couriers", lambda x: None)

    with patch("builtins.input", return_value='n'):
        with patch("builtins.print") as mock_print:
            delete_courier(sample_couriers, 0)

    assert len(sample_couriers) == 2
    mock_print.assert_any_call("🚫 Deletion cancelled.")


# -------------------------
# Test view_couriers
# -------------------------

def test_view_couriers_with_data(sample_couriers):
    with patch("builtins.print") as mock_print:
        view_couriers(sample_couriers)

    mock_print.assert_any_call("\nCouriers : ")


def test_view_couriers_empty():
    with patch("builtins.print") as mock_print:
        view_couriers([])

    mock_print.assert_any_call("❌ No couriers found.")
