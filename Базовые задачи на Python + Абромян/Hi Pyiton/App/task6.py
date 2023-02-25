number = int(input("Ввидите N:\n"))
# factorial = 1
# if number % 2 == 0:
#     for item in range(2, number+1, 2):
#         factorial *= item
# print("Двайной Факториал числа", number, "равен", factorial)


def factorial2(number):
    factorial = 1
    if number % 2 == 0:
        for item in range(2, number+1, 2):
            factorial *= item
        return factorial
    else:
        start = 1
        factorial = 1
        for item in range(start + 2, number+1, 2):
            factorial *= item
        return factorial


temp = factorial2(number)
print("Двайной Факториал числа", number, "равен", temp)
