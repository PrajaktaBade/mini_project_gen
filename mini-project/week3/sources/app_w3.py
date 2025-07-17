
import product_menu
import order_menu
import couriers_menu

# Main Menu
def main_menu():
    while True:
        # clear_screen() 
        print('\nWelcome to the Cafe!!')
        print('What would you like to have ?')
        print("Main Menu options:\n")
        print("0️⃣  : Exit App\n"
              "1️⃣  : Products Menu\n"
              "2️⃣  : Couriers Menu\n" 
              "3️⃣  : Orders Menu")

        customer_input = input('Enter option for main menu: ')

        if customer_input == '0':
            print("Exiting app.Thank you !!")
            break

        elif customer_input == '1':
            product_menu.product_menu()
    
        elif customer_input == '2':
            couriers_menu.couriers_menu()

        elif customer_input == '3':
            order_menu.order_menu()
        
        else:
            print("Invalid choice.Please try again.")
            input("Press Enter to continue....")


if __name__ == '__main__':
    main_menu()


