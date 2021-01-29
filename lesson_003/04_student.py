# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

educational_grant_year = 10 * educational_grant + .0
expenses_year = new_expenses = expenses + .0
i = 1
while i < 10:
    new_expenses *= 1.03
    expenses_year += new_expenses
    i += 1
print(round(expenses_year, 2), 'руб.')

parents_money = expenses_year - educational_grant_year
print('Стеденту надо попросить', round(parents_money, 2))