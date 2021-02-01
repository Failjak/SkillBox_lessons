# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1500, 800)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(point, angle=0, len=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=len, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=len, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=len, width=3)
#     v3.draw()
#
#
# point_triangle = sd.get_point(400, 400)
# triangle(point_triangle, 0, 150)
#
#
# def square(point, angle, len=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=len, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=len, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=len, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=len, width=3)
#     v4.draw()
#
#
# point_square = sd.get_point(100, 50)
# square(point_square, 0, 100)
#
# # - пятиугольника
# def pentagon(point, angle, len):
#     n = 5
#     sum_angle = 180*(n-2)
#     ang = sum_angle//n
#     print(ang)
#     v1 = sd.get_vector(start_point=point, angle=angle, length=len, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle+(180-ang), length=len, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 2*(180-ang), length=len, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 3*(180-ang), length=len, width=2)
#     v4.draw()
#
#     sd.line(start_point=v4.end_point, end_point=v1.start_point, width=2)
#
#
# point_pentagon = sd.get_point(200, 300)
# pentagon(point_pentagon, 0, 100)
#
#
# def hexagon(point, angle, len):
#     n = 6
#     sum_angle = 180 * (n - 2)
#     ang = sum_angle // n
#     print(ang)
#     v1 = sd.get_vector(start_point=point, angle=angle, length=len, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + (180 - ang), length=len, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 2 * (180 - ang), length=len, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 3 * (180 - ang), length=len, width=2)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 4 * (180 - ang), length=len, width=2)
#     v5.draw()
#
#     sd.line(start_point=v5.end_point, end_point=v1.start_point, width=2)
#
#
# hexagon_point = sd.get_point(300, 200)
# hexagon(hexagon_point, 0, 50)
def drawing(sides, point, angle, len, width):
    ang = 180 * (sides - 2) / sides
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=len, width=width)
    vector_1.draw()
    new_start_point = vector_1.end_point
    for i in range(1, sides - 1):
        vector = sd.get_vector(start_point=new_start_point, angle=angle + i*(180-ang), length=len, width=width)
        new_start_point = vector.end_point
        vector.draw()
    sd.line(start_point=new_start_point, end_point=vector_1.start_point, width=width)


start_point = sd.get_point(700, 300)
drawing(sides=10, point=start_point, angle=0, len=50, width=3)


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
