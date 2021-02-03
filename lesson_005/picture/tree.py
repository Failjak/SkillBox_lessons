import simple_draw as sd
import random
sd.resolution = (1200, 600)


def tree(point, angle, length, delta):
    if length < 10:
        return
    vector = sd.get_vector(point, angle, length, 3)
    vector.draw()
    point = vector.end_point
    delta = random.uniform(.2 * 30, 1.8 * 30)
    tree(point, angle - delta, length * .75, delta)
    delta = random.uniform(.2 * 30, 1.8 * 30)
    tree(point, angle + delta, length * .75, delta)
    sd.pause()


# tree(sd.get_point(600, 5), angle=90, length=100, delta=30)

