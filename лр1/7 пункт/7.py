
import sys
from графы.лр1.ссылка.lr1 import matrix, df, edge_list1, labels

size_in_bytes = sys.getsizeof(matrix) + sys.getsizeof(labels)
print(f"Размер матрицы смежности: {size_in_bytes} байт")

size_in_bytes = sys.getsizeof(df)
print(f"Размер списка записей: {size_in_bytes} байт")

size_in_bytes = sys.getsizeof(edge_list1)
print(f"Размер списка ребер: {size_in_bytes} байт")