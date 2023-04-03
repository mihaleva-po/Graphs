
import time
from графы.лр1.пункт_6_new.Массив_записей_3 import summ_massiv
from графы.лр1.пункт_6_new.Матрица_смежности_3 import summ_matrix
from графы.лр1.пункт_6_new.Список_ребер_3 import summ_edge


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    summ_massiv()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы вывода вершин с суммой весов инцидентных ребер "
      f"больше заданного числа из массива записей: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    summ_matrix()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы вывода вершин с суммой весов инцидентных ребер "
      f"больше заданного числа из матрицы смежности: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    summ_edge()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы вывода вершин с суммой весов инцидентных ребер "
      f"больше заданного числа из списка ребер: {total_time:.4f} секунд.")