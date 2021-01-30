# -*- coding: utf-8 -*-

# (цикл for)
import random

import simple_draw as sd
SIZE_X, SIZE_Y = 600, 600
sd.resolution = (SIZE_X, SIZE_Y)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

color = (139, 69, 19)
for y in range(0, SIZE_Y + 1, 50):
    start_point = sd.get_point(0, y)
    end_point = sd.get_point(SIZE_X, y)
    sd.line(start_point=start_point, end_point=end_point, width=2, color=color)
    if y % 100 == 0:
        start = 0
    else:
        start = 50
    for x in range(start, SIZE_X, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x, y-50)
        sd.line(start_point=start_point, end_point=end_point, width=2, color=color)


sd.pause()
