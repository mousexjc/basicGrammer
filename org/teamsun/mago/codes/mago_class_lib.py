import cv2
import numpy as np
from math import sqrt
from PIL import Image, ImageDraw, ImageFont
import time

g_image = np.ndarray(())


# mouse_x = 0
# mouse_y = 0


# def get_mouse(event, x, y, flags, param):
#     global mouse_x
#     global mouse_y
#     mouse_x = x
#     mouse_y = y


# cv2.namedWindow('Mago Class')
# cv2.setMouseCallback('Mago Class', get_mouse)


def window():
    cv2.namedWindow('Mago Class')


def canvas(width=800, height=600):
    global g_image
    g_image = np.zeros((height, width, 3), dtype=np.uint8)
    g_image.fill(255)


def show(time=1):
    global g_image
    cv2.imshow('Mago Class', g_image)
    key = cv2.waitKey(time)
    return key


def circle(x, y, r, color=(0, 0, 0), thickness=1):
    global g_image
    cv2.circle(g_image, (x, y), r, color=color, thickness=thickness)


def line(x1, y1, x2, y2, color=(0, 0, 0), thickness=1):
    global g_image
    cv2.line(g_image, (x1, y1), (x2, y2), color=color, thickness=thickness)


def rectangle(x1, y1, x2, y2, color=(0, 0, 0), thickness=1):
    global g_image
    cv2.rectangle(g_image, (x1, y1), (x2, y2), color=color, thickness=thickness)


def etext(text, left, top, fontScale=1.0, color=(0, 255, 0), thickness=2):
    global g_image
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(g_image, text, (left, top), font, fontScale=fontScale, color=color, thickness=thickness)


def text(text, left, top, textColor=(0, 255, 0), textSize=20):
    global g_image
    if isinstance(g_image, np.ndarray):  # 判断是否OpenCV图片类型
        g_image = Image.fromarray(cv2.cvtColor(g_image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(g_image)
    font_text = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=font_text)
    g_image = cv2.cvtColor(np.asarray(g_image), cv2.COLOR_RGB2BGR)


def mouse(on_mouse):
    cv2.setMouseCallback('Mago Class', on_mouse)


def sleep(ms):
    time.sleep(ms)


def image(path, x, y):
    global g_image
    img = cv2.imread(path)
    h, w = img.shape[:2]
    if 0 < x < g_image.shape[1] - w and 0 < y < g_image.shape[0] - h:
        g_image[y: y + h, x: x + w] = img


def image_png(path, x, y, threshold, type=0):
    global g_image
    thresh_type = cv2.THRESH_BINARY
    img = cv2.imread(path)
    rows, cols, channels = img.shape
    # print(rows, cols)
    # roi = g_image[y:y+rows, x:x+cols]
    if 0 < x < g_image.shape[1] - cols and 0 < y < g_image.shape[0] - rows:
        roi = g_image[y:y+rows, x:x+cols]

        # Now create a mask of logo and create its inverse mask also
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if type < 0:
            thresh_type = cv2.THRESH_BINARY_INV
        else:
            thresh_type = cv2.THRESH_BINARY
        ret, mask = cv2.threshold(img2gray, threshold, 255, thresh_type)  # 这个254很重要
        mask_inv = cv2.bitwise_not(mask)
        # cv2.imshow('mask', mask_inv)
        # Now black-out the area of logo in ROI
        img1_bg = cv2.bitwise_and(roi, roi, mask=mask)  # 这里是mask,我参考的博文写反了,我改正了,费了不小劲

        # Take only region of logo from logo image.
        img2_fg = cv2.bitwise_and(img, img, mask=mask_inv)  # 这里才是mask_inv

        # Put logo in ROI and modify the main image
        dst = cv2.add(img1_bg, img2_fg)
        g_image[y:y+rows, x:x+cols] = dst



if __name__ == '__main__':
    # window()
    # mouse()
    # width = 200
    # height = 200
    # x1 = 100
    # y1 = 100
    # r1 = 80
    # r2 = 40
    # while True:
    #     canvas(width, height)
    #     # image("images/wz.png")
    #     circle(x1, y1, r1)
    #     a = (r1 - r2) / sqrt(2)
    #     rate_x = 2 * a / width
    #     rate_y = 2 * a / height
    #     dist_x = x1 - a
    #     dist_y = y1 - a
    #     x2 = int(dist_x + rate_x * mouse_x)
    #     y2 = int(dist_y + rate_y * mouse_y)
    #     circle(x2, y2, r2, -1)
    #     show()

    image("image/wz_16.png", 50, 50)
