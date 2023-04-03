
# Построить график зависимости вероятности существования пути
# между первым и последним столбцами решетки от вероятности
# закрашивания клетки (объем выборки для вычисления
# вероятности существования пути выбрать самостоятельно, если
# задано несколько значений параметра М, должно быть по
# одному графику для каждого значения).

import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx


N = 10
grid = np.zeros((N, N)) # Создаем нулевую решетку
painted = [] # Закрашенные клетки
componets = [] # Все компоненты

# Создаем нулевую матрицу
matrix = np.zeros((N, N))

probality_having_path = [] # Вероятности наличия пути
value_p = [] # Значения вероятности

# Перебор вероятностей
for i in range(0, 101, 5):
    p = i / 100 # Вероятность
    M = int(p * (N**2)) # Количество клеток, которые нужно закрасить

    success = False # Показывает наличие/отсутствие пути
    kolvo_success = 0  # Количество успешных событий
    for m in range(10): # Повтор одного значение M 10 раз
        # Закрашиваем клетки
        for j in range(M):
            row = random.randint(0, len(grid) - 1)  # Случайная строка
            col = random.randint(0, len(grid[0]) - 1)  # Случайный столбец
            elem = [row, col]
            if elem not in painted:  # Проверка на повтор клеток
                grid[row][col] = 1  # Закрашиваем клетку
                painted.append(elem)  # Закрашенные элементы

        # print(grid)

        # Формируем граф
        edge_list = []  # Список ребер
        ver_1 = 0  # Номер вершины
        ver_2 = 101  # Максимальный номер вершины +1
        list_top = []  # Список вершин
        connection_tops = []  # Список связанных вершин

        for row in range(len(grid)):  # Перебираем строки
            for col in range(len(grid)):  # Перебираем столбцы
                if grid[row][col] != 0:  # Находим вершину
                    nomer_noid = str(row) + str(col)  # Номер вершины формируется как номер строки и столбца
                    connection_tops.append(int(nomer_noid))  # Добавляем в список связанных вершин

                    # Находим ее возможных соседей
                    if row > 0:
                        if grid[row - 1][col] != 0:  # Вершина сверху
                            nomer_noid = str(row - 1) + str(col)  # Номер вершины формируется как номер строки и столбца
                            connection_tops.append(int(nomer_noid))  # Добавляем в список связанных вершин
                    if row < N - 1:
                        if grid[row + 1][col] != 0:  # Вершина снизу
                            nomer_noid = str(row + 1) + str(col)
                            connection_tops.append(int(nomer_noid))
                    if col < N - 1:
                        if grid[row][col + 1] != 0:  # Вершина справа
                            nomer_noid = str(row) + str(col + 1)
                            connection_tops.append(int(nomer_noid))
                    if col > 0:
                        if grid[row][col - 1] != 0:  # Вершина слева
                            nomer_noid = str(row) + str(col - 1)
                            connection_tops.append(int(nomer_noid))
                list_top.append(connection_tops)
                connection_tops = []

        # print(list_top) [[], [], [], [], [19], [], [], [22], [], [], [], [], []]

        # Удаляем пустые элементы списка
        new_list = [sublist for sublist in list_top if sublist]
        # print(new_list) [[19], [22], [34], [37, 47, 65], [48, 27]]

        pairs = []  # Пары ребер
        isolated_vershin = []  # Изолированные вершины
        for f in range(len(new_list)):
            list = new_list[f]  # Вершины по группам связанности
            if len(list) == 1:  # Если вершина 1
                isolated_vershin.append(list[0])  # Добавляем ее в список изолированных вершин
            else:
                # Создаем пары вершин (ребро)
                for i in range(len(list)):
                    for j in range(i + 1, len(list)):
                        edge = (list[i], list[j])  # Ребро
                        edge_reverse = (list[j], list[i])  # Обратное ребро
                        if edge not in pairs and edge_reverse not in pairs:  # Если ребра нет в списке
                            pairs.append(edge)

        # print(pairs) [(3, 4), (4, 14), (4, 5)]

        # print(isolated_vershin) [0, 11, 19, 22, 41, 53, 61, 78]

        # Представление графа
        G = nx.Graph()
        G.add_edges_from(pairs)  # Добавляем ребра

        if pairs != []:  # Если есть связанные вершины
            # Первая цифра номера вершины - номер строки
            # Вторая цифра номера вершины - номер столбца
            # У нас решетка 10 на 10
            # Первый столбец вторая цифра 0
            # Последний столбец вторая цифра 9

            # Найдем вершины из первого столбца
            first_column = []  # Вершины первого столбца
            for par in range(len(pairs)):  # Перебираем все пары
                for t in range(len(pairs[par])):
                    if pairs[par][t] % 10 == 0:  # Если вершина из первого столбца
                        if pairs[par][t] not in first_column:  # Если ее нет в списке
                            first_column.append(pairs[par][t])  # Добавляем в список

            # Найдем вершины из последнего столбца
            last_column = []  # Вершины первого столбца
            for par in range(len(pairs)):  # Перебираем все пары
                for t in range(len(pairs[par])):
                    if pairs[par][t] % 10 == 9:  # Если вершина из последнего столбца
                        if pairs[par][t] not in last_column:  # Если ее нет в списке
                            last_column.append(pairs[par][t])

            if first_column != [] and last_column != []:  # Если есть вершины из обоих столбцов
                for first in range(len(first_column)):  # Перебираем вершины из первого столбца
                    for last in range(len(last_column)):  # Перебираем вершины из последнего столбца
                        # Проверяем связность этих вершин
                        connected = nx.has_path(G, first_column[first], last_column[last])
                        if connected:
                            success = True # Есть успех

        if success == True:
            kolvo_success += 1 # Увеличиваем количество успешных событий

    # Считаем вероятность наличия пути
    probality_having_path.append(kolvo_success / 10)
    value_p.append(p)

# Строим график зависимости вероятности существования пути
# между первым и последним столбцами решетки от вероятности закрашивания клетки
plt.plot(value_p, probality_having_path)
plt.xlabel('Вероятность закрашивания клетки')
plt.ylabel('Вероятность существования пути')
plt.title('Зависимость вероятности существования пути от вероятности закрашивания клетки')
plt.show()




