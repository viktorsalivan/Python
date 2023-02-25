# Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"

a = int(input("Ввидите число : "))
if a // 1000:
    print("millennium")
else:
    print("Error")
