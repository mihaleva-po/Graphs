
from графы.лр1.ссылка.lr1 import edge_list1

# ПРОВЕРКА ЦЕПИ

def proverka_chain_edge():
    # print("Введите последовательность вершин (в виде названий через запятую без пробелов) ")
    chain = 'Mother,Son'#str(input())
    chain = chain.split(',')

    # Проверка на повтор вершин
    def has_duplicate_words(string):
        words = string.split()
        return len(words) != len(set(words))

    number_chain = []  # Хранит номера введенных вершин
    res = has_duplicate_words(str(chain))
    result = ''
    if res:
        result = 'No'
    else:
        # Нет повторов
        # Проверка на наличие пути между вершинами
        for k in range(len(chain) - 1):
            chet = 0  # Счетчик
            for i in range(len(edge_list1)):
                if chain[k] == edge_list1[i][0]:
                    for u in range(len(edge_list1)):
                        if edge_list1[i][1] == chain[k + 1]:
                            chet = 1
            # Проверка условия
            if chet != 1:
                result = 'No'

    # if result == 'No':
    #     print("Не является цепью")
    # else:
    #     print("Является цепью")









