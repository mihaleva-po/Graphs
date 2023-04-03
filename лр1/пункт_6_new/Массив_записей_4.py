
from графы.лр1.ссылка.lr1 import df

# КОЛИЧЕСТВО РЕБЕР В ГРАФЕ
def kolvo_edge_massiv():
    kolvo_edge = 0  # Количество ребер

    for i in range(len(df)):  # Перебираем вершины
        weights = df.iat[i, 10]
        # Количество элементов
        digits = ''.join(str(x) for sublist in weights for x in sublist)
        kolvo_edge += len(digits)

    kolvo_edge = int(kolvo_edge / 2)

    # print("Количество ребер в графе равно", kolvo_edge)


