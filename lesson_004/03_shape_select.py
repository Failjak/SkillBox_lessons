# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
shape_tuple = {1: 'Triangle', 2: 'Square', 3: 'Pentagon', 4: 'Hexagon'}


def drawing(sides, point, angle, len, width):
    ang = 180 * (sides - 2) / sides
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=len, width=width)
    sd.line(start_point=vector_1.start_point, end_point=vector_1.end_point, width=width)
    new_start_point = vector_1.end_point
    for i in range(1, sides - 1):
        vector = sd.get_vector(start_point=new_start_point, angle=angle + i*(180-ang), length=len, width=width)
        sd.line(start_point=vector.start_point, end_point=vector.end_point, width=width)
        new_start_point = vector.end_point
    sd.line(start_point=new_start_point, end_point=vector_1.start_point, width=width)
    sd.pause()


def main():
    print('Enter shape:')
    for i, sh in shape_tuple.items():
        print(i, "-", sh)
    shape = int(input('Your choice:'))
    start_point = sd.get_point(250, 250)
    drawing(sides=shape + 2, point=start_point, angle=0, len=150, width=3)

main()