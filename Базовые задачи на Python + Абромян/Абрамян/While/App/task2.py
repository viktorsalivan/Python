# Даны положительные числа A и B (A > B). На отрезке длины A раз-
# мещено максимально возможное количество отрезков длины B (без нало-
# жений). Не используя операции умножения и деления, найти количество
# отрезков B, размещенных на отрезке A.

a = int(input("Ввидите A: "))
b = int(input("Ввидите B: "))
res = 0  # переменная для вычисления отрезков b
if a <= b:
    print("А должно быть больше B и не равно ему!!!")
    exit()  # завершение программы
while a > b:  # while c англиского после - то есть, только после того как выполняется условие выполняется
    res = a - b
    break

print(f"Количество отрезков  B : {res} ")
