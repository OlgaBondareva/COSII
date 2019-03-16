# рекурсивный алгоритм
def labeling(labels, img, q, fl):
    L = 1
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            q, fl = fill(img, labels, x, y, L, q, fl)
            L += 1
    return q, labels


def fill(img, labels, x, y, L, q, fl):
    r, g, b = img.getpixel((x, y))
    if (labels[x][y] == 0) and (r == 255):
        labels[x][y] = L
        if not fl:
            fl = True
            q.append(L)
        if x > 0:
            fill(img, labels, x - 1, y, L, q, fl)
        if x < (img.size[0] - 1):
            fill(img, labels, x + 1, y, L, q, fl)
        if y > 0:
            fill(img, labels, x, y - 1, L, q, fl)
        if y < (img.size[1] - 1):
            fill(img, labels, x, y + 1, L, q, fl)
    elif r == 255:
        fl = False
    return q, fl
