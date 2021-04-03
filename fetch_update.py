import json, os, time

def update_item(items):
    with open('item.txt', 'w') as my_file:
        json.dump(items, my_file, indent=4)

def fetch_items():
    with open('item.txt', 'r') as item_file:
        return json.load(item_file)

def update_user(user):
    time.sleep(1)
    os.system('cls')
    print("\nUser's credential update:")
    for credential, value in user.items():
        print(f'{credential.capitalize()} : {value}')
    with open('user_credentials.txt', 'w') as my_file:
        json.dump(user, my_file, indent=4)

def fetch_user_cred():
    with open('user_credentials.txt', 'r') as uesr_file:
        return json.load(uesr_file)