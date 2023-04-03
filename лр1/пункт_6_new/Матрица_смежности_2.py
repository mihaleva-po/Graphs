from графы.лр1.ссылка.lr1 import labels, matrix

# ПРОВЕРКА ЦЕПИ

def proverka_chain_matrix():
    # print("Введите последовательность вершин (в виде названий через запятую без пробелов) ")
    chain = 'Mother,Son'#str(input())
    chain = chain.split(',')
    result = ''

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

        # Находим номера введенных вершин
        for i in range(len(chain)):
            for j in range(len(labels)):
                if chain[i] == labels[j]:
                    number_chain.append(j)
        if len(number_chain) != len(chain):
            print('Введено некорректное название вершины')
            result = 'No'
        # Проверка на наличие пути между вершинами
        for i in range(len(number_chain) - 1):
            if matrix[number_chain[i]][number_chain[i + 1]] == 0:
                result = 'No'

    # if result == 'No':
    #     print("Не является цепью")
    # else:
    #     print("Является цепью")








