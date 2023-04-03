
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt


# Функция поиска спектра степеней графа
def spectr_stepenei(pairs, isolated_vershin):
    kolvo_noid = [] # Храним количество вершин с определенной степенью
    stepen_noid = [] # Храним степень вершин
    stepen = [] # Хранит все степени

    # Количество изолированных вершин
    kolvo_noid.append(len(isolated_vershin))
    # Степень изолированных вершин
    stepen_noid.append(0)

    name_noid = [] # Вершины,степень которых уже записали
    # Перебираем вершины с ребрами
    for w in range(len(pairs)):
        for j in range(len(pairs[w])):
            print(pairs[w][j])
            step = 0 # Количество степеней
            if pairs[w][j] not in name_noid: # Если вершина еще не записана
                name_noid.append(pairs[w][j])  # Записываем название вершины
                current_noid = pairs[w][j]  # Текущая вершина
                # Перебираем все вершины в переменной pairs
                for v in range(len(pairs)):
                    for k in range(len(pairs[v])):
                        if pairs[v][k] == current_noid:  # Вершина из pairs равна текущей вершины
                            step += 1  # Увеличиваем степень
                stepen.append(step)  # Добавляем степень вершины в список
    print('stepen')
    print(stepen)
    # stepen = [0, 1, 1, 3, 5, 1, 2]
    # Считаем количество повторов одной степени
    for i in range(len(stepen)):
        step = 0
        if stepen[i] not in stepen_noid: # Если эта степень еще не записана
            current_step = stepen[i]  # Текущая степень
            # Считаем количество текущей степени
            for h in range(len(stepen)):
                if current_step == stepen[h]:  # Если степень повторяется
                    step += 1  # Увеличиваем счетчик
            kolvo_noid.append(step)  # Количество вершин данной степени
            stepen_noid.append(current_step)  # Степень

    print('kolvo_noid')
    print(kolvo_noid)
    print('stepen_moid')
    print(stepen_noid)
    # Строим гистограмму
    bins = np.arange(len(stepen_noid)) # Названия столбцов гистограммы
    plt.bar(bins, kolvo_noid)
    plt.title('Спект степеней вершин графа')
    plt.xlabel('Степень')
    plt.ylabel('Количество вершин')
    plt.xticks(bins, stepen_noid) # Устанавливаем метки по столбцам
    plt.show()


N = 10
grid = np.zeros((N, N)) # Создаем нулевую решетку
painted = [] # Закрашенные клетки
componets = [] # Все компоненты

# Создаем нулевую матрицу
matrix = np.zeros((N, N))

# Перебор вероятностей
for i in range(0, 101, 5):
    p = i / 100 # Вероятность
    M = int(p * (N**2)) # Количество клеток, которые нужно закрасить

    # Закрашиваем клетки
    for j in range(M):
        row = random.randint(0, len(grid) - 1) # Случайная строка
        col = random.randint(0, len(grid[0]) - 1) # Случайный столбец
        elem = [row, col]
        if elem not in painted: # Проверка на повтор клеток
            grid[row][col] = 1 # Закрашиваем клетку
            painted.append(elem) # Закрашенные элементы

    print(grid)

    # Формируем граф
    edge_list = [] # Список ребер
    ver_1 = 0 # Номер вершины
    ver_2 = 101 # Максимальный номер вершины +1
    list_top = [] # Список вершин
    connection_tops = [] # Список связанных вершин

    for row in range(len(grid)): # Перебираем строки
        for col in range(len(grid)): # Перебираем столбцы
                if grid[row][col] != 0:  # Находим вершину
                    nomer_noid = str(row) + str(col) # Номер вершины формируется как номер строки и столбца
                    connection_tops.append(int(nomer_noid)) # Добавляем в список связанных вершин

                    # Находим ее возможных соседей
                    if row > 0:
                        if grid[row - 1][col] != 0:  # Вершина сверху
                            nomer_noid = str(row - 1) + str(col) # Номер вершины формируется как номер строки и столбца
                            connection_tops.append(int(nomer_noid)) # Добавляем в список связанных вершин
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

    pairs = [] # Пары ребер
    isolated_vershin = [] # Изолированные вершины
    for f in range(len(new_list)):
        list = new_list[f] # Вершины по группам связанности
        if len(list) == 1: # Если вершина 1
            isolated_vershin.append(list[0]) # Добавляем ее в список изолированных вершин
        else:
            # Создаем пары вершин (ребро)
            for i in range(len(list)):
                for j in range(i + 1, len(list)):
                    edge = (list[i], list[j]) # Ребро
                    edge_reverse = (list[j], list[i]) # Обратное ребро
                    if edge not in pairs and edge_reverse not in pairs: # Если ребра нет в списке
                        pairs.append(edge)

    # print(pairs) [(3, 4), (4, 14), (4, 5)]

    # print(isolated_vershin) [0, 11, 19, 22, 41, 53, 61, 78]

    if isolated_vershin != [] or pairs != []: # Если есть вершины
        # Визуализация графа
        G = nx.Graph()
        G.add_edges_from(pairs)  # Добавляем ребра

        # Добавление изолированных/единичных вершин
        for p in range(len(isolated_vershin)):
            G.add_node(isolated_vershin[p])

        # pos = nx.kamada_kawai_layout(G)
        pos = nx.shell_layout(G)
        # pos = nx.random_layout(G)
        # pos = nx.circular_layout(G)  # Определение карты расположения узлов
        # pos = nx.spring_layout(G) # Расположение графика
        nx.draw_networkx_nodes(G, pos, node_size=500)  # Добавление узлов
        nx.draw_networkx_edges(G, pos)  # Добавление ребер
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        plt.axis('off')
        plt.title('Граф')
        plt.figure()
        spectr_stepenei(pairs, isolated_vershin)  # Вызываем функцию

















