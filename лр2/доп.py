
import time
import numpy as np
import matplotlib.pyplot as plt


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


# Проверка соседей
def verified_neig(neig):
    while neig != []:
        neig_old = neig
        neig = []
        for k in range(len(neig_old)):
            verified.append(neig_old[k])
            for j in range(len(matrix)):
                if matrix[neig_old[k]][j] != 0 and j not in component:
                    component.append(j)
                    neig.append(j)
                if matrix[j][neig_old[k]] != 0 and j not in component:
                    component.append(j)
                    neig.append(j)

    return component

time_alg = [] # Время выполнения алгоритма
kolvo_comp = [] # Количество компонентов

for k in range(6, 20): # Размер матрицы
    # Создание матрицы графа
    matrix = get_hexagonal_lattice_adjacency_matrix(k)
    # Засекаем время начала выполнения алгоритма
    start_time = time.time()

    # Запускаем алгоритм
    components = []
    verified = []  # Проверенные вершины

    for i in range(len(matrix)):  # i - номер вершины
        neig = []  # Соседи вершины
        if i not in verified:  # Если вершина не проверена
            component = []  # Список связанных компонентов
            component.append(i)
            verified.append(i)
            for j in range(len(matrix)):
                if matrix[i][j] != 0 and j not in component:
                    component.append(j)
                    neig.append(j)
                if matrix[j][i] != 0 and j not in component:
                    component.append(j)
                    neig.append(j)
            components.append(verified_neig(neig))

    # Конец измерения времени
    end_time = time.time()

    # Подсчет времени
    total_time = end_time - start_time

    # Подсчет количества элементов
    kolvo_component = len(components)

    # Запись в переменные для построения графика
    time_alg.append(total_time)
    kolvo_comp.append(kolvo_component)


# Построение графика
plt.plot(kolvo_comp, time_alg)
plt.xlabel('Количество компонентов графа')
plt.ylabel('Время выполнения алгоритма')
plt.title('Зависимость выполнения алгоритма от количества компонентов графа')
plt.show()


