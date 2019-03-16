# геометрические признаки
import sys


def square(labels, labels_array):
    squares = dict.fromkeys(labels_array, 0)
    for i in range(len(labels)):
        for j in range(len(labels[i])):
            if labels[i][j] != 0:
                s = squares.get(labels[i][j])
                s += 1
                squares.update({labels[i][j]: s})
    return squares


def perimeter(labels, labels_array):
    perimeters = dict.fromkeys(labels_array, 0)
    for i in range(len(labels)):
        for j in range(len(labels[i])):
            if labels[i][j] != 0:
                p = perimeters.get(labels[i][j])
                if labels[i - 1][j - 1] == 0 \
                        or labels[i + 1][j - 1] == 0 \
                        or labels[i - 1][j + 1] == 0 \
                        or labels[i + 1][j + 1] == 0:
                    p += 1
                    perimeters.update({labels[i][j]: p})
    return perimeters


def compactness(squares, perimeters):
    keys = squares.keys()
    compactness_dict = dict.fromkeys(keys, 0)
    for key in compactness_dict:
        s = squares.get(key)
        p = perimeters.get(key)
        c = (p ** 2) / s
        compactness_dict.update({key: c})
    return compactness_dict


# mass_centers = {label: [xmin, xmax, ymin, ymax]}
def mass_center(labels, labels_array, squares):
    mass_centers = dict.fromkeys(labels_array)
    for key in mass_centers:
        mass_centers.update({key: [len(labels), 0, len(labels[0]), 0]})
    for x in range(len(labels)):
        for y in range(len(labels[x])):
            if labels[x][y] != 0:
                val = mass_centers.get(labels[x][y])
                if x < val[0]:
                    val[0] = x
                    mass_centers.update({labels[x][y]: val})
                if x > val[1]:
                    val[1] = x
                    mass_centers.update({labels[x][y]: val})
                if y < val[2]:
                    val[2] = y
                    mass_centers.update({labels[x][y]: val})
                if y > val[3]:
                    val[3] = y
                    mass_centers.update({labels[x][y]: val})

    new_centers = dict.fromkeys(labels_array, [0, 0])
    for key in mass_centers:
        x = (mass_centers.get(key)[1] - mass_centers.get(key)[0]) / squares.get(key)
        y = (mass_centers.get(key)[3] - mass_centers.get(key)[2]) / squares.get(key)
        new_centers.update({key: [x, y]})
    return new_centers


def elongation(labels, labels_array):
    elongations = dict.fromkeys(labels_array)
    for key in elongations:
        elongations.update({key: [len(labels), 0, len(labels[0]), 0]})
    for x in range(len(labels)):
        for y in range(len(labels[x])):
            if labels[x][y] != 0:
                val = elongations.get(labels[x][y])
                if x < elongations.get(labels[x][y])[0]:
                    val[0] = x
                    elongations.update({labels[x][y]: val})
                if x > elongations.get(labels[x][y])[1]:
                    val[1] = x
                    elongations.update({labels[x][y]: val})
                if y < elongations.get(labels[x][y])[2]:
                    val[2] = y
                    elongations.update({labels[x][y]: val})
                if y > elongations.get(labels[x][y])[3]:
                    val[3] = y
                    elongations.update({labels[x][y]: val})

    new_elongations = dict.fromkeys(labels_array, [0, 0])
    for key in elongations:
        dx = elongations.get(key)[1] - elongations.get(key)[0]
        dy = elongations.get(key)[3] - elongations.get(key)[2]
        new_elongations.update({key: [dx, dy]})
    return new_elongations
