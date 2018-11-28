import matplotlib.pyplot as plot
from PIL import Image, ImageDraw


def grayscale(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    array = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x, y))
            Y = int(0.3 * r + 0.59 * g + 0.11 * b)
            draw.point((x, y), (Y, Y, Y))
            array.append(Y)
    del draw
    return array, image


def negative(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    ar_r = ar_g = ar_b = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x, y))
            ar_r.append(r)
            ar_g.append(g)
            ar_b.append(b)
            draw.point((x, y), (255 - r, 255 - g, 255 - b))
    del draw
    return ar_r, ar_g, ar_b, image


def solarization(name):
    image = Image.open(name)
    k = float(input("Введите параемтр k для соляризации: "))
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    ar_r = ar_g = ar_b = []
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            ar_r.append(r)
            ar_g.append(g)
            ar_b.append(b)
    max_r = max(ar_r)
    max_g = max(ar_g)
    max_b = max(ar_b)
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = int(k * r * (max_r - r))
            g = int(k * g * (max_g - g))
            b = int(k * b * (max_b - b))
            ar_r[x + y] = r
            ar_g[x + y] = g
            ar_b[x + y] = b
            draw.point((x, y), (r, g, b))
    del draw
    return ar_r, ar_g, ar_b, image


def normalize(pixel):
    if pixel > 255:
        pixel -= 255
    if pixel < 0:
        pixel *= -1
    return pixel


# 0  1  0
# 1  0 -1
# 0 -1  0
def stamping(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    ar_r = ar_g = ar_b = []
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r2, g2, b2 = image.getpixel((x, y - 1))
            r4, g4, b4 = image.getpixel((x - 1, y))
            r6, g6, b6 = image.getpixel((x + 1, y))
            r8, g8, b8 = image.getpixel((x, y + 1))
            r5 = r2 + r4 - r6 - r8
            g5 = g2 + g4 - g6 - g8
            b5 = b2 + b4 - b6 - b8
            r5 = normalize(r5)
            g5 = normalize(g5)
            b5 = normalize(b5)
            ar_r.append(r5)
            ar_g.append(g5)
            ar_b.append(b5)
            draw.point((x, y), (r5, g5, b5))
    del draw
    return ar_r, ar_g, ar_b, image


def binary_normalize(pixel):
    if pixel > 255:
        pixel = 255
    if pixel < 0:
        pixel = 0
    return pixel


# 0 2
# 3 1
def binary_grayscale(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    ar_r = ar_g = ar_b = []
    for x in range(0, width - 1):
        for y in range(0, height - 1):
            r2, g2, b2 = image.getpixel((x + 1, y))
            r3, g3, b3 = image.getpixel((x, y + 1))
            r4, g4, b4 = image.getpixel((x + 1, y + 1))
            r1 = 2 * r2 + 3 * r3 + r4
            g1 = 2 * g2 + 3 * g3 + g4
            b1 = 2 * b2 + 3 * b3 + b4
            binary_normalize(r1)
            binary_normalize(g1)
            binary_normalize(g1)
            ar_r.append(r1)
            ar_g.append(g1)
            ar_b.append(b1)
            draw.point((x, y), (r1, g1, b1))
    del draw
    return ar_r, ar_g, ar_b, image


def lap_norm(pix):
    if pix < 0:
        pix *= -1
    return pix


#  0  1  0
#  1 -4  1
#  0  1  0
def laplas(name):
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    ar_r = ar_g = ar_b = []
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r2, g2, b2 = image.getpixel((x, y - 1))
            r4, g4, b4 = image.getpixel((x - 1, y))
            r5, g5, b5 = image.getpixel((x, y))
            r6, g6, b6 = image.getpixel((x + 1, y))
            r8, g8, b8 = image.getpixel((x, y + 1))
            r5 = r5 * (-4) + r2 + r4 + r6 + r8
            g5 = g5 * (-4) + g2 + g4 + g6 + g8
            b5 = b5 * (-4) + b2 + b4 + b6 + b8
            r5 = lap_norm(r5)
            g5 = lap_norm(g5)
            b5 = lap_norm(b5)
            ar_r.append(r5)
            ar_g.append(g5)
            ar_b.append(b5)
            draw.point((x, y), (r5, g5, b5))
    del draw
    return ar_r, ar_g, ar_b, image


file = 'lenna.jpg'
# file = "mid-autumn-festival-2018-japan.bmp"
image = Image.open(file)
image.show()

# grayscale_array, image_grayscale = grayscale(file)
# image_grayscale.show()

# negative_array_r, negative_array_g, negative_array_b, image_negative = negative(file)
# image_negative.show()
#
# solar_array_r, solar_array_g, solar_array_b, image_solar = solarization(file)
# image_solar.show()
#
# stamp_array_r, stamp_array_g, stamp_array_b, image_stapm = stamping(file)
# image_stapm.show()
#
# binary_g_r, binary_g_g, binary_g_b, image_binary_g = binary_grayscale(file)
# image_binary_g.show()

l_r, l_g, l_b, i_l = laplas(file)
i_l.show()

# grayscale bar chart
# plot.subplot(3, 6, 1)
# plot.hist(grayscale_array, color='k')
# plot.title("Grayscale")
# negative bar chart
# plot.subplot(3, 6, 4)
# plot.hist(negative_array_r, color='r')
# plot.title("Negative Red")
# plot.subplot(3, 6, 5)
# plot.hist(negative_array_g, color='g')
# plot.title("Negative Green")
# plot.subplot(3, 6, 6)
# plot.hist(negative_array_b, color='b')
# plot.title("Negative Blue")
# # solar bar chart
# plot.subplot(3, 6, 7)
# plot.hist(solar_array_r, color='r')
# plot.title("Solar Red")
# plot.subplot(3, 6, 8)
# plot.hist(solar_array_g, color='g')
# plot.title("Solar Green")
# plot.subplot(3, 6, 9)
# plot.hist(solar_array_b, color='b')
# plot.title("Solar Blue")
# # stamping filter
# plot.subplot(3, 6, 10)
# plot.hist(stamp_array_r, color='r')
# plot.title("Stamp filter Red")
# plot.subplot(3, 6, 11)
# plot.hist(stamp_array_g, color='g')
# plot.title("Stamp filter Green")
# plot.subplot(3, 6, 12)
# plot.hist(stamp_array_b, color='b')
# plot.title("Stamp filter Blue")
# # binary grayscale filter
# plot.subplot(3, 6, 13)
# plot.hist(binary_g_r, color='r')
# plot.title("BG filter Red")
# plot.subplot(3, 6, 14)
# plot.hist(binary_g_g, color='g')
# plot.title("BG filter Green")
# plot.subplot(3, 6, 15)
# plot.hist(binary_g_b, color='b')
# plot.title("BG filter Blue")

# laplas
plot.subplot(1, 3, 1)
plot.hist(l_r, color='r')
plot.title("Red")
plot.subplot(1, 3, 2)
plot.hist(l_g, color='g')
plot.title("Green")
plot.subplot(1, 3, 3)
plot.hist(l_b, color='b')
plot.title("Blue")

plot.show()
# image_grayscale.save("grayscale.bmp")
# image_negative.save("negative.bmp")
# image_solar.save("solar.bmp")
# image_stapm.save("stamping.bmp")
# image_binary_g.save("binary_grayscale.bmp")
