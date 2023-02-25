# Дан список целых чисел.
# Подсчитать сколько четных чисел в списке
import random
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод элементов списка  в случайном порядке - не по заданию (для интереса)
random.shuffle(spisok)
counter = 0  # Счёчик для подсчёта чётных
for item in spisok:
    if item > 0 and item % 2:
        counter += 1
print(counter)
