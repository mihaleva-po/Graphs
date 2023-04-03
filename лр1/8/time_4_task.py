
import time
from графы.лр1.пункт_6_new.Массив_записей_4 import kolvo_edge_massiv
from графы.лр1.пункт_6_new.Матрица_смежности_4 import kolvo_edge_matrix
from графы.лр1.пункт_6_new.Список_ребер_4 import kolvo_edge_edge


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    kolvo_edge_massiv()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы вывода количества ребер "
      f"в графе из массива записей: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    kolvo_edge_matrix()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы вывода количества ребер "
      f"в графе из матрицы смежности: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    kolvo_edge_edge()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы вывода количества ребер "
      f"в графе из списка ребер: {total_time:.4f} секунд.")