from mago_class_lib import *
from random import randint

width = 800
height = 300


class Bird:
    def __init__(self, x=100, y=10, r=10, color=(0, 0, 255), fall_speed=1, jump_speed=50):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__color = color
        self.__fall_speed = fall_speed
        self.__jump_speed = jump_speed

    def draw(self):
        self.__y += self.__fall_speed
        global height
        if self.__y > height - self.__r:
            self.__y = height - self.__r
        circle(self.__x, self.__y, self.__r, self.__color, -1)

    def jump(self):
        self.__y -= self.__jump_speed
        if self.__y < self.__r:
            self.__y = self.__r

    def dead(self, wall_pos, wall_gap):
        if wall_pos >= 0:
            if wall_pos + self.__r <= self.__y <= wall_pos + wall_gap - self.__r:
                return False
            else:
                return True


class Wall:
    def __init__(self, gap=100, length=50, wall_speed=1, wall_dist=200, collision_point=110, color=(255, 0, 0)):
        global width, height
        self.__color = color
        self.__collision_point = collision_point
        self.__wall_dist = wall_dist
        self.__wall_speed = wall_speed
        self.__length = length
        self.__gap = gap
        self.__height = height
        self.__width = width
        self.__x = width
        self.__y = 0
        self.__cur_pos = -1
        self.__pos_list = []
        self.__new_wall()
        self.__score = 0
        self.__temp = self.__cur_pos
        self.__level = 0

    def __random_wall(self):
        return randint(0, self.__height - self.__gap)

    def __new_wall(self):
        self.__pos_list.append(self.__random_wall())

    def draw(self):
        self.__x -= self.__wall_speed
        if self.__x % self.__wall_dist == 0:
            self.__new_wall()
        if self.__x <= -self.__length:
            self.__pos_list.pop(0)
            self.__x = self.__wall_dist - self.__length

        # print(self.pos_list)
        for i in range(len(self.__pos_list)):
            rectangle(self.__x + self.__wall_dist * i, 0, self.__x + self.__length + self.__wall_dist * i,
                      self.__pos_list[i], color=self.__color, thickness=-1)
            rectangle(self.__x + self.__wall_dist * i, self.__pos_list[i] + self.__gap,
                      self.__x + self.__length + self.__wall_dist * i, self.__height, color=self.__color, thickness=-1)
            if self.__collision_point - self.__length <= self.__x + self.__wall_dist * i <= self.__collision_point:
                self.__cur_pos = self.__pos_list[i]
            elif self.__x + self.__wall_dist * i < self.__collision_point - self.__length:
                self.__cur_pos = -1
        return self.__cur_pos

    def get_score(self):
        if self.__cur_pos < self.__temp:
            self.__score += 5
        self.__temp = self.__cur_pos
        return self.__score

    def get_level(self):
        if self.__score < 10:
            self.__level = 1
            self.__gap = 150
        elif self.__score < 20:
            self.__level = 2
            self.__gap = 140
        elif self.__score < 30:
            self.__level = 3
            self.__gap = 130
        elif self.__score < 40:
            self.__level = 4
            self.__gap = 120
        elif self.__score < 50:
            self.__level = 5
            self.__gap = 110
        elif self.__score < 60:
            self.__level = 6
            self.__gap = 100
        elif self.__score < 70:
            self.__level = 7
            self.__wall_speed = 2
        elif self.__score < 80:
            self.__level = 8
            self.__wall_dist = 190
        elif self.__score < 90:
            self.__level = 9
            self.__wall_dist = 180
        elif self.__score < 100:
            self.__level = 10
            self.__wall_dist = 170
        elif self.__score < 110:
            self.__level = 11
            self.__wall_dist = 160
        elif self.__score < 120:
            self.__level = 12
            self.__wall_dist = 150
        elif self.__score < 130:
            self.__level = 13
            self.__length = 60
        elif self.__score < 140:
            self.__level = 14
            self.__length = 70
        elif self.__score < 150:
            self.__level = 15
            self.__length = 80
        return self.__level

    def restart(self):
        self.__x = self.__width
        self.__cur_pos = -1
        self.__score = 0


start = 0
bird_x = 100
bird_y = 10
bird_r = 10
bird_color = (0, 0, 255)
bird_fall = 1
bird_jump = 50
bird = Bird(x=bird_x, y=bird_y, r=bird_r, color=bird_color, fall_speed=bird_fall, jump_speed=bird_jump)

gap = 150
length = 50
wall_speed = 1
wall_dist = 200
wall = Wall(gap=gap, length=length, wall_speed=wall_speed, wall_dist=wall_dist,
            collision_point=bird_x + bird_r)

temp = -1
score = 0
level = 0
window()
while True:
    canvas(width, height)
    bird.draw()
    pos = wall.draw()
    score = wall.get_score()
    level = wall.get_level()
    if bird.dead(wall_pos=pos, wall_gap=gap):
        text = 'You Lose!'
        etext(text, int(width / 2 - len(text) * 8), int(height / 2 - 100), color=(0, 0, 255))
        text = 'Your Score is ' + str(score)
        etext(text, int(width / 2 - len(text) * 8), int(height / 2), color=(0, 0, 255))
        text = 'Press r to Restart'
        etext(text, int(width / 2 - len(text) * 8), int(height / 2 + 100), color=(0, 0, 255))
        start = 0
    etext("score :" + str(score), width - 180, 30, color=(0, 102, 255))
    etext("level :" + str(level), width - 180, 60, fontScale=0.7, color=(102, 102, 255))
    etext("Mago Python Class", width - 350, height - 10)
    key = show(start)
    if key == ord('r'):
        start = 10
        wall.restart()
        score = 0
    if key == ord('j'):
        bird.jump()
    if key == ord('q'):
        break

