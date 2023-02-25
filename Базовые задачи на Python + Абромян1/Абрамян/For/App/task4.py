# Дано целое число — цена 1 кг конфет. Вывести стоимость 1,
# 2, . . . , 10 кг конфет.
price = int(input("Ввидите цену за 1кг:"))
kg = int(input("Ввидите количиство кг:"))
for i in range(1, kg + 1):
    summa = i*price
    print(summa)
