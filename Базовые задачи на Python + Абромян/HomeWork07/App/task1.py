"""
	Написать 12 функций по переводу:
1.	
2.	
3.	
4.	
5.	
6.	
7.	
8.	
9.	
10.	
11.	Пинты в литры
12.	Литры в пинты
"""


def inchesConvertTOcentimeters(length):  # 1 Дюймы в сантиметры
    rezult = length*2.54  # Умножьте значение "Длина" на 2,54
    return rezult


def centimeterConvertTOInches(length):  # 2 Сантиметры в дюймы
    rezult = length/2.54  # Разделите значение "Длина" на 2,54
    return rezult


def milesConvertTOkilometers(length):  # 3 Мили в километры
    # Чтобы получить приблизительный результат, умножте значение "Длина" на 1,609
    rezult = length*1.609
    return rezult


def kilometersConvertToMiles(length):  # 4 Километры в мили
    # Чтобы получить приблизительный результат, разделите значение "Длина" на 1,609
    rezult = length/1.609
    return rezult


def poundsConvertToKilograms(massa):  # 5 Фунты в килограммы
    # Чтобы получить приблизительный результат, умножьте значение "Масса" на 2,205
    rezult = massa*2.205
    return rezult


def kilogramsConvertToPounds(massa):  # 6 Килограммы в фунты
    # Чтобы получить приблизительный результат, разделите значение "Масса" на 2,205
    rezult = massa/2.205
    return rezult


def ouncesConvertToGrams(massa):  # 7 Унции в граммы
    # Чтобы получить приблизительный результат, разделите значение "Масса" на 28,35
    rezult = massa/28.35
    return rezult


def gramsConvertToOunces(massa):  # 8 Граммы в унции
    # Чтобы получить приблизительный результат, умножить значение "Масса" на 28,35
    rezult = massa*28.35
    return rezult


def gallonConvertTOliters(volume):  # 9 Галлон в литры
    rezult = volume*3.785
    return rezult


def litersConvertToGallons(volume):  # 10 Литры в галлоны
    # Чтобы получить приблизительный результат, разделите значение "Объем" на 3,785
    rezult = volume/3.785
    return rezult


def pintsConvertToLiters(volume):  # 11 Пинты в литры
    # Чтобы получить приблизительный результат, разделите значение "Объем" на 2,113
    rezult = volume/2.113
    return rezult


def litersConvertToPints(volume):  # Литры в пинты
    # Чтобы получить приблизительный результат, умножте значение "Объем" на 2,113
    rezult = volume*2.113
    return rezult
