import os

# Define the file path for the orders.txt file relative to the script
file_name = os.path.join(os.path.dirname(__file__), "..","data", "orders.txt")

# Create the file if it does not exist
def create_file_if_not_exists():
    if not os.path.exists(file_name):
        with open(file_name, mode="w") as file:
            pass  # Just create an empty file

# Load orders from the text file
def load_orders():
    create_file_if_not_exists()
    orders = {}
    with open(file_name, mode="r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            order_id, name, address, phone, status = line.split(" | ")
            orders[order_id] = {
                "customer_name": name,
                "address": address,
                "phone": phone,
                "status": status
            }
    return orders

# Save orders to the text file
def save_orders(orders):
    with open(file_name, mode="w") as file:
        for order_id, order in orders.items():
            line = f"{order_id} | {order['customer_name']} | {order['address']} | {order['phone']} | {order['status']}\n"
            file.write(line)

# Print menu
def print_order_menu():
    print("Orders menu list:\n")
    print("0 : Return to main menu\n"
          "1 : Print Orders\n"
          "2 : Create new order\n"
          "3 : Update order status\n"
          "4 : Update Existing order\n"
          "5 : Delete order")

# Display single order
def display_order(order_id, order):
    print(f"\nOrder ID   : {order_id}")
    print(f"Name       : {order['customer_name']}")
    print(f"Address    : {order['address']}")
    print(f"Phone      : {order['phone']}")
    print(f"Status     : {order['status']}")

# Order menu loop
def order_menu():
    orders = load_orders()

    while True:
        print_order_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '0':
            save_orders(orders)
            print("Exiting order menu...")
            break

        elif choice == '1':
            if not orders:
                print("No orders found.")
            else:
                for order_id, order in sorted(orders.items()):
                    display_order(order_id, order)

        elif choice == '2':
            print("Enter order details:")
            customer_name = input("Name: ").strip()
            address = input("Address: ").strip()
            phone = input("Phone: ").strip()
            status = input("Status: ").strip()
            new_order_id = f"order_{len(orders)+1}"
            orders[new_order_id] = {
                "customer_name": customer_name,
                "address": address,
                "phone": phone,
                "status": status
            }
            save_orders(orders)
            print(f"Order '{new_order_id}' added successfully.")

        elif choice == '3':
            if not orders:
                print("No orders to update.")
                continue
            for oid in orders:
                print(f"{oid} - {orders[oid]['customer_name']}")
            order_id = input("Enter Order ID: ").strip()
            if order_id in orders:
                print(f"Current status: {orders[order_id]['status']}")
                new_status = input("Enter new status: ").strip()
                orders[order_id]['status'] = new_status
                save_orders(orders)
                print("Status updated successfully.")
            else:
                print("Order ID not found.")

        elif choice == '4':
            order_id = input("Enter Order ID: ").strip()
            if order_id in orders:
                print("Fields: customer_name, address, phone, status")
                field = input("Enter field to update: ").strip()
                if field in orders[order_id]:
                    new_value = input(f"Enter new value for {field}: ").strip()
                    orders[order_id][field] = new_value
                    save_orders(orders)
                    print(f"{field} updated successfully.")
                else:
                    print("Invalid field.")
            else:
                print("Order ID not found.")

        elif choice == '5':
            order_id = input("Enter Order ID to delete: ").strip()
            if order_id in orders:
                confirm = input("Are you sure you want to delete this order? (yes/no): ").lower()
                if confirm == "yes":
                    del orders[order_id]
                    save_orders(orders)
                    print("Order deleted successfully.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Order ID not found.")

        else:
            print("Invalid option. Please try again.")





