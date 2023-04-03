
from графы.лр1.ссылка.lr1 import labels, df

# ПОИСК ВСЕХ СОСЕДЕЙ ЗАДАННОЙ ВЕРШИНЫ

def poisk_neig_massiv():
    # print('Введите название вершины ')
    top = 'Son'#input()  # Название вершины

    number = -1  # Номер вершины
    while number == -1:
        for i in range(len(labels)):
            if labels[i] == top:
                number = i

    neig = [] # Соседи
    for i in range(len(df)):
        if df.iat[i, 1] == top:
            neig.append(df.iat[i, 7])
    # print('\n', "Соседи вершины ", top, ' ', neig)




