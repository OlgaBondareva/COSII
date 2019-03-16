import sys

from PIL import Image, ImageDraw

from geometric_features import square, perimeter, compactness, mass_center, elongation
from image_processing import low_filter, binarization, median_filter, clipping, opening
from recursive_algorithm import labeling

# file = 'easy/P0001460.jpg'
file = 'hard/P0001464.jpg'
image = Image.open(file)
image.show()
image = low_filter(image)

image = binarization(image)
image = median_filter(image)
image = clipping(image)
image = opening(image, 5)
image.save('binary.png')
image.show()

sys.setrecursionlimit(5000)

# labels должна быть обнулена
n = image.size[0]
m = image.size[1]
lbls = [0] * n
for i in range(n):
    lbls[i] = [0] * m

labels_array = []
flag = False
labels_array, labeled = labeling(lbls, image, labels_array, flag)
print("The quantity of things on the photo is " + str(len(labels_array)))
squares = square(labeled, labels_array)
perimeters = perimeter(labeled, labels_array)
compactnesses = compactness(squares, perimeters)
mass_centers = mass_center(labeled, labels_array, squares)
elongations = elongation(labeled, labels_array)

x_vectors = dict.fromkeys(labels_array, [])

j = 0
for key in x_vectors:
    x_vectors.update({key: [key, compactnesses.get(key), elongations.get(key)[0], elongations.get(key)[1]]})
    j += 1
