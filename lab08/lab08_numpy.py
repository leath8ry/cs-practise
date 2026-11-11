import numpy as np


# Задание 1. Создание векторов и матриц
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print("=== Задание 1 ===")
print(f"hours: {hours}")
print(f"shape: {hours.shape}, ndim: {hours.ndim}, size: {hours.size}, dtype: {hours.dtype}")
print()

# Задание 2. Индексы и срезы в векторе
print("=== Задание 2 ===")
print(f"Третий элемент: {hours[2]}")
print(f"Последний элемент: {hours[-1]}")
print(f"Элементы с индексами 2–5: {hours[2:6]}")
print(f"Каждый второй элемент: {hours[::2]}")
print(f"Массив в обратном порядке: {hours[::-1]}")
print()

# Задание 3. Строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("=== Задание 3 ===")
print(f"Форма: {temperatures.shape}")
print(f"Число измерений: {temperatures.ndim}")
print(f"Число элементов: {temperatures.size}")
print(f"[1][2]: {temperatures[1, 2]}")
print(f"Первая строка: {temperatures[0]}")
print(f"Последний столбец: {temperatures[:, -1]}")
print(f"Первые две строки без первого столбца:\n{temperatures[:2, 1:]}")
print(f"Центральный фрагмент 2x2:\n{temperatures[0:2, 1:3]}")
print()


# Задание 4. Прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)

print("=== Задание 4 ===")
print(f"Первые три строки:\n{matrix[:3]}\nshape: {matrix[:3].shape}")
print(f"Последние две строки:\n{matrix[-2:]}\nshape: {matrix[-2:].shape}")
print(f"Первые два столбца:\n{matrix[:, :2]}\nshape: {matrix[:, :2].shape}")
print(f"Строки 1-3, столбцы 2-4:\n{matrix[1:4, 2:5]}\nshape: {matrix[1:4, 2:5].shape}")
print(f"Угловой блок 2x2 (правый нижний):\n{matrix[3:, 3:]}\nshape: {matrix[3:, 3:].shape}")
print()

# Задание 5. Изменение массива с помощью срезов
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1

print("=== Задание 5 (changed_hours) ===")
print(f"changed_hours: {changed_hours}")
print(f"исходный hours:  {hours}")
print()

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0          
changed_matrix[:, -1] = -1        
changed_matrix[1:4, 1:4] = 100    

print("=== Задание 5 (changed_matrix) ===")
print(f"Исходная matrix:\n{matrix}")
print(f"Изменённая:\n{changed_matrix}")
print()

# Задание 6. Изменение формы
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("=== Задание 6 ===")
print(f"numbers shape: {numbers.shape}")
print(f"table shape:   {table.shape}")
print(f"transposed shape: {transposed.shape}")
