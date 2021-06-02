from mago_class_lib import *


def get_mouse(event, x, y, flags, param):
    global mouse_x
    global mouse_y
    mouse_x = x
    mouse_y = y


def jisuan(dx, dy, dr, r, width, height):
    a = (dr - r) / sqrt(2)
    bx = 2 * a / width
    cx = dx - a
    x = int(cx + bx * mouse_x)

    by = 2 * a / height
    cy = dy - a
    y = int(cy + by * mouse_y)

    return x, y


width = 800
height = 600
mouse_x = 0
mouse_y = 0
x1 = 305
y1 = 180
R = 90
x2 = 495
y2 = 180

xx = 385
yy = 180

r = 55
window()
mouse(get_mouse)
while True:
    canvas(width, height)
    circle(400, 300, 250)
    circle(400, 300, 20)
    circle(400, 420, 70)

    circle(x1, y1, R)
    circle(x2, y2, R)

    # a = (R - r) / sqrt(2)
    # bx = 2 * a / width
    # cxz = x1 - a
    # x3 = int(cxz + bx * mouse_x)
    #
    # by = 2 * a / height
    # cyz = y1 - a
    # y3 = int(cyz + by * mouse_y)
    #
    # cxy = x2 - a
    # cyy = y2 - a
    # x4 = int(cxy + bx * mouse_x)
    # y4 = int(cyy + by * mouse_y)
    #
    #
    # # circle(x3, y3, r, thickness=-1)
    # # circle(x4, y4, r, thickness=-1)

    x3, y3 = jisuan(x1, y1, R, r, width, height)
    circle(x3, y3, r, thickness=-1)
    x4, y4 = jisuan(x2, y2, R, r, width, height)
    circle(x4, y4, r, thickness=-1)
    # x5, y5 = jisuan(xx, yy, R, r, width, height)
    # circle(x5, y5, r, thickness=-1)

    image_png("/Users/Jacky/Documents/pyCharmProj/basicGrammer/org/teamsun/mago/codes/image/wz_64.png", mouse_x - 32, mouse_y - 32, 0, -1)
    # image_png("image/wz_64.png", 0, 0, 0, -1)

    show(1)
