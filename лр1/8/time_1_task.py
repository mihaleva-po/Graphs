
import time
from графы.лр1.пункт_6_new.Массив_записей_1 import poisk_neig_massiv
from графы.лр1.пункт_6_new.Матрица_смежности_1 import poisk_neig_matrix
from графы.лр1.пункт_6_new.Список_ребер_1 import poisk_neig_edge

# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    poisk_neig_massiv()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы поиска всех соседей заданного графа из массива записей: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    poisk_neig_matrix()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы поиска всех соседей заданного графа из матрицы смежности: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    poisk_neig_edge()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы поиска всех соседей заданного графа из списка ребер: {total_time:.4f} секунд.")