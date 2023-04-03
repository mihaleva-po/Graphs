
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# Матрица представления графа
matrix = np.array([
    [0,3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,5,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,4,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,0],
    [0,0,1,0,0,1,0,0,0,0],
    [0,7,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,7,0]
])


# Алгоритм поиска компонентов связанности

# Проверка соседей
def verified_neig(neig):
    while neig != []:
        neig_old = neig
        neig = []
        for k in range(len(neig_old)):
            verified.append(neig_old[k])
            for j in range(len(matrix)):
                if matrix[neig_old[k]][j] != 0 and j not in component:
                    component.append(j)
                    neig.append(j)
                if matrix[j][neig_old[k]] != 0 and j not in component:
                    component.append(j)
                    neig.append(j)

    return component


components = []
verified = [] # Проверенные вершины

for i in range(len(matrix)): # i - номер вершины
    neig = []  # Соседи вершины
    if i not in verified: # Если вершина не проверена
        component = []  # Список связанных компонентов
        component.append(i)
        verified.append(i)
        for j in range(len(matrix)):
            if matrix[i][j] != 0 and j not in component:
                component.append(j)
                neig.append(j)
            if matrix[j][i] != 0 and j not in component:
                component.append(j)
                neig.append(j)

        components.append(verified_neig(neig))

for i in range(len(components)):
    print(components[i])


# Визуализация графа
graph = nx.from_numpy_array(matrix)
pos = nx.circular_layout(graph) # Определение карты расположения узлов
nx.draw(graph, pos = pos, with_labels=True) # Создание изображения графа
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels)
nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_labels)
plt.show()









