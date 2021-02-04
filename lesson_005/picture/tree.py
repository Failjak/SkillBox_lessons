import simple_draw as sd


def drawing_tree(point, angle, length, color, width):
    delta = 30
    if length < 3:
        return
    if length < 15:
        color = sd.COLOR_GREEN
        width = 1
    vector = sd.get_vector(point, angle, length, width)
    vector.draw(color=color)
    point = vector.end_point
    # delta = random.uniform(.2 * 30, 1.8 * 30)
    drawing_tree(point, angle - delta, length * .75, color, width)
    # delta = random.uniform(.2 * 30, 1.8 * 30)
    drawing_tree(point, angle + delta, length * .75, color, width)



# tree(sd.get_point(600, 5), angle=90, length=100, color=sd.COLOR_DARK_ORANGE, width=4)
# sd.pause()
