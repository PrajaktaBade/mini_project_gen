import psycopg2
from db import get_connection

def is_valid_phone(phone):
    cleaned = phone.replace("+","").replace("-","").replace(" ","")
    return cleaned.isdigit() and len(cleaned) == 11

def load_couriers():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT courier_id, name, phone FROM couriers ORDER BY courier_id")
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"❌ Error loading couriers: {e}")

def view_couriers():
    couriers = load_couriers()
    if not couriers:
        print("❌ No couriers found.")
        return
    print("\nCouriers : ")
    print("{:<5}{:<20}{:<15}".format("ID","Courier Name", "Phone"))
    print("-" * 45)
    for cid,name,phone in couriers:
        print("{:<5}{:<20}{:<15}".format(cid,name,phone))
    print("-" * 45)

def add_courier(name,phone):
    if not name or not phone:
        print("⚠️ Name and phone cannot be empty.")
        return
    if not is_valid_phone(phone):
        print("❌ Invalid phone number.Must be digits only and 11 digits including 0 at start.")
        return
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM couriers WHERE name = %s OR phone = %s",(name,phone))
        existing = cur.fetchall()
        if existing:
            print("⚠️ Courier with same name or phone alreday exists.")
            conn.close()
            return
    
        cur.execute("INSERT INTO couriers (name,phone) VALUES (%s,%s)",(name,phone))
        conn.commit()
        conn.close()
        print(f"✅ added courier: 👤 {name}, 📞 {phone}")
    except Exception as e:
        print(f"❌ Error adding courier: {e}")

def update_courier():
    view_couriers()
    try: 
        courier_id = int(input("🆔 Enter ID of courier to update: "))
    except ValueError:
        print("⚠️ Invalid ID")
        return
    
    new_name = input("✍️ Enter new name(leave blank to keep current) : ").strip()
    new_phone = input("📞 Enter new phone(leave blank to keep current) : ").strip()

    if new_phone and not is_valid_phone(new_phone):
        print("❌ Invalid phone number.")
        return
    try: 
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT name,phone FROM couriers WHERE courier_id = %s",(courier_id,))
        result = cur.fetchone()
        if not result:
            print("❌ Courier ID not found.")
            conn.close()
            return
    
        current_name,current_phone = result
        updated_name = new_name if new_name else current_name
        updated_phone = new_phone if new_phone else current_phone

        cur.execute("""
                SELECT * FROM couriers
                WHERE (name = %s OR phone = %s) AND courier_id != %s
        """,(updated_name,updated_phone,courier_id))
        if cur.fetchone():
            print("⚠️ Another courier with same name or phone exists.")
            conn.close()
            return
    
        cur.execute("""
            UPDATE couriers
            SET name = %s, phone = %s 
            WHERE courier_id = %s  
        """,(updated_name,updated_phone,courier_id))                 
        conn.commit()
        conn.close()
        print("✏️ Courier updated.")
    except Exception as e:
        print("f❌ Error updating courier: {e}")

def delete_courier():
    view_couriers()
    try:
        courier_id = int(input("🆔 Enter ID of courier you want to delete: "))
    except ValueError:
        print("⚠️ Invalid ID.")
        return
    
    confirm = input("⚠️ Are you sure you want to delete this courier(y/n):").lower()
    if confirm != 'y':
        print("🚫 Deletion cancelled.")
        return
    
    try: 
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM couriers WHERE  courier_id = %s",(courier_id,))
        conn.commit()
        conn.close()
        print("🗑️ Courier deleted.")
    except Exception as e:
        print(f"❌ Error deleting courier: {e}")

def print_courier_menu():
    print("\n📦 Couriers Menu:")
    print("0️⃣ : Return to main menu")
    print("1️⃣ : View Couriers")
    print("2️⃣ : Add Courier")
    print("3️⃣ : Update Courier")
    print("4️⃣ : Delete Courier")

def couriers_menu():
    while True:
        print_courier_menu()
        try: 
            choice = input("🔍 Enter your choice for courier menu: ")

            if choice == '0':
                print("🔙 Returning to main menu...")
                break
            elif choice == '1':
                view_couriers()
            elif choice == '2':
                name = input("✍️ Enter courier name: ").strip()
                phone = input("📞 Enter courier phone: ").strip()
                add_courier(name, phone)
            elif choice == '3':
                update_courier()
            elif choice == '4':
                delete_courier()
            else:
                print("❌ Invalid choice. Try again.")
        except Exception as e:
            print(f"🚫 Inexpected error: {e}")

        input("🔄 Press Enter to continue...")
