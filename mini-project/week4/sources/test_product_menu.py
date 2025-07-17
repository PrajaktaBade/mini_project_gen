#import os
import csv
import pytest
from product_menu import add_product,update_product,delete_product,generate_new_product_id


@pytest.fixture
def temp_file(tmp_path):
    """Creates a temporary CSV file for testing"""
    file_path = tmp_path / "test_products.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product_id", "product", "price"])
        writer.writeheader()
        writer.writerow({"product_id": "1", "product": "Apple", "price": "0.99"})
        writer.writerow({"product_id": "2", "product": "Banana", "price": "0.49"})
    return file_path


def test_load_products(tmp_path):
    file_path = tmp_path / "test_products.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product_id", "product", "price"])
        writer.writeheader()
        writer.writerow({"product_id": "1", "product": "Milk", "price": "1.50"})

    from utils import load_csv
    products = load_csv(str(file_path), ["product_id", "product", "price"])
    assert products[0]["product"] == "Milk"
    assert float(products[0]["price"]) == 1.50


def test_save_and_load_products(tmp_path):
    # Save
    test_file = tmp_path / "products.csv"
    products = {
        "1": {"product": "Water", "price": 0.89},
        "2": {"product": "Juice", "price": 1.99}
    }
    from utils import save_csv, load_csv
    save_csv(str(test_file), ["product_id", "product", "price"], [
        {"product_id": pid, "product": data["product"], "price": data["price"]}
        for pid, data in products.items()
    ])
    loaded = load_csv(str(test_file), ["product_id", "product", "price"])
    assert len(loaded) == 2
    assert loaded[0]["product"] == "Water"


def test_generate_new_product_id():
    products = {"1": {"product": "A", "price": 1}, "2": {"product": "B", "price": 2}}
    new_id = generate_new_product_id(products)
    assert new_id == "3"


def test_add_product(monkeypatch):
    products = {}
    monkeypatch.setattr("builtins.input", lambda _: "Test Product")
    add_product(products, "Test Product", "2.5")
    assert "1" in products
    assert products["1"]["product"] == "Test Product"
    assert products["1"]["price"] == 2.5


def test_update_product(monkeypatch):
    products = {"1": {"product": "Old", "price": 1.0}}
    inputs = iter(["1", "New", "2.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    update_product(products)
    assert products["1"]["product"] == "New"
    assert products["1"]["price"] == 2.0


def test_delete_product(monkeypatch):
    products = {"1": {"product": "DeleteMe", "price": 3.0}}
    monkeypatch.setattr("builtins.input", lambda _: "1")
    delete_product(products)
    assert "1" not in products
