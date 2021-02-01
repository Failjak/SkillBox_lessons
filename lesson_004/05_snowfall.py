# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
def snowfall(n, coord, wind, speed):
    lenght = 20
    while True:
        for i in range(n):
            x0, y0 = coord[i][0], coord[i][1]
            point = sd.get_point(x0, y0)
            sd.snowflake(center=point, length=lenght)
            if coord[i][1] <= lenght and speed != 0:
                speed[i] = 0
                wind[i] = 0
                # coord.pop([i][0])
                # coord.pop([i][1])
            if coord[i][0] >= 580 and wind[i] > 0:
                wind[i] = 0
                # coord.pop([i][0])
                # coord.pop([i][1])
            if coord[i][0] <= 20 and wind[i] < 0:
                wind[i] = 0
                # coord.pop([i][0])
                # coord.pop([i][1])
            sd.sleep(.1)
        for i in range(n):
            x0, y0 = coord[i][0], coord[i][1]
            point = sd.get_point(x0, y0)
            sd.snowflake(center=point, length=lenght, color=sd.background_color)
        coord[i][0] -= wind[i]
        coord[i][1] -= speed[i]
        if sd.user_want_exit():
            break
    sd.pause()


def main():
    speed = []
    wind = []
    snowflake_coord = []
    # quan = int(input('Enter the num of snowflakes:'))
    for i in range(3):
        speed.append(random.randint(10, 50))
        wind.append(random.randint(-20, 20))
        x = random.randint(50, 550)
        y = random.randint(400, 550)
        snowflake_coord.append([x, y])
    snowfall(3, snowflake_coord, wind, speed)


main()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


