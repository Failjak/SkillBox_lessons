import random
import simple_draw as sd


def draw_wall():
    COLOR = (139, 69, 19)

    start_point_y = y0 = 10
    start_point_x = x0 = 450

    width = 3
    height_wall = 300
    width_wall = 300

    height_brick = 50
    width_brick = 100
    for y in range(y0, y0 + height_wall + 1, height_brick):
        start_point = sd.get_point(x0, y)
        sd.get_vector(start_point, 0, width_wall, width).draw(color=COLOR)
        if y + height_brick >= y0 + height_wall + 1:
            break
        x_start = int(random.uniform(x0 + width_brick/2, x0 + 3*width_brick/4))
        for x in range(x_start, x0 + width_wall, width_brick):
            start_point = sd.get_point(x, y)
            sd.get_vector(start_point, 90, height_brick, width).draw(color=COLOR)
    sd.get_vector(sd.get_point(x0, y0), 90, height_wall, width).draw(color=COLOR)
    sd.get_vector(sd.get_point(x0 + width_wall, y0), 90, height_wall, width).draw(color=COLOR)
    sd.get_vector(sd.get_point(x0, y0), 0, width_wall, width).draw(color=COLOR)
    draw_roof(start_point_x, start_point_y, height_wall, width_wall, COLOR)


def draw_roof(x0, y0, height_wall, width_wall, COLOR):
    points = [sd.Point(x=x0 - width_wall / 4, y=y0 + height_wall), sd.Point(x=x0 + width_wall / 2, y=y0 + 1.8 * height_wall), sd.Point(x=x0 + 5 * width_wall / 4, y=y0 + height_wall)]
    sd.polygon(point_list=points, color=COLOR, width=0)


# draw_wall()

