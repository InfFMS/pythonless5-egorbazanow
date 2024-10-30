# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import random
import math
N = int(input())
vector1 = [random.uniform(-10, 10) for _ in range(N)]
vector2 = [random.uniform(-10, 10) for _ in range(N)]
print(vector1)
print(vector2)
