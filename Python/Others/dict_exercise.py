shopping_dict = {
    'milk': 3,
    'rice': 4,
    'egg': 5,
    'cola': 2,
}


def add_item(item):
    if item in shopping_dict:
        shopping_dict[item] += 1
    else:
        shopping_dict[item] = 1
    print('Item added into the list')

def remove_item(item):
    if item in shopping_dict:
        shopping_dict[item] -= 1
        if shopping_dict[item] == 0:
            shopping_dict.pop(item)
        print('Item removed')
    else:
        print('Item is not in the list')


def display_items():
    print('Your shopping list:')
    for key, value in shopping_dict.items():
        print(f'{key}: {value}')


options = [
    'Add new item',
    'Remove item',
    'Display items',
    'Quit'
]


option = 0

while option != '4':
    display_items()
    print('You can manage your shopping list by the options below:')
    for num, item in enumerate(options, start=1):
        print(f"{num}. {item}")

    option = input('Please choose your option: ')

    if option == '1':
        item = input('Please add item: ')
        add_item(item)

    elif option == '2':
        item = input('Please input item to remove: ')
        remove_item(item)

    elif option == '3':
        display_items()
