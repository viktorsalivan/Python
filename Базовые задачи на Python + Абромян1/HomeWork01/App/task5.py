from calendar import c
import math
a = int(input("Ввидите первый катет :"))
b = int(input("Ввидите второй катет :"))
c = math.sqrt(a*a+b*b)
perimeter = a + b + c
ploshad = a*b/2
print(f"Периметер = {perimeter} Площадь =  {ploshad}")
