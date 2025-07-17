import csv
import os
from utils import load_csv,save_csv
from couriers_menu import load_couriers
from product_menu import load_products

from collections import defaultdict

base_dir = os.path.dirname(os.path.dirname(__file__))
data_folder = os.path.join(base_dir,"data")
os.makedirs(data_folder, exist_ok =True)

file_name = os.path.join(data_folder,"orders.csv")
fieldnames = ["customer_name","customer_address","customer_phone","courier_index","status","product_indexes"]
products = load_products()
couriers = load_couriers()

def load_orders():
    return load_csv(file_name, fieldnames)

def save_orders(orders):
    save_csv(file_name, fieldnames, orders)

def print_order_menu():
    print("🛍️ Orders menu: \n")
    print("0️⃣ : Return to main menu\n" 
          "1️⃣ : 📋 View Orders\n"
          "2️⃣ : ➕ Add new order\n"
          "3️⃣ : 🔄 Update order status\n"
          "4️⃣ : 🗑️ Delete order")

def view_orders(orders,products):
    if not orders:
        print("❌ No orders found.")
        return

    product_names_map = {str(i): p['name'] for i, p in enumerate(products)}
    grouped = defaultdict(list)
    for i, order in enumerate(orders):
        grouped[order['status']].append((i, order))

    print("\n📦 Orders (Grouped by Status):")
    print("=" * 90)
    for status, group in grouped.items():
        print(f"\n📌 Status: {status}")
        print("-" * 90)
        for index, order in group:
            product_ids = order.get('product_indexes', '').split(',')
            product_names = [product_names_map.get(pid.strip(), f"(Unknown #{pid.strip()})") for pid in product_ids]

            print(f"ID: {index} | Name: {order['customer_name']} | Address: {order['customer_address']} | "
                  f"Phone: {order['customer_phone']} | Courier ID: {order['courier_index']} | "
                  f"Products: {', '.join(product_names)}")
        print("-" * 90)
    
def add_order(orders,name,address,phone,courier_index,product_indexes):
    if not (name and address and phone):
        print("⚠️ Name, address, and phone cannot be empty.")
        return

    orders.append({
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone,
        "courier_index": courier_index,
        "status": "preparing",
        "product_indexes": ','.join(map(str, product_indexes))
    })
    save_orders(orders)
    print(f"✅ Order added for {name}.")

     
def update_order_status(orders,index,new_status):
    if not (0 <= index < len(orders)):
        print("❌ Invalid order index.")
        return
    
    orders[index]['status'] = new_status
    save_orders(orders)
    print("✏️ Order status updated.")

        
def delete_order(orders,index):
    if not (0 <= index < len(orders)):
        print("❌ Invalid index.")
        return
    confirm = input("⚠️ Are you sure you want to delete this order for {order[index][customer_name]}'?(y/n): ")
    if confirm != "y":
        print("🚫 Deletion cancelled.")
        return
    
    removed = orders.pop(index)
    save_orders(orders)
    print(f"🗑️ Deleted order for: {removed['customer_name']}")


def order_menu():
    orders = load_orders()
    
    while True:
        try:
            print_order_menu()
            order_menu_input = input("📲 Enter you choice for order menu:")
            
            if order_menu_input == '0':
                print("🔙 Out of order menu...")
                break
            
            elif order_menu_input == '1':
                view_orders(orders,products)
                input("🔄 Press 'Enter' to continue...")
            
            elif order_menu_input == '2':
                name = input("👤 Enter customer name:")
                address = input("🏠 Enter address:")
                phone = input("📞 Enter phone:")
                courier_index = input("🚚 Enter courier index:")
                product_indexes = input("📦 Enter product indexes (comma-separated):")
                product_indexes_list = [p.strip() for p in product_indexes.split(',') if p.strip().isdigit()]
                add_order(orders,name,address,phone,courier_index,product_indexes_list)
                input("🔄 Press 'Enter' to continue...")
                
            elif order_menu_input == '3':
                view_orders(orders,products)
                try:
                    index = int(input("🆔 Enter order index to update status:"))
                    new_status = input("🔄 Enter new status (preparing/dispatched/delivered): ")
                    update_order_status(orders,index,new_status)
                except ValueError:
                    print("⚠️ Invalid input.")
                input("🔄 Press 'Enter' to continue...")
    
            elif order_menu_input == '4':
                view_orders(orders,products)
                try:
                    index = int(input("🆔 Enter order index to delete: "))
                    delete_order(orders,index)
                except ValueError:
                    print("⚠️ Invalid input.")
                input("🔄 Press 'Enter' to continue...")

            else:
                print("⚠️ Invalid order menu option.")
                input("🔄 Press 'Enter' to continue...")

        except Exception as e:
            print(f"Unexpected error: {e}")
            input("🔄 Press 'Enter to continue...")