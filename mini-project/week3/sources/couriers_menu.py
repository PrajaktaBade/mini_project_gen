import os

# Define the file path for the couriers.txt file relative to the script
file_name = os.path.join(os.path.dirname(__file__), "..", "data", "couriers.txt")

# Create the file if it does not exist
def create_file_if_not_exists():
    if not os.path.exists(file_name):
        # Make sure the directory exists
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, mode="w") as file:
            pass  # Just create an empty file

# Load couriers from the text file
def load_couriers():
    create_file_if_not_exists()
    couriers = []
    with open(file_name, mode="r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Expecting lines like: name | phone
            name, phone = line.split(" | ")
            couriers.append({"name": name, "phone": phone})
    return couriers

# Save couriers to the text file
def save_couriers(couriers):
    with open(file_name, mode="w") as file:
        for courier in couriers:
            line = f"{courier['name']} | {courier['phone']}\n"
            file.write(line)

# Display all couriers
def view_couriers(couriers):
    if not couriers:
        print("No couriers found.")
        return
    print("\nCouriers:")
    print("{:<5}{:<20} {:<15}".format("ID", "Courier Name", "Phone Number"))
    print("-" * 45)
    for i, courier in enumerate(couriers):
        print("{:<5} {:<20} {:<15}".format(i, courier['name'], courier['phone']))
    print("-" * 45)

# Add new courier
def add_courier(couriers, name, phone):
    if not name or not phone:
        print("Name and phone cannot be empty.")
        return
    couriers.append({"name": name, "phone": phone})
    save_couriers(couriers)
    print(f"Added courier: {name}, {phone}")

# Update courier
def update_courier(couriers, index, new_name, new_phone):
    if 0 <= index < len(couriers):
        if new_name:
            couriers[index]["name"] = new_name
        if new_phone:
            couriers[index]["phone"] = new_phone
        save_couriers(couriers)
        print("Courier updated.")
    else:
        print("Invalid index.")

# Delete courier
def delete_courier(couriers, index):
    if 0 <= index < len(couriers):
        removed = couriers.pop(index)
        save_couriers(couriers)
        print(f"Deleted courier: {removed['name']}")
    else:
        print("Invalid index.")

# Courier menu options
def print_courier_menu():
    print("\nCouriers Menu:\n")
    print("0 : Return to main menu\n"
          "1 : View Couriers\n"
          "2 : Add New Courier\n"
          "3 : Update Courier\n"
          "4 : Delete Courier")

# Main courier menu loop
def couriers_menu():
    couriers = load_couriers()

    while True:
        print_courier_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '0':
            save_couriers(couriers)
            print("Exiting courier menu...")
            break

        elif choice == '1':
            view_couriers(couriers)

        elif choice == '2':
            name = input("Enter courier name: ").strip()
            phone = input("Enter courier phone: ").strip()
            add_courier(couriers, name, phone)

        elif choice == '3':
            view_couriers(couriers)
            try:
                index = int(input("Enter index of courier to update: "))
                new_name = input("Enter new name (or press enter to skip): ").strip()
                new_phone = input("Enter new phone (or press enter to skip): ").strip()
                update_courier(couriers, index, new_name, new_phone)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            view_couriers(couriers)
            try:
                index = int(input("Enter index of courier to delete: "))
                delete_courier(couriers, index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        else:
            print("Invalid choice. Please try again.")







