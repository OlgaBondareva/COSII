# рекурсивный алгоритм
import sys

L = 0
flag = False


def labeling(img, tags):
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            tags = fill(img, tags, x, y, L)
            flag = False
    return tags


def fill(img, tags, x, y, L):
    r, g, b = img.getpixel((x, y))
    if (tags[x][y] == 0) and (r == 255):
        if not flag:
            flag = True
            L += 1
        tags[x][y] = L
        if x > 0:
            fill(img, tags, x - 1, y, L)
        if x < (img.size[0] - 1):
            fill(img, tags, x + 1, y, L)
        if y > 0:
            fill(img, tags, x, y - 1, L)
        if y < (img.size[1] - 1):
            fill(img, tags, x, y + 1, L)
    return tags


def recursive_algorithm(img):
    # labels должна быть обнулена
    n = img.size[0]
    m = img.size[1]
    labels = [0] * n
    for i in range(n):
        labels[i] = [0] * m

    sys.setrecursionlimit(5000)
    lbls = labeling(img, labels)
    return lbls
