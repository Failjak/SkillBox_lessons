# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
color_dict = {1: 'COLOR_RED', 2: 'COLOR_ORANGE',
              3: 'COLOR_YELLOW', 4: 'COLOR_GREEN',
              5: 'COLOR_CYAN', 6: 'COLOR_BLUE',
              7: 'COLOR_PURPLE'}
color_tuple = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE,
               3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN,
               5: sd.COLOR_CYAN, 6: sd.COLOR_BLUE,
               7: sd.COLOR_PURPLE}


def drawing(sides, point, angle, len, width, col):
    ang = 180 * (sides - 2) / sides
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=len, width=width)
    sd.line(start_point=vector_1.start_point, end_point=vector_1.end_point, width=width, color=col)
    new_start_point = vector_1.end_point
    for i in range(1, sides - 1):
        vector = sd.get_vector(start_point=new_start_point, angle=angle + i*(180-ang), length=len, width=width)
        sd.line(start_point=vector.start_point, end_point=vector.end_point, width=width, color=col)
        new_start_point = vector.end_point
    sd.line(start_point=new_start_point, end_point=vector_1.start_point, width=width, color=col)
    sd.pause()


print('Enter color:')
for i, col in color_dict.items():
    print(i, "-", col)
color = color_tuple[int(input('Your choice:'))]
start_point = sd.get_point(150, 150)
drawing(sides=10, point=start_point, col=color, angle=0, len=50, width=3)