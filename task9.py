# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
def remove_duplicates(A):
    B = []
    for element in A:
        if element not in B:
            B.append(element)
    return B
from random import randint
N = int(input())
A = [ randint(1, 100)  for i in range(N)]
print(A)
B = list(remove_duplicates(A))
print(B)
#Нашел функцию в интернете
#Она проверяет каждый элемент и изначального списка, а затем добавляет неповторяющиеся в новый список