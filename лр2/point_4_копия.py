import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Создание графа
def get_hexagonal_lattice_adjacency_matrix(M):
    # Создаем нулевую матрицу
    M2 = M * M
    matrix = np.zeros((M2, M2))

    # Соединяем вершины в правильную шестиугольную решетку
    for V in range(M2):
        r = V // M
        c = V % M
        if ((r % 4 == 0 and c % 2 == 1) or
                (r % 4 == 2 and c % 2 == 0)):
            if r > 0:
                matrix[V][V - M] = matrix[V - M][V] = 1
            if r < M - 1 and c < M - 1:
                matrix[V][V + M + 1] = matrix[V + M + 1][V] = 1
            if r < M - 1 and c > 0:
                matrix[V][V + M - 1] = matrix[V + M - 1][V] = 1

    return matrix


# Визуализация решетки
graph = nx.from_numpy_array(get_hexagonal_lattice_adjacency_matrix(6))
pos = nx.kamada_kawai_layout(graph) # Определение карты расположения узлов
nx.draw(graph, pos = pos, with_labels=True) #Создание изображения графа
plt.show() #Отображение графа












