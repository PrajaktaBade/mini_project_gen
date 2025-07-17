from db import get_connection

def load_products():
    products = {}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT product_id, product, price FROM products ORDER BY product_id")
                for pid, name, price in cur.fetchall():
                    products[str(pid)] = {"product": name, "price": float(price)}
    except Exception as e:
        print(f"Error loading products: {e}")
    return products

def view_products(products):
    if not products:
        print("📦 No products found.")
        return
    print("\n 📋 List of products : ")
    print("\n{:<10} {:<35} {:>10}".format("🆔 ID", "📦 Product", "💰Price (£)"))
    print("-" * 60)
    for pid, data in products.items():
        print("{:<10} {:<35} {:>10}".format(pid, data['product'], f"£{data['price']:.2f}"))
    print("-" * 60)

def add_product(products, product, price):
    if not product or not price:
        print("⚠️ Product and price cannot be empty")
        return
    try:
        price = float(price)
        if price < 0:
            print("⚠️ Price cannot be negative.")
            return
    except ValueError:
        print("⚠️Invalid price.Must be a number.")
        return
    
    if any(p['product'].lower() == product.lower() for p in products.values()):
        print("⚠️ Product with this name already exists.")
        return
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO products (product, price) VALUES (%s, %s) RETURNING product_id",
                    (product, price)
                )
                new_id = cur.fetchone()[0]
                conn.commit()
                products[str(new_id)] = {"product": product, "price": price}
                print(f"✅ {product} added with ID {new_id} and saved.")
    except Exception as e:
        print(f"🚫 Error adding product: {e}")

def update_product(products):
    view_products(products)
    pid = input("✏️ Enter product ID to update: ").strip()
    if pid not in products:
        print("❌ Invalid product ID.")
        return

    new_name = input("📝 Enter new product name(or leave blank to keep current): ").strip()
    new_price_str = input("💵 Enter new product price(or leave blank to keep current): ").strip()

    if not new_name and not new_price_str:
        print("⚠️ No updates entered.")
        return

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if new_name:
                    cur.execute("UPDATE products SET product = %s WHERE product_id = %s", (new_name, pid))
                    products[pid]["product"] = new_name
                if new_price_str:
                    try:
                        new_price = float(new_price_str)
                        cur.execute("UPDATE products SET price = %s WHERE product_id = %s", (new_price, pid))
                        products[pid]["price"] = new_price
                    except ValueError:
                        print("⚠️ Invalid price input.")
                conn.commit()
                print("✅ Product updated and saved.")
    except Exception as e:
        print(f"🚫 Failed to update product: {e}")

def delete_product(products):
    view_products(products)
    pid = input("🗑️ Enter product ID to delete: ").strip()
    if pid not in products:
        print("⚠️ Invalid product ID")
        return
    confirm = input(f"⚠️ Are you sure you want to delete '{products[pid]['product']}'?(y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Delete cancelled.")
        return
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM products WHERE product_id = %s", (pid,))
                conn.commit()
                removed = products.pop(pid)
                print(f"🗑️ Deleted product: {removed['product']} (£{removed['price']:.2f})")
    except Exception as e:
        print(f"🚫 Failed to delete product: {e}")
    

def print_product_menu():
    print("🛍️ Product Menu Options\n")
    print("Options:\n"
          "0️⃣: Return to main menu\n"
          "1️⃣: 📋 Print Product List\n"
          "2️⃣: ➕ Add New Product\n"
          "3️⃣: ✏️ Update Product\n"
          "4️⃣: 🗑️ Delete Product")

def product_menu():
    products = load_products()

    while True:
        print_product_menu()
        try:
            option = input("Enter product menu option: ").strip()

            if option == '0':
                print("🔙 Returning to main menu...")
                break
            elif option == '1':
                view_products(products)
                input("🔄 Press 'Enter' to continue...")
            elif option == '2':
                name = input("🆕 Enter product name: ").strip()
                price = input("💵 Enter product price: ").strip()
                add_product(products, name, price)
                input("🔄 Press 'Enter' to continue...")
            elif option == '3':
                update_product(products)
                input("🔄 Press 'Enter' to continue...")
            elif option == '4':
                delete_product(products)
                input("🔄 Press 'Enter' to continue...")
            else:
                print("⚠️ Invalid choice. Try again.")
            
        except Exception as e: 
                print(f"🚫 Unexpected error: {e}")

        
