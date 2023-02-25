# Даны целые числа K и N (N > 0).
# Вывести N раз число K.
k = int(input("Ввидите число K:\n"))
n = int(input("Ввидите количиство раз N:\n"))
if n > 0:
    for i in range(0, n):
        print(k)
