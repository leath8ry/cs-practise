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
