# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resolution = (600, 600)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
color_tuple = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE,
               3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN,
               5: sd.COLOR_CYAN, 6: sd.COLOR_BLUE,
               7: sd.COLOR_PURPLE}


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    for x in range(5):
        alfa = random.uniform(-30 * 1.4, 30 * 1.4)
        vector = sd.get_vector(start_point=start_point, angle=angle + alfa, length=length, width=3)
        color = random.randint(1, 7)
        vector.draw(color=color_tuple[color])
        coef = random.uniform(.75 * .2, .75 * 1.2)
        draw_branches(vector.end_point, angle + alfa, length * coef)


point = sd.get_point(300, 30)
angle, length = 90, 100
draw_branches(point, angle, length)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


