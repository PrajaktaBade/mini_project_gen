import csv
import os
from utils import load_csv,save_csv

base_dir = os.path.dirname(os.path.dirname(__file__))
data_folder = os.path.join(base_dir,"data")
os.makedirs(data_folder, exist_ok =True)

file_name = os.path.join(data_folder,"couriers.csv")
fieldnames = ["name","phone"]

def load_couriers():
    return load_csv(file_name,fieldnames)

def save_couriers(couriers):
    save_csv(file_name,fieldnames,couriers)

def is_valid_phone(phone):
    cleaned = phone.replace("+","").replace("-","").replace(" ","")
    return cleaned.isdigit() and 7 <= len(cleaned) <= 11

def view_couriers(couriers):
    if not couriers:
        print("❌ No couriers found.")
        return
    print("\nCouriers : ")
    print("\n{:<5}{:<20} {:<15}".format("ID","Courier Name","Phone Number"))
    print("-" * 45)
    for i ,courier in enumerate(couriers):
        print("{:<5} {:<20} {:<15}".format(i,courier['name'],courier['phone']))
    print("-"* 45)

def add_courier(couriers,name,phone):
    if not name or not phone:
        print("⚠️ Name and phone cannot be empty.")
        return
    
    if not is_valid_phone(phone):
        print("❌ Invalid phone number.Please enter a valid number (11 digits including 0 at starting,digits only).")
        return
    
    for courier in couriers:
        if courier['name'].lower == name.lower() and courier['phone'] == phone:
            print("⚠️ A courier with the same name and phone number already exists.")
            return
        elif courier['phone'] == phone:
            print("⚠️ A courier with the same phone number already exists.")
            return
        elif courier['name'].lower() == name.lower():
            print("⚠️ A courier with the same name already exists.")
            return

    couriers.append({"name": name,"phone": phone})
    save_couriers(couriers)
    print(f"✅ Added courier: {name},📞{phone}")

def update_courier(couriers,index,new_name,new_phone):
    if not(0 <= index < len(couriers)):
        print("❌ Invalid index.")
        return
    current_courier = couriers[index]

    if new_name:
           new_name = new_name.strip()
           for i,courier in enumerate(couriers):
               if i != index and courier["name"].lower() == new_name.lower():
                   print("⚠️ A courier with the same name already exists.")
                   return         
           couriers[index]["name"] = new_name

    if new_phone:
            new_phone = new_phone.strip()
            if not is_valid_phone(new_phone):
                print("❌ Invalid phone number.Must be 11 digit including 0 at the starting,digits only.")
                return 
            
            for i, courier in enumerate(couriers):
                if i != index and courier["phone"] == new_phone:
                    print("⚠️ A courier with the same phone number already exists.")
                    return
            
            current_courier["phone"] = new_phone

    save_couriers(couriers)
    print("✏️Courier updated.")


    
def delete_courier(couriers,index):
    try:
        if not (0 <= index < len(couriers)):
            print("❌ Invalid index.")
            return
        removed = couriers[index]
    
        confirm =input(f"⚠️ Are you sure you want to delete courier '{removed['name']}: ")
        if confirm.lower() != 'y':
            print("🚫 Deletion cancelled.")
            return

        couriers.pop(index)

        try:
            save_couriers(couriers)
            print(f"🗑️ Deleted courier: {removed['name']}")
        except IOError as e:
            print("❌  Failed to save updated couriers file: {e}")
    
    except Exception as e:
        print ("⚠️ An unexpected error occured during deletion: {e}")
        

def print_courier_menu():
    print("\n 📦 Couriers menu list :\n")
    print("0️⃣ : Return to main menu\n" \
          "1️⃣ : View Couriers\n"
          "2️⃣ : Add new Courier\n"
          "3️⃣ : Update Courier\n"
          "4️⃣ : Delete Courier")


def couriers_menu():
    couriers = load_couriers()
    
    while True:
        print_courier_menu()
        courier_menu_input = input("🔍 Enter your choice for courier menu:\n")

        if courier_menu_input == '0':
            print('🔙 Out of the Courier menu...')
            save_couriers(couriers)
            break
        
        elif courier_menu_input == '1':
            view_couriers(couriers)
            input("🔄 Press 'Enter' to continue...")
        
        elif courier_menu_input == '2':
            name = input("✍️ Enter courier name: ").strip()
            phone = input("📞Enter courier phone: ").strip()
            add_courier(couriers,name,phone)
            input("🔄 Press 'Enter' to continue...")
                
        elif courier_menu_input == '3':
            view_couriers(couriers)
            try:
                index = int(input("🆔 Enter index of courier to update:"))
                new_name = input("✍️ Enter new name: ").strip()
                new_phone = input("📞 Enter new phone: ").strip()
                update_courier(couriers,index,new_name,new_phone)
            except ValueError:
                print("⚠️ Invalid index.")
            input("🔄 Press 'Enter' to continue...")
        
        elif courier_menu_input == '4':   
            view_couriers(couriers)
            try:
                index = int(input("🆔 Enter index of courier to delete: "))
                delete_courier(couriers,index)
            except ValueError:
                print("⚠️ Invalid index.")   
            input("🔄 Press 'Enter' to continue...")  

        else:
            print("❌ Invalid choice,try again.")  
            input("🔄 Press 'Enter' to continue...")