from os import system
# from seed import seed
# from items_operations import print_list_of_items, add_item, delete_item, update_item_price

#gets the list of products from the seed method, imported from seed.py
# list_of_products = seed()

# Prints a menu with several options and returns the selected option
def print_options():
    print("1. Show menu")
    print("2. Add product to the menu")
    print("3. Edit price of a product from the menu")
    print("4. Delete a product from the menu")
    print("5. Take an order")
    print("6. Exit")
    opt = input("Select your option (1-6): ")
    return opt


def add_product():
    # asks for name and
    name = input("What's the name of the new product? ")
    price = float(input (f"What's the price of {name}? "))

    # add_item(list_of_products, name, price)
    # print(f"{name} being added to the menu...")
    


def delete_product():
    #show the list of products
    # print_list_of_items(list_of_products)
    #ask about the product we want to delete
    name = input("What is the product you want to delete? ")
    # delete_item(list_of_products, name)
    #make sure it is in the menu

    #delete it

def edit_product():
    #show the list of products
    # print_list_of_items(list_of_products)
    #ask about the product we want to delete
    name = input("What is the product you want to update? ")
    #make sure it is in the menu
    # update_item_price(list_of_products,name)
    #ask for the new price

def take_order():
    print("start a new order...")
    # under construction

option = ""

# Menu feature: The while loop prints the menu option and the user select the option.
# Each valid option invokes the selected function
# The loop only stops when the input is 6 (exit option)
while option != "6":
    system('clear')
    # invoke print options and return the selected option
    option = print_options()
    system('clear')
    if option == "1":
        print("Prints the list of products...")
        # print_list_of_items(list_of_products)
    elif option == "2":
        print("asks for name and price and add the item to the list of products")
        # add_product()
    elif option == "3":
        print("asks for name of product and updates the price of the product")
        # edit_product()
    elif option == "4":
        print("asks for name of product and removes it from the list")
        # delete_product()
    elif option == "5":
        print("Takes an order")
        #take_order()
    #manages the exit option and the invalid options
    elif option == "6":
        continue
    else:
        print("Invalid option")
    #adds a break in the control flow until the user presses Enter    
    input("press Enter to continue...")
    system('clear')

print("Goodbye!") 
