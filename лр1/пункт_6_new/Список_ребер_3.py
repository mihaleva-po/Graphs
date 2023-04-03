
from графы.лр1.ссылка.lr1 import labels, edge_list1

# НОМЕРА ВЕРШИН, СУММА ВЕСОВ ИНЦИДЕНТНЫХ РЕБЕР КОТОРЫХ БОЛЬШЕ N

def summ_edge():
    # print("Введите целое число")
    N = 5 #int(input())

    tops = []  # Вершины
    for k in range(len(labels)):  # Перебираем вершины
        summ = 0
        for i in range(len(edge_list1)):  # Перебираем список ребер
            if labels[k] == edge_list1[i][0]:
                summ += edge_list1[i][2]
            if labels[k] == edge_list1[i][1]:
                summ += edge_list1[i][2]

        if summ > N:
            tops.append(labels[k])

    # print("Вершина/ы ", tops, 'сумма весов инцидентных ребер которых больше ', N)





















