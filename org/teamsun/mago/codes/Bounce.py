from mago_class_lib import *
from random import randint

mouse_x = 0
mouse_y = 0


def get_mouse(event, x, y, flags, param):
    global mouse_x
    global mouse_y
    mouse_x = x
    mouse_y = y


width = 800
height = 600
x = 10
y = 10
r = 10
vx = 0
vy = 0
length = 100
dist = height - 100
f1 = 0
f2 = 0
score = 0
level = 'level 1'
box_size = 20
lucky_box = []
lucky_show = False
ex_len = 0
temp_len = 0
temp_num = 0
window()
mouse(get_mouse)
while True:
    canvas(width, height)

    x += vx
    y += vy
    if y < r:
        score += abs(vx * vy)

        if temp_len != 0:
            temp_num += 1
            if temp_num > 5:
                temp_len = 0
                temp_num = 0

        if randint(0, 10) == 1:
            vx = randint(-3, 3)
            vy = randint(1, 2)
        else:
            vy = -vy
        if randint(0, 10) == 7:
            lucky_show = True
            lx = randint(0, width - box_size)
            ly = randint(0, dist - box_size / 2)
            lucky_box = [lx, ly, lx + box_size, ly + box_size]
        if score < 20:
            length = 100 + ex_len + temp_len
        elif 20 <= score < 50:
            length = 90 + ex_len + temp_len
            level = 'level 2'
        elif 50 <= score < 70:
            length = 70 + ex_len + temp_len
            level = 'level 3'
        elif 70 <= score < 100:
            length = 50 + ex_len + temp_len
        elif 100 <= score < 150:
            length = 40 + ex_len + temp_len
            level = 'level 4'
        elif 150 <= score < 200:
            length = 30 + ex_len + temp_len
            level = 'level 5'
        else:
            length = 20 + ex_len + temp_len
            level = 'final level'
    if x > width - r or x < r:
        vx = -vx

    circle(x, y, r, thickness=-1)

    if y > height - r:
        vx = vy = 0
        text = 'You Lose!'
        etext(text, int(width / 2 - len(text) * 8), int(height / 2 - 100), color=(0, 0, 255))
        text = 'Your Score is ' + str(score)
        etext(text, int(width / 2 - len(text) * 8), int(height / 2), color=(0, 0, 255))
        text = 'Press r to Restart'
        etext(text, int(width / 2 - len(text) * 8), int(height / 2 + 100), color=(0, 0, 255))

    if dist - r - r < y < dist - r:
        if f1 > 0:
            f2 = mouse_x
            # print('f2:', f2)
            if f2 - f1 == 0:
                pass
            elif f2 - f1 > 0:
                vx = vx - 1
                # print('vx:', vx)
            else:
                vx = vx + 1
            f1 = 0
    elif mouse_x - length - r <= x <= mouse_x + length + r and dist - r < y < dist - r + r:
        f1 = mouse_x
        vy = -vy

    if lucky_show:
        if lucky_box[0] - r < x < lucky_box[2] + r and lucky_box[1] - r < y < lucky_box[3] + r:
            lucky_show = False
            vy = 1
            luck = randint(0, 3)
            if luck == 0:
                score += 10
                ex_len += 10
            elif luck == 1:
                ex_len += 20
            elif luck == 2:
                score += 20
            else:
                temp_len = 200
        else:
            rectangle(lucky_box[0], lucky_box[1], lucky_box[2], lucky_box[3], color=(150, 25, 17), thickness=-1)
            etext("L", int(lucky_box[0]), int(lucky_box[1] + box_size), fontScale=1.0, color=(0, 255, 255))
    rectangle(mouse_x - length, dist, mouse_x + length, dist + 10, thickness=-1)
    etext("score :" + str(score), 30, 30, color=(0, 64, 250))
    etext(level, 30, 60, fontScale=0.7, color=(220, 64, 16))
    etext("bonus :" + str(abs(vx * vy)), 30, 80, fontScale=0.5, color=(200, 164, 16))
    etext("length :" + str(length), 30, 100, fontScale=0.5, color=(200, 164, 16))
    etext("Mago Python Class", width - 400, height - 30)
    key = show(1)
    if key == ord('r'):
        x = 10
        y = 10
        vx = randint(1, 3)
        vy = randint(1, 2)
        score = 0
        length = 100
        lucky_show = False
    elif key == ord('q'):
        break
