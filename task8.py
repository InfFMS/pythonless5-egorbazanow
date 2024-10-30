# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
import random
N = int(input())
A = [random.randint(10, 100000) for _ in range(N)]
print(A)
def fun(number):
  d = str(number)
  return len(set(d)) == 1
filt = [x for x in A if fun(x)]
print(filt)