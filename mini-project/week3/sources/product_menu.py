# Importing required modules
import os

# Define the file path for the TXT file relative to the current script location
file_name = os.path.join(os.path.dirname(__file__), "..", "data", "products.txt")

# Function to create the file if it does not exist
def create_file_if_not_exists():
    if not os.path.exists(file_name):
        with open(file_name, mode="w") as file:
            file.write("product,price\n")  # Write header line

# Function to load products from the TXT file into a list of dictionaries
def load_products():
    create_file_if_not_exists()
    products = []
    with open(file_name, mode="r") as file:
        next(file)  # Skip header
        for line in file:
            line = line.strip()
            if line:  # skip empty lines
                product, price = line.split(",", 1)
                products.append({"product": product, "price": float(price)})
    return products

# Function to save a list of product dictionaries to the TXT file
def save_products(products):
    with open(file_name, mode="w") as file:
        file.write("product,price\n")  # Write header
        for product in products:
            file.write(f"{product['product']},{product['price']}\n")

# Function to display all products in a formatted table
def view_products(products):
    if not products:
        print("No products found.")
        return
    print("\nList of products : ")
    print("\n{:<5}{:<20} {:<15}".format("ID", "Product", "Price"))
    print("-" * 45)
    for i, prod in enumerate(products):
        print("{:<5} {:<20} {:<15}".format(i, prod['product'], prod['price']))
    print("-" * 45)

# Function to add a new product to the list and save to file
def add_product(products, product, price):
    if not product or not price:
        print("Product and price cannot be empty")
        return
    products.append({"product": product, "price": float(price)})
    save_products(products)
    print(f"{product} added and saved.")

# Function to update an existing product by index
def update_product(products):
    view_products(products)
    try:
        idx = int(input('Enter product index you want to update: '))
        if 0 <= idx < len(products):
            new_name = input('Enter new product name: ')
            new_price = float(input('Enter new product price: '))
            if new_name:
                products[idx]["product"] = new_name
            if new_price:
                products[idx]["price"] = new_price
            save_products(products)
            print("Product updated and saved.")
        else:
            print("Invalid index.")
    except ValueError:
        print('Invalid input. Please try again.')

# Function to delete a product from the list
def delete_product(products):
    view_products(products)
    try:
        idx = int(input('Enter product index you want to delete: '))
        if 0 <= idx < len(products):
            removed = products.pop(idx)
            save_products(products)
            print(f"Deleted product: {removed['product']} (£{removed['price']:.2f}) changes saved.")
        else:
            print("Invalid index.")
    except ValueError:
        print('Invalid index.')

# Function to print the menu options for the product menu
def print_product_menu():
    print("\nProduct Menu options\n")
    print("Options:\n"
          "0: Return to main menu\n"
          "1: Print Product List\n"
          "2: Add New Product\n"
          "3: Update Product\n"
          "4: Delete Product")

# Function to run the main product menu loop
def product_menu():
    products = load_products()
    while True:
        print_product_menu()
        product_menu_input = input('Enter product menu option: ')
        if product_menu_input == '0':
            print('Exiting the product menu...')
            save_products(products)
            break
        elif product_menu_input == '1':
            view_products(products)
        elif product_menu_input == '2':
            product = input('Enter new product name you would like to add: ')
            try:
                price = float(input('Enter product price: '))
                add_product(products, product, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif product_menu_input == '3':
            update_product(products)
        elif product_menu_input == '4':
            delete_product(products)
        else:
            print("Invalid choice, try again.")



