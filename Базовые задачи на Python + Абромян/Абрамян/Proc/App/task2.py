# Описать процедуру PowerA234(A, B, C, D), вычисляющую вторую, тре-
# тью и четвертую степень числа A и возвращающую эти степени соответст-
# венно в переменных B, C и D (A — входной, B, C, D — выходные парамет-
# ры; все параметры являются вещественными). С помощью этой процедуры
# найти вторую, третью и четвертую степень пяти данных чисел.

import random


def power(value):
    rezult1 = value**2
    rezult2 = value ** 3
    rezult3 = value**4
    return rezult1, rezult2, rezult3


a = random.randrange(-10, 10)
temp1, temp2, temp3 = power(a)
print(temp1, temp2, temp3)
