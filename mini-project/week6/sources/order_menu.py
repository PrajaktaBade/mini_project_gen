from db import get_connection
from courier_menu import load_couriers
from product_menu import load_products
from collections import defaultdict

def load_orders():
    try:
        orders = []
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT order_id, customer_name, customer_address, customer_phone, courier_id, status, items
                    FROM orders ORDER BY order_id
                """)
                for row in cur.fetchall():
                    orders.append({
                        "order_id": row[0],
                        "customer_name": row[1],
                        "customer_address": row[2],
                        "customer_phone": row[3],
                        "courier_index": str(row[4]),
                        "status": row[5],
                        "product_ids": row[6]  # string like "1,2,3"
                    })
        return orders
    except Exception as e:
        print(f"🚫Error loading orders: {e}")
        return[]


def get_products_by_order(order_id, conn):
    try:
        with conn.cursor() as cursor:
            # Get the comma-separated product IDs string from the order
            cursor.execute("SELECT items FROM orders WHERE order_id = %s", (order_id,))
            result = cursor.fetchone()
            if not result:
                return []

            item_ids_str = result[0]  # e.g., "1,3,4"

            # Convert string to list of integers
            item_ids = [int(pid) for pid in item_ids_str.split(',') if pid.strip().isdigit()]
            if not item_ids:
                return []

            # Now query products table using WHERE id IN (%s, %s, ...)
            query = f"SELECT product FROM products WHERE product_id = ANY(%s)"
            cursor.execute(query, (item_ids,))
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"🚫 Error retrieving products for order {order_id}: {e}")

def get_orders_grouped_by_status(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT order_id, customer_name, customer_address, customer_phone, courier_id, status
                FROM orders
            """)
            rows = cursor.fetchall()

            # Create a dictionary to group orders by status
            orders_by_status = {}

            for row in rows:
                order_id, name, address, phone, courier_id, status = row
                products = get_products_by_order(order_id, conn)

                order_dict = {
                    'order_id': order_id,
                    'customer_name': name,
                    'customer_address': address,
                    'customer_phone': phone,
                    'courier_id': courier_id,
                    'products': products
                }

                orders_by_status.setdefault(status, []).append(order_dict)
            return orders_by_status
    except Exception as e:
        print("🚫 Error grouping orders: {e}")
        return {}

def view_orders(conn):
    try:
        orders_by_status = get_orders_grouped_by_status(conn)
        print("📦 Orders Grouped by Status")
        print("=" * 80)
    
        for status, orders in orders_by_status.items():
            print(f"\n📌 Status: {status.upper()}")
            print("-" * 80)
            for order in orders:
                print(f"Order ID : {order['order_id']}")
                print(f"Customer : {order['customer_name']}")
                print(f"Address  : {order['customer_address']}")
                print(f"Phone    : {order['customer_phone']}")
                print(f"Courier  : {order['courier_id']}")
                print(f"Products : {', '.join(order['products'])}")
                print("-" * 80)
            print("=" * 80)
    except Exception as e:
        print(f"🚫 Error viewing orders:{e}")


def add_order(name, address, phone, courier_id, product_ids):
    if not (name and address and phone):
        print("⚠️ Name, address, and phone cannot be empty.")
        return

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, status, items)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (name, address, phone, courier_id, 'preparing', ','.join(map(str, product_ids))))
                conn.commit()
                print(f"✅ Order added for {name}.")
    except ValueError:
        print("🚫 Courier ID must be a number.")
    except Exception as e:
        print(f"🚫 Failed to add order: {e}")

def update_order_status(order_id, new_status):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE orders SET status = %s WHERE order_id = %s
                """, (new_status, order_id))
                conn.commit()
                print("✏️ Order status updated.")
    except ValueError:
        print("🚫 Order ID must be a number.")
    except Exception as e:
        print(f"🚫 Failed to update order: {e}")

def delete_order(order_id):
    try:
        confirm = input(f"⚠️ Are you sure you want to delete order #{order_id} (y/n)? ").strip().lower()
        if confirm != 'y':
            print("🚫 Deletion cancelled.")
            return
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
                conn.commit()
                print(f"🗑️ Order #{order_id} deleted.")
    except ValueError:
        print("🚫 Order ID must be a number.")
    except Exception as e:
        print(f"🚫 Failed to delete order: {e}")




def print_order_menu():
    print("\n🛍️ Orders Menu Options\n")
    print("0️⃣ : Return to main menu\n" 
          "1️⃣ : 📋 View Orders\n"
          "2️⃣ : ➕ Add New Order\n"
          "3️⃣ : 🔄 Update Order Status\n"
          "4️⃣ : 🗑️ Delete Order")

def order_menu():
    try:
        products = load_products()
    except Exception as e:
        print(f"🚫 Failed to load products: {e}")
        products = []

    while True:
        print_order_menu()
        choice = input("📲 Enter your choice: ").strip()

        if choice == '0':
            print("🔙 Returning to main menu...")
            break

        elif choice == '1':
            try:
                with get_connection() as conn:
                    view_orders(conn)
            except Exception as e:
                print(f"🚫 Could not view orders: {e}")
            input("🔄 Press 'Enter' to continue...")

        elif choice == '2':
            try:
                name = input("👤 Enter customer name: ").strip()
                address = input("🏠 Enter customer address: ").strip()
                phone = input("📞 Enter customer phone: ").strip()
                courier_id = input("🚚 Enter courier ID: ").strip()
                product_id = input("📦 Enter product IDs (comma-separated): ").strip()
                product_list = [pid.strip() for pid in product_id.split(',') if pid.strip().isdigit()]
                if not product_list:
                    print("⚠️ No valid product IDs provided.")
                else:
                    add_order(name, address, phone, courier_id, product_list)
            except Exception as e:
                print(f"🚫 Failed to add new order: {e}")
            input("🔄 Press 'Enter' to continue...")

        elif choice == '3':
            try:
                with get_connection() as conn:
                    view_orders(conn)
                order_id = input("🔁 Enter order ID to update status: ").strip()
                new_status = input("📦 Enter new status (preparing/dispatched/delivered): ").strip()
                update_order_status(order_id, new_status)
            except Exception as e:
                print(f"🚫 Failed to update status: {e}")
            input("🔄 Press 'Enter' to continue...")

        elif choice == '4':
            try:
                with get_connection() as conn:
                    view_orders(conn)
                order_id = input("🗑️ Enter order ID to delete: ").strip()
                delete_order(order_id)
            except Exception as e:
                print(f"🚫 Failed to delete order: {e}")
            input("🔄 Press 'Enter' to continue...")

        else:
            print("⚠️ Invalid option.")
            input("🔄 Press 'Enter' to continue...")