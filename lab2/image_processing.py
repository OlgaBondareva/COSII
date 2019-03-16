import copy
import math

from PIL import Image, ImageDraw


def grayscale(image):
    draw = ImageDraw.Draw(image)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x, y))
            Y = int(0.3 * r + 0.59 * g + 0.11 * b)
            draw.point((x, y), (Y, Y, Y))
    del draw
    return image


# H1
#  1  0 -1
#  2  0 -2
#  1  0 -1
# H2
# -1 -2 -1
#  0  0  0
#  1  2  1
# S = sqrt(H1*H1 + H2*H2)
def sobel_operator(image):
    draw = ImageDraw.Draw(image)
    array = []
    for x in range(1, image.size[0] - 1):
        for y in range(1, image.size[1] - 1):
            # H1
            h11, g, b = image.getpixel((x - 1, y - 1))
            h31, g, b = image.getpixel((x + 1, y - 1))
            h41, g, b = image.getpixel((x - 1, y))
            h61, g, b = image.getpixel((x + 1, y))
            h71, g, b = image.getpixel((x - 1, y + 1))
            h91, g, b = image.getpixel((x + 1, y + 1))
            h1 = h11 - h31 + 2 * h41 - 2 * h61 + h71 - h91
            # H2
            h12, g, b = image.getpixel((x - 1, y - 1))
            h22, g, b = image.getpixel((x + 1, y - 1))
            h32, g, b = image.getpixel((x - 1, y))
            h72, g, b = image.getpixel((x + 1, y))
            h82, g, b = image.getpixel((x - 1, y + 1))
            h92, g, b = image.getpixel((x + 1, y + 1))
            h2 = -h12 - 2 * h22 - h32 + h72 + 2 * h82 + h92

            S = math.sqrt(h1 ** 2 + h2 ** 2)
            array.append(S)
    del draw
    return array


# бинаризация методом k-средних
def binarization(img):
    sobel_array = sobel_operator(img)
    B = []
    T0 = 127
    for x in range(len(sobel_array)):
        if sobel_array[x] >= T0:
            B.append(1)
        else:
            B.append(0)
    H = []
    L = []
    for x in range(1, img.size[0] - 1):
        for y in range(1, img.size[1] - 1):
            r, g, b = img.getpixel((x, y))
            if B[x - 1 + y - 1] == 1:
                H.append(r + g + b)
            else:
                L.append(r + g + b)
    T = 0.5 * ((sum(H) + sum(L)) / ((img.size[0] - 2) * (img.size[1] - 2)))
    gray = grayscale(img)
    draw = ImageDraw.Draw(gray)
    for x in range(gray.size[0]):
        for y in range(gray.size[1]):
            r, g, b = gray.getpixel((x, y))
            if r >= T:
                r = 255
            else:
                r = 0
            draw.point((x, y), (r, r, r))
    del draw
    return gray


# 0.1 from
# 1 1 1
# 1 2 1
# 1 1 1
def low_filter(image):
    draw = ImageDraw.Draw(image)
    for x in range(1, image.size[0] - 1):
        for y in range(1, image.size[1] - 1):
            r1, g1, b1 = image.getpixel((x - 1, y - 1))
            r2, g2, b2 = image.getpixel((x, y - 1))
            r3, g3, b3 = image.getpixel((x + 1, y - 1))
            r4, g4, b4 = image.getpixel((x - 1, y))
            r5, g5, b5 = image.getpixel((x, y))
            r6, g6, b6 = image.getpixel((x + 1, y))
            r7, g7, b7 = image.getpixel((x - 1, y + 1))
            r8, g8, b8 = image.getpixel((x, y + 1))
            r9, g9, b9 = image.getpixel((x + 1, y + 1))
            r5 = int(0.1 * (2 * r5 + r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9))
            g5 = int(0.1 * (2 * g5 + g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9))
            b5 = int(0.1 * (2 * b5 + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9))
            draw.point((x, y), (r5, g5, b5))
    del draw
    return image


def median_filter(image):
    draw = ImageDraw.Draw(image)
    for x in range(1, image.size[0] - 1):
        for y in range(1, image.size[1] - 1):
            r1, g1, b1 = image.getpixel((x - 1, y - 1))
            r2, g2, b2 = image.getpixel((x, y - 1))
            r3, g3, b3 = image.getpixel((x + 1, y - 1))
            r4, g4, b4 = image.getpixel((x - 1, y))
            r5, g5, b5 = image.getpixel((x, y))
            r6, g6, b6 = image.getpixel((x + 1, y))
            r7, g7, b7 = image.getpixel((x - 1, y + 1))
            r8, g8, b8 = image.getpixel((x, y + 1))
            r9, g9, b9 = image.getpixel((x + 1, y + 1))
            r = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
            g = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
            b = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
            r.sort()
            g.sort()
            b.sort()
            r5 = r[4]
            g5 = g[4]
            b5 = b[4]
            draw.point((x, y), (r5, g5, b5))
    del draw
    return image


def clipping(image):
    image1 = Image.new("RGB", (image.size[0], image.size[1]))
    draw = ImageDraw.Draw(image1)
    for x in range(1, image.size[0] - 1):
        for y in range(1, image.size[1] - 1):
            r, g, b = image.getpixel((x, y))
            draw.point((x - 1, y - 1), (r, g, b))
    return image1


def erosion(img, size):
    border = math.floor(size / 2)
    new = copy.deepcopy(img)
    pixels = []
    for i in range(size ** 2):
        pixels.append(0)
    draw = ImageDraw.Draw(new)
    for x in range(img.size[0] - size):
        for y in range(img.size[1] - size):
            pi = 0
            for i in range(x, x + size):
                for j in range(y, y + size):
                    r, g, b = img.getpixel((i, j))
                    pixels[pi] = r
                    pi += 1
            value = min(pixels)
            draw.point((x + border, y + border), (value, value, value))
    del draw
    return new


def delation(img, size):
    border = math.floor(size / 2)
    new = copy.deepcopy(img)
    pixels = []
    for i in range(size ** 2):
        pixels.append(0)
    draw = ImageDraw.Draw(new)
    for x in range(img.size[0] - size):
        for y in range(img.size[1] - size):
            pi = 0
            for i in range(x, x + size):
                for j in range(y, y + size):
                    r, g, b = img.getpixel((i, j))
                    pixels[pi] = r
                    pi += 1
            value = max(pixels)
            draw.point((x + border, y + border), (value, value, value))
    del draw
    return new


# размыкание
def opening(img, size=3):
    open_image = erosion(img, size)
    open_image = delation(open_image, size)
    return open_image
