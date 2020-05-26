shopping_list=[]
plural="item"

def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items
    Enter 'HELP' to get help
    ENTER 'SHOW' to view the list.""")


def add_items(plural):
    while True:
        new_item = input("> ")
        if len(shopping_list)>0:
                plural="items"
        if new_item.upper() == 'DONE':
            break
        elif new_item.upper() == 'HELP':
            show_help()
            continue
        elif new_item.upper() == 'SHOW':
            show_list()
            continue
        else:
            shopping_list.append(new_item)
            print("{} added successfully.  You now have {} {} in your list.".format(new_item, len(shopping_list),plural))


def show_list():
    print("Your shopping list:")
    for items in shopping_list:
        print(items)            

show_help()
add_items(plural)




