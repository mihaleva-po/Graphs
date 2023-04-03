
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import warnings

# Матрица смежности в явном виде
matrix = [[0, 0, 1,	0,	0,	0,	0,	0],
[0,	0,	0,	1,	0,	0,	0,	0],
[0,	0,	0,	0,	1,	1,	0,	0],
[0,	0,	2,	0,	1,	1,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0],
[2,	0,	1,	0,	0,	0,	0,	0],
[0,	2,	0,	1,	0,	0,	0,	0]]

# Подписи вершин
labels = {0: 'Grandpa 1', 1: 'Grandpa 2', 2: 'Mother', 3: 'Father', 4: 'Son', 5: 'Daughter',
          6: 'Grandma 1', 7: 'Grandma 2'}

edge_list1 = [] # Хранит список ребер
edge_list2 = []
for i in range(len(matrix)): # Перебираем все элементы матрицы
    for j in range(len(matrix)):
        if matrix[i][j] != 0: # Проверка на наличие ребра между точками
            edge_list1.append((labels[i], labels[j], matrix[i][j]))
            edge_list2.append((i, j, {'weight': matrix[i][j]}))
print("Список ребер:")
print(edge_list1)


# Создание графа
G = nx.DiGraph(directed=True)
# Подписи вершин
G.add_nodes_from(['Grandpa 1', 'Grandpa 2', 'Mother', 'Father', 'Son', 'Daughter',
 'Grandma 1', 'Grandma 2'])
# Список ребер
G.add_weighted_edges_from([('Grandpa 1', 'Mother', 1), ('Grandpa 2', 'Father', 1),
                           ('Mother', 'Son', 1), ('Mother', 'Daughter', 1), ('Father', 'Mother', 2),
                           ('Father', 'Son', 1), ('Father', 'Daughter', 1), ('Grandma 1', 'Grandpa 1', 2),
                           ('Grandma 1', 'Mother', 1), ('Grandma 2', 'Grandpa 2', 2), ('Grandma 2', 'Father', 1)])

pos = nx.circular_layout(G) #Определение карты расположения узлов
nx.draw(G, pos = pos, with_labels=True) #Создание изображения графа
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
plt.show() #Отображение графа

# Создание списка записей

records = [] # Создание массива записей
for i in range(len(matrix)): # Перебираем строки
    node = {
        'id': i,
        'name': labels[i],
        'children': 0, # Количество детей
        'parents': 0,
        'neighbors': 0,
        'name_children': [],
        'name_parents': [],
        'name_neighbors': [],
        'outgoing_weights': [], # Вес исходящих ребер
        'incoming_weights': [], # Вес входящий ребер
        'incident_weights': [] # Вес инцидентных ребер
    }
    for j in range(len(matrix)): # Перебираем столбцы
        if matrix[i][j] != 0:
            node['children'] += 1
            node['name_children'].append(labels[j])
            node['outgoing_weights'].append(matrix[i][j])

    k = i # k хранит номер строки
    for y in range(len(matrix)): # Проходимся по столбцу, изменяя номер строки
        if matrix[y][k] != 0:
            node['parents'] += 1
            node['name_parents'].append(labels[y])
            node['incoming_weights'].append(matrix[y][k])

    node['neighbors'] = node['parents'] + node['children']
    node['name_neighbors'].append(node['name_parents'])
    node['name_neighbors'].append(node['name_children'])
    node['incident_weights'].append(node['incoming_weights'])
    node['incident_weights'].append(node['outgoing_weights'])
    records.append(node)

print('\n', "Массив записей:")

# Вывод данных в виде таблицы

# Создание пустой таблицы
df = pd.DataFrame(columns=['ID', 'Name', 'Children', 'Children_name', 'Parents', 'Parents_name',
                           'Neighbors', 'Neighbors_name', 'Outgoing_weights',
                                 'Incoming_weights', 'Incident_weights'])
# Заполнение таблицы
for record in records:
    new_row = {'ID':record['id'], 'Name':record['name'], 'Children':record['children'],
               'Children_name': record['name_children'], 'Parents':record['parents'],
               'Parents_name':record['name_parents'], 'Neighbors':record['neighbors'],
               'Neighbors_name':record['name_neighbors'],'Outgoing_weights':record['outgoing_weights'],
                                 'Incoming_weights':record['incoming_weights'],
               'Incident_weights':record['incident_weights']}
    warnings.simplefilter("ignore") # Убираем предупреждения
    df = df.append(new_row, ignore_index=True)

print(df.to_string(index=False))















