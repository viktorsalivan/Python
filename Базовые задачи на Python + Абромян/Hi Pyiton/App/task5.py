number = int(input("Введите число: "))
i = 2  # начальная позиция числа (число)
factorial = 1  # чило на которое мы будем умнажать
while i <= number:  # пока наша начальная позиция меньше или равна числу продалжаем
    factorial *= i
    i += 2  # каждый раз приболяем к начальной позиции 2  то есть 1*2  = 2, 4x1 = 4, 6X1 = 6 => выход
print("Факториал числа", number, "равен", factorial)
