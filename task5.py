# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
from random import randint
N = int(input())
A = [ randint(1, 10000)  for i in range(N)]
print(A)
k = 0
print(max(A))
for i in range(0, N):
    if A[i] == max(A):
        k+=1
print(k)

