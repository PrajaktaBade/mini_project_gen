# Import required modules
import csv
import os
# Custom utility functions for CSV operations
from utils import load_csv,save_csv

# Set up the base directory and data folder
base_dir = os.path.dirname(os.path.dirname(__file__))                                 #Get parent of current script's
data_folder = os.path.join(base_dir,"data")                                           #Create path to 'data' directory
os.makedirs(data_folder, exist_ok =True)                                              # Create 'data folder if it doesn't exist

#Define file name and column headres for product data
file_name = os.path.join(data_folder,"products.csv")
fieldnames = ["product_id","product","price"]

# Load product data from CSV into a dictionary
def load_products():
    rows = load_csv(file_name,fieldnames)                                             # Load rows using helper function
    products ={}
    for row in rows:
        products[row['product_id']] = {
            "product" : row["product"],
            "price" : float(row["price"])                                              # Convert price from string to float
        }
    return products

# Save the products dictionary to a CSV file
def save_products(products):
    rows = []
    for pid,data in products.items():
        rows.append({
            "product_id" : pid,
            "product" : data["product"],
            "price" : str(data["price"])
        })
    save_csv(file_name,fieldnames,rows)
    return products

# Display all products in a tabular format
def view_products(products):
    if not products:
        print("📦 No products found.")
        return
    print("\n 📋 List of products : ")
    print("\n{:<10} {:<35} {:>10}".format("🆔 ID"," 📦Product","💰Price (£)"))
    print("-" * 60)
    for pid,data in products.items():
        print("{:<10} {:<35} {:>10}".format(pid, data['product'], f"£{data['price']:.2f}"))
    print("-"* 60)

# Generate a new product ID by incrementing the highest existing ID
def generate_new_product_id(products):
    try:
        if not products:
            return "1"
        max_id = max(int(pid) for pid in products.keys())
        return str(max_id + 1)
    except Exception:
        return "1"

# Add a new product to the products dictionary and save it
def add_product(products,product,price):
    if not product or not price:
        print("⚠️ Product and price can not be empty")
        return
    try:
        price = float(price)
        new_id = generate_new_product_id(products)
        products[new_id] = {"product" :product, "price":price}
        save_products(products)
        print(f"✅ {product} added with ID {new_id} and saved.")
    except ValueError:
        print("❌ Price must be a valid number.")
    except Exception as e:
        print(f"🚫 Error adding product: {e}")
        
# Update product name or price by product ID        
def update_product(products):
    view_products(products)
    pid = input("✏️Enter product ID to update: ").strip()
    if pid not in products:
        print("❌ Invalid product ID.")
        return
    
    new_name = input('📝 Enter new product :').strip()
    new_price_str = input('💵 Enter new product price: ')
                
    if new_name:
        products[pid]["product"] = new_name
    if new_price_str:
        try:
            new_price = float(new_price_str)
            products[pid]["price"] = new_price
        except ValueError:
            print("⚠️ Invalid price input.Price not updated")
    
    try:
        save_products(products)
        print("✅ Product updated and saved.")
    except Exception as e:
        print(f"🚫 Failed to save updated product: {e}")

# Delete a product bu its ID 
def delete_product(products):
    view_products(products)
    pid = input('🗑️ Enter product index you want update: ')
    
    if pid in products:
        removed =products.pop(pid)
        try:
            save_products(products)
            print(f"🗑️ Deleted product: {removed['product']} (£{removed['price']:.2f})")
        except Exception as e:
            print(f"🚫Failed to save deletion: {e}")
    else:
        print("⚠️ Invalid product ID")    

# Print available product menu options        
def print_product_menu():
    print("🛍️ Product Menu options\n")
    print("Options: \n" 
          "0️⃣: Return to main menu \n" 
          "1️⃣: 📋 Print Product List\n"
          "2️⃣: ➕ Add New Product\n"
          "3️⃣: ✏️Update product\n"
          "4️⃣: 🗑️ Delete Product")

# Main loop for product management
def product_menu():
    products = load_products()                                                         

    while True:
        print_product_menu()
        product_menu_input = input('Enter product menu option: ').strip()

        if product_menu_input == '0':
            print('🔙 Out of the product menu..')
            save_products(products)
            break
           
        elif product_menu_input == '1':
            view_products(products)
            input("🔄 Press 'Enter' to continue...")
   
        elif product_menu_input == '2':
            name = input('🆕 Enter new product name you would like to add:').strip()
            price = input('💵 Enter product price: ').strip()
            add_product(products,name,price)
            input("🔄 Press 'Enter' to continue...")
            
        elif product_menu_input == '3':
            update_product(products)
            input("🔄 Press 'Enter' to continue...")
   
        elif product_menu_input == '4':
            delete_product(products)
            input("🔄 Press 'Enter' to continue...")

        else:
            print("⚠️ Invalid choice,try again")
            input("🔄 Press 'Enter' to continue...")