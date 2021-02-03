# -*- coding: utf-8 -*-

from district.central_street.house1 import room1 as cs_h1_r1, room2 as cs_h1_r2
from district.central_street.house2 import room1 as cs_h2_r1, room2 as cs_h2_r2
from district.soviet_street.house1 import room1 as ss_h1_r1, room2 as ss_h1_r2
from district.soviet_street.house2 import room1 as ss_h2_r1, room2 as ss_h2_r2


# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

print('На районе живут: ', ', '.join(cs_h1_r1.folks+cs_h1_r2.folks+cs_h2_r1.folks+cs_h2_r2.folks), ',', sep='')
print(', '.join(ss_h1_r1.folks+ss_h1_r2.folks+ss_h2_r1.folks+ss_h2_r2.folks), '.', sep='')
