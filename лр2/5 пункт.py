
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

    # Удаляем лишние вершины
    row_sums = np.sum(matrix, axis=1)
    while np.min(row_sums) < 2:
        i = np.argmin(row_sums)
        matrix = np.delete(matrix, i, axis=0)
        matrix = np.delete(matrix, i, axis=1)
        row_sums = np.sum(matrix, axis=1)

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

mean_time_alg = [] # Среднее время выполнения алгоритма
kolvo_node = [] # Количество вершин

for k in range(6, 20): # Размер матрицы
    sum_time = 0 # Суммарное время для 10 повторов выполнения алгоритма
    for n in range(10): # Количество повторов

         matrix = get_hexagonal_lattice_adjacency_matrix(k) # Создание матрицы графа
         # Подсчет количества вершин
         kolvo = len(matrix)

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
         sum_time += total_time

    # Запись в переменные для построения графика
    mean_time_alg.append(sum_time/10)
    kolvo_node.append(kolvo)


# Построение графика
plt.plot(kolvo_node, mean_time_alg)
plt.xlabel('Количество вершин графа')
plt.ylabel('Время выполнения алгоритма')
plt.title('Зависимость выполнения алгоритма от количества вершин графа')
plt.show()












