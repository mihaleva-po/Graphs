
from графы.лр1.ссылка.lr1 import labels, matrix

# НОМЕРА ВЕРШИН, СУММА ВЕСОВ ИНЦИДЕНТНЫХ РЕБЕР КОТОРЫХ БОЛЬШЕ N
def summ_matrix():
    # print("Введите целое число")
    N = 5 #int(input())
    tops = []  # Вершины
    for i in range(len(matrix)):  # Перебираем вершины
        summ = 0
        for j in range(len(matrix)):  # Перебираем столбцы
            if matrix[i][j] != 0:
                summ += matrix[i][j]

        for k in range(len(matrix)):  # Перебираем строки
            if matrix[k][i] != 0:
                summ += matrix[k][i]

        if summ > N:
            tops.append(labels[i])

    # print("Вершина/ы ", tops, 'сумма весов инцидентных ребер которых больше ', N)
















