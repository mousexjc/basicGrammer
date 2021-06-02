from mago_class_lib import *
from random import randint


def tank(tank, color=(0, 0, 0)):
    circle(tank[0], tank[1], tank[2], color=color, thickness=-1)
    line(tank[0] + tank[2] * tank[3][0], tank[1] + tank[2] * tank[3][1],
         tank[0] + tank[2] * 2 * tank[3][0], tank[1] + tank[2] * 2 * tank[3][1],
         thickness=2)


def wall(tank):
    global width
    global height
    if tank[0] > width - 2 * tank[2]:
        tank[0] = width - 2 * tank[2]
    if tank[0] < 2 * tank[2]:
        tank[0] = 2 * tank[2]
    if tank[1] > height - 2 * tank[2]:
        tank[1] = height - 2 * tank[2]
    if tank[1] < 2 * tank[2]:
        tank[1] = 2 * tank[2]


def fire(tank):
    bullets.append([tank[0] + tank[2] * 2 * tank[3][0],
                    tank[1] + tank[2] * 2 * tank[3][1],
                    tank[3], bullet_r,
                    bullet_v])


def enemy_fire(tank):
    enemy_bullets.append([tank[0] + tank[2] * 2 * tank[3][0],
                          tank[1] + tank[2] * 2 * tank[3][1],
                          tank[3], bullet_r,
                          bullet_v])


def is_bullet(bullet):
    global width
    global height
    if bullet[0] > width or bullet[1] > height or bullet[0] < 0 or bullet[1] < 0:
        return False
    else:
        return True


def new_enemy_tank():
    enemy_tanks.append([randint(tank_r, width), randint(tank_r, height), tank_r, dirs[randint(0, 3)], enemy_tank_v])


dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
width = 800
height = 600
tank_x = 250
tank_y = 250
tank_r = 10
tank_dir = dirs[0]
tank_v = 10
my_tank = [tank_x, tank_y, tank_r, tank_dir, tank_v]

bullet_x = 0
bullet_y = 0
bullet_r = 2
bullet_v = 1
bullets = []

enemy_tank_v = 1
enemy_tanks = []
enemy_bullets = []
for i in range(0, 5):
    enemy_tanks.append([randint(tank_r, width), randint(tank_r, height), tank_r, dirs[randint(0, 3)], enemy_tank_v])

score = 0
window()
while True:
    canvas(width, height)
    tank(my_tank, color=(0, 0, 255))
    wall(my_tank)

    for bullet in bullets:
        bullet[0] += bullet[2][0] * bullet[4]
        bullet[1] += bullet[2][1] * bullet[4]
        circle(bullet[0], bullet[1], bullet[3], thickness=-1)
        if is_bullet(bullet):
            pass
        else:
            bullets.remove(bullet)
        for eb in enemy_bullets:
            if eb == bullet:
                bullets.remove(bullet)
                enemy_bullets.remove(eb)

    for bullet in enemy_bullets:
        bullet[0] += bullet[2][0] * bullet[4]
        bullet[1] += bullet[2][1] * bullet[4]
        circle(bullet[0], bullet[1], bullet[3], thickness=-1)
        if is_bullet(bullet):
            pass
        else:
            enemy_bullets.remove(bullet)
        if my_tank[0] - my_tank[2] < bullet[0] < my_tank[0] + my_tank[2] and \
                my_tank[1] - my_tank[2] < bullet[1] < my_tank[1] + my_tank[2]:
            enemy_bullets.remove(bullet)
            print('u died!')

    # if step < 0:
    #     dir = dirs[randint(0, 3)]
    #     step = 200
    # else:
    #     step -= 1
    # dir = dirs[randint(0, 3)]

    for enemy_tank in enemy_tanks:
        m = randint(0, 1000)
        if m < 10:
            enemy_tank[3] = dirs[randint(0, 3)]
        elif m > 990:
            enemy_fire(enemy_tank)
        else:
            pass
        enemy_tank[0] += int(enemy_tank[3][0] * enemy_tank[4])
        enemy_tank[1] += int(enemy_tank[3][1] * enemy_tank[4])
        tank(enemy_tank)
        wall(enemy_tank)
        for bullet in bullets:
            if enemy_tank[0] - enemy_tank[2] < bullet[0] < enemy_tank[0] + enemy_tank[2] and \
                    enemy_tank[1] - enemy_tank[2] < bullet[1] < enemy_tank[1] + enemy_tank[2]:
                enemy_tanks.remove(enemy_tank)
                bullets.remove(bullet)
                score += 1

    etext("score :" + str(score), 30, 30, color=(0, 64, 250))
    etext("Mago Python Class", width - 400, height - 30)
    key = show(1)

    if key == ord('w'):
        my_tank[1] -= my_tank[4]
        my_tank[3] = dirs[0]
    elif key == ord('s'):
        my_tank[1] += my_tank[4]
        my_tank[3] = dirs[1]
    elif key == ord('a'):
        my_tank[0] -= my_tank[4]
        my_tank[3] = dirs[2]
    elif key == ord('d'):
        my_tank[0] += my_tank[4]
        my_tank[3] = dirs[3]
    if key == ord('g'):
        fire(my_tank)
        print(bullets)
    if key == ord('t'):
        new_enemy_tank()
