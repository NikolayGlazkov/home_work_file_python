import yaml

data = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price': {
        'computer': '200€-1000€',
        'keyboard': '5€-50€',
        'mouse': '4€-7€',
        'printer': '100€-300€'
    }
}

with open('test.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open('test.yaml', encoding='utf-8') as file:
    print(file.read())