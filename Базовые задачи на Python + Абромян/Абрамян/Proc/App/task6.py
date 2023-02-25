# Описать процедуру DigitCountSum(K, C, S), находящую количество C
# цифр целого положительного числа K, а также их сумму S (K — входной,
# C и S — выходные параметры целого типа). С помощью этой процедуры
# найти количество и сумму цифр для каждого из пяти данных целых чисел.

k = int(input("Ввидите чило K : "))


def digitCountSum(k):
    sumaspisok = list(str(k))
    counter = 0
    Summacounter = 0
    for item in sumaspisok:
        Summacounter += (int(item))
        counter += 1
    return counter, Summacounter


temp1, temp2 = digitCountSum(k)
print(f"Количиство - {temp1} Сума = {temp2}")
