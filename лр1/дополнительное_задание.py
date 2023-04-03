
from графы.лр1.ссылка.lr1 import df

tops = [] # Вершины
for i in range(len(df)): # Перебираем вершины
    top = df.iat[i, 1] # Какая-то вершина
    weights_1 = df.iat[i, 8] # Вес исходящих ребер
    print(top)
    sum_1 = 0
    for num in weights_1:
        sum_1 += num
    print(sum_1)

    weights_2 = df.iat[i, 9]  # Вес входящих ребер
    sum_2 = 0
    for num in weights_2:
        sum_2 += num
    print(sum_2)

    if sum_2 > sum_1: # Сравнение сумм весов ребер
        tops.append(top)

print("Вершина/ы ", tops, 'в которых суммарный вес входящих ребер превышает суммарный вес исходящих ребер')














