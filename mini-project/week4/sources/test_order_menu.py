import pytest
from unittest.mock import patch, mock_open, MagicMock
import builtins
import order_menu

@pytest.fixture
def mock_orders():
    return {
        "order_1": {
            "customer_name": "Alice",
            "address": "123 Main St",
            "phone": "1234567890",
            "status": "pending"
        }
    }

# --------------------------
# Test load_orders and save_orders
# --------------------------

@patch("order_menu.load_csv")
def test_load_orders(mock_load_csv):
    mock_load_csv.return_value = [
        {
            "order_id": "order_1",
            "customer_name": "Alice",
            "address": "123 Main St",
            "phone": "1234567890",
            "status": "pending"
        }
    ]
    orders = order_menu.load_orders()
    assert orders["order_1"]["customer_name"] == "Alice"

@patch("order_menu.save_csv")
def test_save_orders(mock_save_csv, mock_orders):
    order_menu.save_orders(mock_orders)
    mock_save_csv.assert_called_once()

# --------------------------
# Test create_new_order
# --------------------------

@patch("order_menu.save_orders")
@patch("builtins.input", side_effect=["Bob", "456 Elm St", "0987654321", "confirmed"])
def test_create_new_order(mock_input, mock_save_orders, mock_orders):
    order_menu.create_new_order(mock_orders)
    assert "order_2" in mock_orders
    assert mock_orders["order_2"]["customer_name"] == "Bob"

# --------------------------
# Test update_order_status
# --------------------------

@patch("order_menu.save_orders")
@patch("builtins.input", side_effect=["order_1", "shipped"])
def test_update_order_status(mock_input, mock_save_orders, mock_orders, capsys):
    order_menu.update_order_status(mock_orders)
    captured = capsys.readouterr()
    assert "✅ Status updated successfully for order_1" in captured.out
    assert mock_orders["order_1"]["status"] == "shipped"

# --------------------------
# Test update_existing_order
# --------------------------

@patch("order_menu.save_orders")
@patch("builtins.input", side_effect=["order_1", "customer_name", "Charlie"])
def test_update_existing_order(mock_input, mock_save_orders, mock_orders):
    order_menu.update_existing_order(mock_orders)
    assert mock_orders["order_1"]["customer_name"] == "Charlie"

# --------------------------
# Test delete_order
# --------------------------

@patch("order_menu.save_orders")
@patch("builtins.input", side_effect=["order_1", "yes"])
def test_delete_order(mock_input, mock_save_orders, mock_orders):
    order_menu.delete_order(mock_orders)
    assert "order_1" not in mock_orders

# --------------------------
# Test display_order
# --------------------------

def test_display_order(capsys, mock_orders):
    order_menu.display_order("order_1", mock_orders["order_1"])
    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "123 Main St" in captured.out
