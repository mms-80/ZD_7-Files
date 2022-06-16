import os
from pprint import pprint

BASE_PATH = os.getcwd()
FILE_NAME = 'recipes.txt'

full_path = os.path.join(BASE_PATH, FILE_NAME)

def cook_book_func(full_path):
    cook_book = {}
    with open(full_path, encoding='utf8') as rec_file:
        food = rec_file.readline().strip()
        for line in rec_file:
            quantity = int(line.strip())
            lines = []
            for items in range(quantity):
                data = rec_file.readline().strip().split(' | ')
                lines.append({'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]})
            cook_book[food] = lines
            rec_file.readline()
            food = rec_file.readline().strip()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, full_path):
    result = {}
    cook_book = cook_book_func(full_path)
    menu = list(cook_book.keys())

    for dish in dishes:
        if dish not in menu:
            print(f'Блюдо: {dish} - нет в меню!')
        else:
            order = cook_book[dish]
            for ingredient in order:
                ingr_name = ingredient['ingredient_name']
                if ingredient['ingredient_name'] not in result:
                    ingr_quantity = int(ingredient['quantity']) * int(person_count)
                    ingr_measure = ingredient['measure']
                    result[ingr_name] = {'measure': ingr_measure, 'quantity': ingr_quantity}
                else:
                    result[ingr_name]['quantity'] += int(ingredient['quantity']) * int(person_count)

    return result

# pprint(cook_book_func(full_path))
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Утка по-пекински', 'Шашлык'], 2, full_path))
