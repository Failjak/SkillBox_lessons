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
def snowfall(n):
    speed, coord, length = [], [], []
    for i in range(n):
        speed.append(random.randint(10, 50))
        x = random.randint(50, 550)
        y = random.randint(400, 550)
        coord.append([x, y])
        length.append(random.randint(10, 25))
    while True:
        for i in range(n):
            wind = random.randint(-20, 20)
            if speed[i] == 0:
                speed.pop(i)
                speed.insert(i, random.randint(5, 30))

            if len(coord[i]) == 0:
                length.pop(i)
                length.insert(i, random.randint(10, 40))
                coord.remove([])
                x = random.randint(50, 550)
                y = random.randint(500, 550)
                coord.insert(i, [x, y])

            coord[i][0] -= wind
            coord[i][1] -= speed[i]
            x0, y0 = coord[i][0], coord[i][1]
            point = sd.get_point(x0, y0)
            sd.snowflake(center=point, length=length[i])

            if coord[i][1] <= 2*length[i] and speed != 0:
                speed[i] = 0
                coord[i].pop()
                coord[i].pop()
            # elif (coord[i][0] >= 560 and wind < 0) or (coord[i][0] <= 40 and wind > 0):
            #     wind *= -1
        sd.sleep(0.1)
        for i in range(n):
            if len(coord[i]) != 0:
                x0, y0 = coord[i][0], coord[i][1]
                point = sd.get_point(x0, y0)
                sd.snowflake(center=point, length=length[i], color=sd.background_color)

        if sd.user_want_exit():
            break
    sd.pause()


def main():
    snowfall(10)


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


