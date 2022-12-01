
def print_list_of_items(items):
    for item in items:
        print(item)

# adds a new item to the menu
def add_item(items, name, price):

    new_item = {"name": name, "price": price}
    items.append(new_item)

def delete_item(items, name):
    # iterate through the list looking for the item
    for item in items:
        # check if the item's name of this iteration is equal to the name we receive.
        if item["name"] == name:
            # access to the list and remove the item
            items.remove(item)
            print(f"{name} was removed from the menu")
            
        print(f"{name} is not in the menu")   

def update_item_price(items, name):
    # iterate through the list looking for the item
    for item in items:
        # check if the item's name of this iteration is equal to the name we receive.
        if item["name"] == name:
            # ask for the new price
            price = float(input(f"What is the new price for {name}? "))
            #update the item's price
            item["price"] = price
            print(f"{name}'s price was uptaded in the menu")

        print(f"{name} is not in the menu")   
