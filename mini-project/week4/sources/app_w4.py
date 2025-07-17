from utils import clear_screen 
import product_menu
import order_menu
import couriers_menu

# Main Menu
def main_menu():
    while True:
        try:
            clear_screen() 
            print('\nWelcome to the Cafe!!')
            print('What would you like to have ?')
            print("Main Menu options:\n")
            print("0️⃣  : Exit App\n"
                  "1️⃣  : Products Menu 🍽️\n"
                  "2️⃣  : Couriers Menu 🚚\n" 
                  "3️⃣  : Orders Menu 🛍️")

            customer_input = input('Enter option for main menu: ')

            if customer_input == '0':
                print("Exiting app.Thank you !!")
                break

            elif customer_input == '1':
                try:
                    product_menu.product_menu()
                except Exception as e:
                    print(f"Error occured in Product Menu: {e}")
                    input("Press 'Enter' to return to main menu...")
    
            elif customer_input == '2':
                try:
                    couriers_menu.couriers_menu()
                except Exception as e:
                    print(f"Error occured in Courier Menu: {e}")
                    input("Press 'Enter' to return to main menu...")


            elif customer_input == '3':
                try:
                    order_menu.order_menu()
                except Exception as e:
                    print(f"Error occured in Order Menu: {e}")
                    input("Press 'Enter' to return to main menu...")
        
            else:
                print("⚠️ Invalid choice.Please try again.")
                input("Press 'Enter' to continue....")

        except KeyboardInterrupt:
            print("\nApplication interrupted by user. Existing gracefully.")
            break

        except Exception as main_e:
            print(f"Unexpected error: {main_e}")
            input("Press 'Enter' to continue")    


if __name__ == '__main__':
    main_menu()


