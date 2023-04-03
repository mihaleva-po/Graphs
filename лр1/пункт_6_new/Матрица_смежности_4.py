
from графы.лр1.ссылка.lr1 import matrix

# КОЛИЧЕСТВО РЕБЕР В ГРАФЕ
def kolvo_edge_matrix():
    kolvo_edge = 0  # Количество ребер

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                kolvo_edge += 1

    # print("Количество ребер в графе равно", kolvo_edge)

