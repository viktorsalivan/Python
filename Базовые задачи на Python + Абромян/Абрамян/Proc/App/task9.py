# Описать процедуру Swap(X, Y), меняющую содержимое переменных X
# и Y (X и Y — вещественные параметры, являющиеся одновременно вход-
# ными и выходными). С ее помощью для данных переменных A, B, C, D по-
# следовательно поменять содержимое следующих пар: A и B, C и D, B и C
# и вывести новые значения A, B, C, D.

x = int(input("Ввидите x : \n"))
y = int(input("Ввидите y : \n"))


def swap(x, y):
    temp = x  # В временую переменную присваем x
    x = y  # x присваеваем y
    y = temp  # y присваеваем x
    return x, y


swap(x, y)
print(f"X = {x} Y = {y}")
