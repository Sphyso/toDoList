list_dict = {}


#Adds items in the beginning
def add_item(item):
    key_num = 1
    value = item
    list_dict[key_num] = value
    while value != "Stop":
        key_num += 1
        value = input("Enter an item: ")
        if value != "Stop":
            list_dict[key_num] = value
        else:
            print("\n")
            print_list()
            start()


#Remove item based on the items number
def remove_item(item_num):
    list_dict.pop(item_num)
    print_list()
    start()

#Update items: takes in item num and the item
def update_item(item_num, item):
    list_dict[item_num] = item
    print_list()
    start()

#Used to add items the first set
def add_item_after(item):
    last_key = list(list_dict)[-1]
    last_key += 1
    list_dict[last_key] = item
    print_list()
    start()

#Prints the list
def print_list():
    for key, value in list_dict.items():
        print("\t", key, value)

#Get user choice
def choose_option(choice):
    if choice.upper() == 'A':
        item = input("Enter an item: ")
        add_item_after(item)
    elif choice.upper() == 'U':
        item_num = int(input("Enter the item number: "))
        item = input("Enter an item: ")
        update_item(item_num, item)
    elif choice.upper() == 'D':
        item_num = int(input("Enter the item number: "))
        remove_item(item_num)



#main method program starts here
def start():
    if len(list_dict) == 0:
        print("Add items to the list then enter 'Stop' to save \n")
        value = input("Enter an item: ")
        add_item(value)
    else:
        chioce = input("""
    Enter 'A' to add an item
    Enter 'U' to update an existing item
    Enter 'D' to delete an item
    **Enter any other character to end**
        """)

        choose_option(chioce)


start()