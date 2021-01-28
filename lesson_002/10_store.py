#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

lamp_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamp_quan = store[goods['Лампа']][0]['quantity']

table_cost1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_cost2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
table_quan = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
table_cost = table_cost1 + table_cost2

sofa_cost1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofa_cost2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sofa_quan = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
sofa_cost = sofa_cost2 + sofa_cost1

chair_cost1 = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chair_cost2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chair_cost3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
chair_quan = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']
chair_cost = chair_cost1 + chair_cost2 + chair_cost3

print('Лампа: <кол-во> -', lamp_quan, '|<общая стоимость> - ', lamp_cost)
print('Стол: <кол-во> -', table_quan, '|<общая стоимость> - ', table_cost)
print('Диван: <кол-во> -', sofa_quan, '|<общая стоимость> - ', sofa_cost)
print('Стул: <кол-во> -', chair_quan, '|<общая стоимость> - ', chair_cost)