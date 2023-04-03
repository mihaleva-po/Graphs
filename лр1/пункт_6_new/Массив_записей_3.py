
from графы.лр1.ссылка.lr1 import labels, df

# НОМЕРА ВЕРШИН, СУММА ВЕСОВ ИНЦИДЕНТНЫХ РЕБЕР КОТОРЫХ БОЛЬШЕ N

def summ_massiv():
    # print("Введите целое число")
    N = 5 #int(input())

    tops = []  # Вершины
    for i in range(len(labels)):  # Перебираем вершины
        weights = df.iat[i, 10]
        digits = ''.join(str(x) for sublist in weights for x in sublist)
        summ = sum(int(d) for d in digits)

        if summ > N:
            tops.append(labels[i])

    # print("Вершина/ы ", tops, 'сумма весов инцидентных ребер которых больше ', N)



