def allSum(*args):
    summa = 0
    for item in args:
        summa = summa + item
    return summa


rezult = allSum(1, 2, 3, 4, 5, 6, 7, 8)
print(rezult)
