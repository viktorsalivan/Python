# Описать процедуру AddRightDigit(D, K), добавляющую к целому поло-
# жительному числу K справа цифру D (D — входной параметр целого типа,
# лежащий в диапазоне 0–9, K — параметр целого типа, являющийся одно-
# временно входным и выходным). С помощью этой процедуры последова-
# тельно добавить к данному числу K справа данные цифры D1 и D2, выводя
# результат каждого добавления.
k = int(input("Ввидите K :"))
d = int(input("Ввидите d :"))


def addRightDigit(k, d):
    return k * 10 + d


print(addRightDigit(k, d))
