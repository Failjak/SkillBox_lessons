# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw as sd

RES_X, RES_Y = 600, 600
sd.resolution = (RES_X, RES_Y)
sd.background_color = (255, 255, 255)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color, radius):
    sd.circle(center_position=sd.get_point(x, y), color=color, radius=radius, width=3)
    eye_right, eye_left = sd.get_point(x + radius/4, y + radius/3), sd.get_point(x - radius/4, y + radius/3)
    sd.circle(center_position=eye_right, radius=radius/10, color=color)
    sd.circle(center_position=eye_left, radius=radius/10, color=color)
    mouth_start, mouth_end = sd.get_point(x-radius/3, y - radius/5), sd.get_point(x+radius/3, y - radius/5)
    sd.line(mouth_start, mouth_end, color)


for _ in range(10):
    radius = random.randint(30, 60)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    smile(x=random.randint(radius, RES_X-radius), y=random.randint(radius, RES_Y-radius), color=color, radius=radius)


sd.pause()
