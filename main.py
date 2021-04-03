from fetch_update import fetch_items, fetch_user_cred, update_user, update_item

def buy_items(quantity_to_buy, item, user):
    item_quantity = item.get('quantity')
    user_balance = user.get('balance')
    to_pay = item.get('price') * quantity_to_buy

    # if the purchase is valid, we update
    if user_balance >= to_pay:
        if item_quantity > quantity_to_buy:
            item.update({'quantity': item_quantity - quantity_to_buy})
            user.update({'balance': user_balance - to_pay})
            return
        print('Insufficient Stock! Please recharge')
        return
    print('Insufficient Balance! Please recharge!')

def print_items(items):
    # list of items inside json file
    print('\nItem\t\tColor\tPrice\tQuantity')
    for x, item in enumerate(items['mouse'], start=1):
        print('{}. {}\t{}\t{}\t{}'.format(x, item.get('name'),
                                          item.get('color'), item.get('price'), item.get('quantity')))
def main_transaction():
    # we load the items and user credentials
    items = fetch_items()
    user = fetch_user_cred()
    # print user's credential
    for credential, value in user.items():
        print(f'{credential.capitalize()} : {value}')

    print_items(items)
    # user input to which product he chooses to buy
    which_item = int(input('What item do you want to buy? '))
    to_buy = int(input('How many? '))

    # we only pass the item to be modified in which the user chose
    item_to_buy = items['mouse'][which_item - 1]
    buy_items(to_buy, item_to_buy, user)
    update_item(items)
    update_user(user)


if __name__ == '__main__':
    main_transaction()








