import random
import simple_draw as sd

sd.resolution = (600, 600)
COLOR = (139, 69, 19)

start_point_y = 10
start_point_x = 10

width = 3
height_wall = 500
width_wall = 500

height_brick = 50
width_brick = 100
# TODO Сделать на пол кирпича


def draw_wall(x0, y0, height_wall, width_wall, height_brick, width_brick, width):
    for y in range(y0, y0 + height_wall + 1, height_brick):
        start_point = sd.get_point(x0, y)
        sd.get_vector(start_point, 0, width_wall, width).draw(color=COLOR)
        if y + height_brick >= y0 + height_wall + 1:
            break
        x_start = random.randint(x0 + width_brick/2, x0 + 3*width_brick/4)
        for x in range(x_start, x0 + width_wall, width_brick):
            start_point = sd.get_point(x, y)
            sd.get_vector(start_point, 90, height_brick, width).draw(color=COLOR)
    sd.get_vector(sd.get_point(x0, y0), 90, height_wall, width).draw(color=COLOR)
    sd.get_vector(sd.get_point(x0 + width_wall, y0), 90, height_wall, width).draw(color=COLOR)
    sd.get_vector(sd.get_point(x0, y0), 0, width_wall, width).draw(color=COLOR)
    sd.pause()


draw_wall(start_point_x, start_point_y, height_wall, width_wall, height_brick, width_brick, width)
