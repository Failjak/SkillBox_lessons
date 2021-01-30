# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (600, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# start_x = 50
# end_x = 350
# step = 15
# for color in rainbow_colors:
#     start_point = sd.get_point(start_x, 50)
#     end_point = sd.get_point(end_x, 350)
#     sd.line(start_point, end_point, color, 13)
#     start_x += step
#     end_x += step



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x = 1500
y = -1000
step = 17
for color in rainbow_colors:
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=1800, width=25, color=color)
    x += step
    y -= step
sd.pause()
