# кластеризация методом k-means
import random


# k - количество кластеров, на которые надо разделить входные векторы
# x_vectors = словарь {ярлык: [значения, его, векторов]}
def k_means(x_vectors, k):
    global m_vectors
    # формируем массив со всеми отдельными значениями векторов,
    # чтобы потом из этих чисел случайно выбрать значения для центров
    numbers = []
    for i in range(k):
        m_vectors = [0] * len(x_vectors[i] - 1)
        for j in range(x_vectors[i]):
            numbers.append(x_vectors[i][j])
    # получаем случайные значения центров
    for i in range(k):
        for j in range(len(m_vectors[i])):
            m_vectors[i][j] = random.choice(numbers)

    # centers - словарь с номером центра и его вектором
    centers = dict.fromkeys(range(k), [])
    i = 0
    for key in centers:
        centers.update({key: m_vectors[i]})
        i += 1

    # clusters - словарь с номером центра и ключами объектов
    clusters = dict.fromkeys(range(k), [])


# возвращает номер центра и ключ объекта
# centers - словарь с номером центра и его вектором
# clusters - словарь с номером центра и ключами объектов
# x_vectors = словарь {ярлык: [значения, его, векторов]}
def insert_to_cluster(centers, clusters, x_vectors):
    for key in x_vectors:
        # d = разность в значениях векторов между каждым центром и объектом
        d = [0] * len(clusters)
        vector = x_vectors.get(key)
        for k in centers:
            for j in range(len(vector)):
                d[j] += centers.get(k)[j] - vector[j]
        min_d = max(d)
        c = 0
        for j in range(len(d)):
            if d[j] < min_d:
                min_d = d[j]
                c = j
        return c, key


# centers - словарь с номером центра и его вектором
# clusters - словарь с номером центра и ключами объектов
# x_vectors = словарь {ярлык: [значения, его, векторов]}
def centers_recount(centers, clusters, x_vectors):
    is_same = True
    for key in clusters:
        tags = clusters.get(key)
        vectors = []
        for i in range(len(tags)):
            vectors.append(x_vectors.get(tags[i]))
        new_center = center_recount(vectors)
        if not new_center.__eq__(centers.get(key)):
            centers.update({key: new_center})
            is_same = False
    return is_same


# vectors - массив векторов, которые были отнесены к данному центру
# возвращает новый вектор центра
def center_recount(vectors):
    new_center = [0.0] * len(vectors[0])
    for i in range(len(vectors)):
        for j in range(len(vectors[0])):
            new_center[j] += vectors[j][i]
    d = len(vectors)
    for i in range(len(new_center)):
        new_center[i] = new_center[i] / d
    return new_center
