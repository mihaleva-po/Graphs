
from графы.лр1.ссылка.lr1 import df

# ПРОВЕРКА ЦЕПИ

def proverka_chain_massiv():
    # print("Введите последовательность вершин (в виде названий через запятую без пробелов) ")
    chain = 'Mother,Son'#str(input())
    chain = chain.split(',')
    result = ''

    # Проверка на повтор ребер
    def has_duplicate_edges(edges):
        seen_edges = set()
        for edge in edges:
            if edge in seen_edges:
                return True
            seen_edges.add(edge)
        return False

    if has_duplicate_edges(chain) == 'True':
        result = 'No'
    else:
        # Повторяющихся ребер нет
        # Проверка на наличие пути между вершинами
        for k in range(len(chain) - 1):  # Перебираем введенные слова
            mas_neig = []
            chet = 0
            for i in range(len(df)):  # Перебираем строки
                if chain[k] == df.iat[i, 1]:
                    one_word = df.iat[i, 3]
                    neig = df.iat[i, 3]
                    for i in range(len(neig)):
                        if neig[i] == chain[k + 1]:
                            chet = 1

            if chet != 1:
                result = 'No'

    # if result == 'No':
    #     cont # print("Не является цепью")
    # else:
        # print("Является цепью")









