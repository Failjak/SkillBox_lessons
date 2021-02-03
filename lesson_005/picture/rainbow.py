import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# x = 1500
# y = -1000
# step = 17
# rainbow(x, y, step)
def rainbow(x , y, step):
    for color in rainbow_colors:
        point = sd.get_point(x, y)
        sd.circle(center_position=point, radius=1800, width=25, color=color)
        x += step
        y -= step
    sd.pause()

