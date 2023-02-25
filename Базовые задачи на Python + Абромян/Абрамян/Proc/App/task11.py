# Описать процедуру Minmax(X, Y), записывающую в переменную X ми-
# нимальное из значений X и Y, а в переменную Y — максимальное из этих
# значений (X и Y — вещественные параметры, являющиеся одновременно
# входными и выходными). Используя четыре вызова этой процедуры, найти

x = int(input("Ввидите x : \n"))
y = int(input("Ввидите y : \n"))


def minMax(x, y):
    summa = x + y
    if x > y:
        x = summa - x  # y
        y = summa - y  # x
    else:
        x < y
        pass
        return x, y


tempX, tempY = minMax(x, y)
print(tempX, tempY)

# def minMax(x, y):
#     minValue = 0
#     maxValue = 0
#     if x > y:
#         maxValue = x
#     else:
#         maxValue = y
#     if x < y:
#         minValue = x
#     else:
#         minValue = y
#     return minValue, maxValue


# tempMin, tempMax = minMax(x, y)
# print(f"Минимальное значение : {tempMin}\nМаксимальное значение : {tempMax}")
