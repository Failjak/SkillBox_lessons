import simple_draw as sd
import random


def snowfall(n):
    speed, coord, length = [], [], []
    for i in range(n):
        speed.append(random.randint(10, 50))
        x = random.randint(10, 250)
        y = random.randint(300, 350)
        coord.append([x, y])
        length.append(random.randint(5, 10))

    while True:
        for i in range(n):
            sd.start_drawing()
            wind = random.randint(-20, 20)

            point = sd.get_point(coord[i][0], coord[i][1])
            sd.snowflake(center=point, length=length[i], color=sd.background_color)
            coord[i][0] -= wind
            coord[i][1] -= speed[i]

            x0, y0 = coord[i][0], coord[i][1]
            point = sd.get_point(x0, y0)
            sd.snowflake(center=point, length=length[i])

            if coord[i][1] <= 20 and speed != 0:
                speed[i] = 0
                coord[i].pop()
                coord[i].pop()

            sd.finish_drawing()

            if speed[i] == 0:
                speed.pop(i)
                speed.insert(i, random.randint(5, 30))

            if len(coord[i]) == 0:
                length.pop(i)
                length.insert(i, random.randint(5, 10))
                coord.remove([])
                x = random.randint(10, 250)
                y = random.randint(300, 350)
                coord.insert(i, [x, y])

        sd.sleep(0.1)
        if sd.user_want_exit():
            break
    # sd.pause()


# def main():
#     snowfall(10)


# main()