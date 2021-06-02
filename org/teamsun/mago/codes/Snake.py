from mago_class_lib import *
import random
import time


def isover(head):
    if snake.count(head) > 1:  # 碰到自己身体
        return True
    if (head[0] == width / 10) or (head[1] == height / 10) or (head[0] == -1) or (head[1] == -1):  # 碰到墙
        return True
    return False


def food_draw(food_x, food_y, food_size=10):
    rectangle(food_x * 10, food_y * 10, food_x * 10 + food_size, food_y * 10 + food_size, (108, 96, 244), -1)


def food_pos(width=500, height=500, food_size=10):
    return random.randint(0, int(width / food_size - 1)), random.randint(0, int(height / food_size - 1))


def snake_draw(snake_pos):
    for sk in snake_pos:
        # print(sk[1])
        rectangle(sk[0] * 10, sk[1] * 10, sk[0] * 10 + 10, sk[1] * 10 + 10, (173, 202, 25), -1)


width = 500
height = 500
food_size = 10
snake_speed = 0.1
pos = {
    'UP': (0, -1),
    'DOWN': (0, +1),
    'LEFT': (-1, 0),
    'RIGHT': (+1, 0),
}
current = 'DOWN'
snake = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]  # ex: [[1,1],[1,2],[1,3]]  [y,x]
head = snake[-1]
text_size = 20

window()
canvas(width, height)
food_x, food_y = food_pos(width, height, food_size)

while True:
    canvas(width, height)
    text('码高Python趣味编程', width - 300, height - 30, (252, 85, 49), 30)
    if isover(head) is False:
        text('得分: ' + str(len(snake) - 5), 10, 10, (1, 176, 241))
        food_draw(food_x, food_y, food_size)
        head = [head[0] + pos[current][0], head[1] + pos[current][1]]
        snake.append(head)
        if head[0] == food_x and head[1] == food_y:
            food_x, food_y = food_pos(width, height, food_size)
            snake_speed = snake_speed - 0.01
        else:
            snake.pop(0)
        snake_draw(snake)
        time.sleep(snake_speed)
        key = show(1)
        if key == ord('w') and current != 'DOWN':
            current = 'UP'
        elif key == ord('s') and current != 'UP':
            current = 'DOWN'
        elif key == ord('a') and current != 'RIGHT':
            current = 'LEFT'
        elif key == ord('d') and current != 'LEFT':
            current = 'RIGHT'
    else:
        text('游戏结束 !', 10, int(height / 2 - text_size * 2), (255, 0, 0))
        text('你的得分是 ' + str(len(snake) - 5), 10, int(height / 2), (255, 0, 0))
        text('按 "r" 键重新开始!', 10, int(height / 2 + text_size * 2), (255, 0, 0))
    key = show(1)
    if key == ord('r'):
        current = 'DOWN'
        snake = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
        head = snake[-1]
        snake_speed = 0.1
    elif key == ord('q'):
        break
