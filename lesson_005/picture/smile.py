import random
import simple_draw as sd

# RES_X, RES_Y = 600, 600
# sd.resolution = (RES_X, RES_Y)
# sd.background_color = (255, 255, 255)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_smile(x, y, radius):
    sd.circle(center_position=sd.get_point(x, y), color=color, radius=radius, width=3)
    eye_right, eye_left = sd.get_point(x + radius/4, y + radius/3), sd.get_point(x - radius/4, y + radius/3)
    sd.circle(center_position=eye_right, radius=radius/10, color=color)
    sd.circle(center_position=eye_left, radius=radius/10, color=color)
    mouth_start, mouth_end = sd.get_point(x-radius/3, y - radius/5), sd.get_point(x+radius/3, y - radius/5)
    sd.line(mouth_start, mouth_end, color)



# smile(x=random.randint(radius, RES_X-radius), y=random.randint(radius, RES_Y-radius), radius)


# sd.pause()