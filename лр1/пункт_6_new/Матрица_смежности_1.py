
from графы.лр1.ссылка.lr1 import labels, matrix

# ПОИСК ВСЕХ СОСЕДЕЙ ЗАДАННОЙ ВЕРШИНЫ

def poisk_neig_matrix():
    # print('Введите название вершины ')
    top = 'Son'#input()  # Название вершины

    number = -1  # Номер вершины
    neig = []  # Соседи
    while number == -1:
        for i in range(len(labels)):
            if labels[i] == top:
                number = i

    st = number  # Номер строки
    for i in range(len(matrix)):  # Перебираем номер столбца
        if matrix[st][i] != 0:
            neig.append(labels[i])

    st = number  # Номер столбца
    for i in range(len(matrix)):  # Перебираем номер строки
        if matrix[i][st] != 0:
            neig.append(labels[i])

    # print("Соседи вершины ", top, ' ', neig)















