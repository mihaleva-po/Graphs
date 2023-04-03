
from графы.лр1.ссылка.lr1 import labels, edge_list1

# ПОИСК ВСЕХ СОСЕДЕЙ ЗАДАННОЙ ВЕРШИНЫ

def poisk_neig_edge():
    # print('Введите название вершины ')
    top = 'Son'#input()  # Название вершины

    number = -1  # Номер вершины
    neig = []  # Соседи
    while number == -1:
        for i in range(len(labels)):
            if labels[i] == top:
                number = i

    neig = []  # Соседи
    for i in range(len(edge_list1)):
        if edge_list1[i][0] == top:
            neig.append(edge_list1[i][1])
        if edge_list1[i][1] == top:
            neig.append(edge_list1[i][0])

    # print("Соседи вершины ", top, ' ', neig)












