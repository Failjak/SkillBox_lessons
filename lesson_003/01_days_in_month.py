# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('В', month, 'месяце 31 день')
elif month == 2:
    print('В', month, 'месяце либо 28, либо 29 дней')
elif month == 4 or month == 6 or month == 11:
    print('В', month, 'месяце либо 30 дней')
else:
    print('Месяц введен некорректно')