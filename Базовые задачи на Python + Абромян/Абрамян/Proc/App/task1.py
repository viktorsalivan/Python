# Описать процедуру PowerA3(A, B), вычисляющую третью степень числа
# A и возвращающую ее в переменной B (A — входной, B — выходной пара-
# метр; оба параметра являются вещественными). С помощью этой процеду-
# ры найти третьи степени пяти данных чисел.

def power(a, b):
    rezult = a**b
    return rezult


a = power(3, 3)
print(a)
b = power(3, 4)
print(b)
c = power(3, 5)
print(c)
