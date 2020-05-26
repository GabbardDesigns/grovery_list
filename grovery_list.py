shopping_list=[]
plural="item"

def main_menu(plural):
    while True:
        print("Please select an option from the menu.")
        print("""
        Enter 'ADD' to add items to your shopping list
        ENTER 'SHOW' to view the list
        ENTER 'QUIT' to end the program.""")
        menu_selection = input("> ").upper()
        if menu_selection == 'QUIT':
            break
        elif menu_selection == 'ADD':
            add_items(plural)
            continue
        elif menu_selection == 'SHOW':
            show_list()
            input("""
            Press any key to continue.""") 
            continue



def show_menu():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items
    Enter 'HELP' to get help
    ENTER 'SHOW' to view the list.""")

def add_items(plural):
    show_menu()
    while True:
        new_item = input("> ")
        if len(shopping_list)>0:
                plural="items"
        if new_item.upper() == 'DONE':
            break
        elif new_item.upper() == 'HELP':
            show_menu()
            continue
        elif new_item.upper() == 'SHOW':
            show_list()
            show_menu()
            continue
        else:
            shopping_list.append(new_item)
            print("{} added successfully.  You now have {} {} in your list.".format(new_item, len(shopping_list),plural))


def show_list():
    print("Your shopping list:")
    for items in shopping_list:
        print(items)           

main_menu(plural)




