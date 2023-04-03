
import time
from графы.лр1.пункт_6_new.Массив_записей_2 import proverka_chain_massiv
from графы.лр1.пункт_6_new.Матрица_смежности_2 import proverka_chain_matrix
from графы.лр1.пункт_6_new.Список_ребер_2 import proverka_chain_edge


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    proverka_chain_massiv()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы проверки последовательности вершин на цепь из массива записей: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    proverka_chain_matrix()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы проверки последовательности вершин на цепь из матрицы смежности: {total_time:.4f} секунд.")


# Начало измерения времени
start_time = time.time()

N = pow(10, 6)
for i in range(N):
    proverka_chain_edge()

# Конец измерения времени
end_time = time.time()

# Подсчет времени
total_time = end_time - start_time
print(f"Время выполнения программы проверки последовательности вершин на цепь из списка ребер: {total_time:.4f} секунд.")