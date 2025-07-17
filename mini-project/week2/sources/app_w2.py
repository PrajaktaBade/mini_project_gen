#Creating products list
products = ['Espresso','Americano','Cappuccino','Latte','Mocha','Flat White','Tea','Fresh Orange Juice','Blueberry Muffin','Chocklate Croissant','Bagel','Avocado Toast','Caesar Salad']
products_price = [2.5,2.75,3.0,3.5,3.75,3.25,2.0,3.0,2.80,3.20,3.50,4.25,5.5]

orders = {
    "order_1": {
        "customer_name": "John Jones",
        "customer_address": "Main Street, LONDON",
        "customer_phone": "07987654321",
        "status": "preparing"
    },
    "order_2": {
        "customer_name": "Emily Smith",
        "customer_address": "Park Avenue, LONDON",
        "customer_phone": "07123456789",
        "status": "ready for pickup"
    }
}

#printing main menu options
def main_menu():
    print('\nWelcome to the Cafe!!')
    print('What would you like to have ?')
    print("Main Menu options:\n")
    print("0 : Exit App\n"
          "1 : Print Products Menu\n"
          "2 : Print Orders Menu")
    
while True:
    main_menu()
#GET user input for main menu option
    customer_input = input('Enter option for main menu: ')

# EXIT app
    if customer_input == '0':
        print('Exiting app..Thank you!!')
        break
    
# Displaying products menu
    elif customer_input == '1':
        print("Here is the Product Menu options\n")
        print("Options: \n" 
            "0: Exit the app \n" 
            "1:Print Product List\n"
            "2: Menu options\n"
            "3: Add New Menu\n"
            "4: Delete Product")
        product_menu_input = input('Enter a menu option from the product list: ')

# Returning to main menu if product_menu_input is '0'    
        if product_menu_input == '0':
            print('Returning to main menu...')
        
# Printing product list available in the cafe     
        elif product_menu_input == '1':
            print("\n List of menu available here:")
            for idx,menu in enumerate(products,start =1): # Added enumerate for giving numbers to menu while displaying
                print(f"{idx} : {menu} : £{products_price[idx-1]}")
        
#Creating new list by appending new product    
        elif product_menu_input == '2':
            new_product = input('Enter new product name you would like to add:')
            products.append(new_product)
            print('Updated list:',products)
    
#Fetching index value with its product name & Updating a list with new element from user.
        elif product_menu_input == '3':
            indexed_list = list(enumerate(products))
            print(indexed_list)
            prd_index = int(input('Enter new product index you want to add new product in a list: '))
            prd_name = input('Enter a product name you would like add in a list:')
            if 0 <= prd_index <= len(products):
                products.insert(prd_index,prd_name)
                print('Updated product list: ',products)
            else: 
                print('Invalid index.Please enter a number between 0 and len(products) - 1')

#Taking a index value from user & deleting that element & displaying the updated list.

        elif product_menu_input == '4':
            print(products)
            prd_index = int(input("Enter a product index value you want to delete: "))
            if 0 <= prd_index < len(products):
                deleted_item = products.pop(prd_index)
                print(f"deleted_item : {deleted_item}")
                print("Updated list: " ,products)
            else:
                print('Invalid index.Please enter a number between 0 and len(products) - 1')

#Displaying order menu    
    elif customer_input == '2':
        print("Here is the orders list: \n")
        print("0 : Return to main menu\n" \
          "1 : prints Orders Dictionary\n"
          "2 : Create new order\n"
          "3 : Update existing order status\n"
          "4 : Update Existing order\n" \
          "5 : Delete order")
        order_menu_input = input("Enter you choice for order menu:\n")


#Accepting user input & going through conditions
#Returning to main menu if it is '0'
        if order_menu_input == '0':
            print("Returning to main menu...")
            main_menu()

#Printing orders Dictioanry
        elif order_menu_input == '1':
            print("Orders Details:")
            for order_id in sorted(orders):
                order = orders[order_id]
                print(f"\nOrder ID   :{order_id}")
                print(f"Name.        :{order['customer_name']}")
                print(f"Address.     :{order['customer_address']}")
                print(f"Phone Number :{order['customer_phone']}")
                print(f"Status.      :{order['status']}")
        
#Creating new order
        elif order_menu_input == '2':
            print("What would you like to order from the menu?")
            print("Add your order details here:\n")
            customer_name = input("Enter your name: ")
            address = input("Enter your address:")
            phone = input("Enter your phone number: ")
            status = input("Enter your order status(pending,confirmed,preparing etc.)")

            new_order_id = f"order_{len(orders)+1}"
            new_order = {
                "customer_name" : customer_name,
                "address": address,
                "phone": phone,
                "status": status   
            }

            orders[new_order_id] = new_order

            print(f"Order '{new_order_id}' added successfully!\n")     

# Updating existing order        
        elif order_menu_input == '3':   
            print("Update Existing Order Status\n")
            for order_id in orders:
                print(f"{order_id} - {orders[order_id]['customer_name']}")
            update_order_id = input("Enter the order ID you want to update (e.g order_1):")
            if update_order_id in orders:
                print(f"Current status of {update_order_id}:{orders[update_order_id]['status']}")
                new_status = input("Enter new status(e.g,pending.preparing):")
                orders[update_order_id]['status'] = new_status

                print(f"Status updated successfully for {update_order_id}!")
                print(f"Updated status:{orders[update_order_id]['status']}")
            else:
                print("Invalid order ID.Please check and try again.")

# Update Existing order
        elif order_menu_input == '4':
            order_id = input("Enter the order_id you want to update(e.gorder_1):")
        
            if order_id in orders:
                print(f"Current details for {order_id}:")
                for key,value in orders[order_id].items():
                    formatted_key = key.replace('-',' ').capitalize()
                    print(f"{formatted_key}:{value}")
                print("Enter a field you would like to update:")
                print("Options: customer_name,address,phone,status")
                field = input("Enter the field name:")
                if field in orders[order_id]:
                    new_value = input("Enter new value for {field.replace('-', ' ')}:")
                    orders[order_id][field] = new_value
                    print(f"\n{field.replace('-', ' ').capitalize()} updated successfully!")
                    print("\nUpdated Order Details:")
                    for key,value in orders[order_id].items():
                        formatted_key = key.replace("_"," ").capitalize()
                        print(f"{formatted_key}:{value}")
                else:
                    print("Invalid field name.Please choose from the listed options")
            else:
                print("Order Id not found.Please enter a valid one.")

# Deleting order    
        elif order_menu_input == '5':
            order_id = input("Enter the order ID you want to delete (e.g., order_1): ")
            if order_id in orders:
                print(f"\nCurrent details for {order_id}:")
                for key, value in orders[order_id].items():
                    formatted_key = key.replace("_", " ").capitalize()
                    print(f"{formatted_key}: {value}")
                confirm = input("Are you sure you want to delete this order? (yes/no): ").lower()

                if confirm == "yes":
                    del orders[order_id]
                    print(f"{order_id} has been deleted successfully.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Order ID not found. Please enter a valid one.")
    



        
        
