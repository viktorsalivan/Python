import math
'''
Даны два действительных числа. Найти среднее арифметическое и среднее
геометрическое этих чисел
'''
a = 10
b = 20
sum = a + b
avgArifmetic = sum/2
print(f"Среднее арифметическое = {avgArifmetic}")
avgGeometric = math.sqrt(a*b)
print(f"Среднее геомитричиское = {avgGeometric}")
