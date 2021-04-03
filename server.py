from fetch_update import fetch_items, fetch_user_cred, update_user, update_item
from main import print_items
import os, time

def update(item):
    item_quantity = item.get('quantity')
    response = int(input('\t1. Add quantity\n\t2. Subtract quantity\n\tWhich to perform? '))
    if response == 1:
        number_of_items = int(input("How many to add? "))
        item.update({'quantity': item_quantity + number_of_items})
        return
    elif response == 2:
        number_of_items = int(input("How many to subtract? "))
        item.update({'quantity': item_quantity - number_of_items})
        return
    print('Invalid response! Returning')

def print_list():
    items = fetch_items()
    print_items(items)
    ans = int(input('Which items to update? '))
    item_to_update = items['mouse'][ans - 1]
    update(item_to_update)
    time.sleep(1)
    os.system('cls')
    print('\nUpdate on item:')
    print_items(items)
    update_item(items)


if __name__ == '__main__':
    print_list()
