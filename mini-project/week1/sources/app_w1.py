#Creating products list
products = ['Espresso','Americano','Cappuccino','Latte','Mocha','Flat White','Tea','Fresh Orange Juice','Blueberry Muffin','Chocklate Croissant','Bagel','Avocado Toast','Caesar Salad']
products_price = [2.5,2.75,3.0,3.5,3.75,3.25,2.0,3.0,2.80,3.20,3.50,4.25,5.5]

#printing main menu options
def main_menu():
    print('Welcome to the Cafe!!')
    print('What would you like to have ?')
    print("Main Menu options:\n")
    print("0 : Exit App\n"
          "1 : Print Products Menu\n"
          "2 : Print Orders Menu")

main_menu()
#GET user input for main menu option
customer_input = input('Enter option for main menu: ')

# EXIT app
if customer_input == '0':
    print('Exiting app..Thank you!!')

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
        print('Exiting app..Thank you!!')
        main_menu()

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
