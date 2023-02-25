from simple_console_menu import Menu

from App.task1 import *

menuNumber = Menu.SimpleConsoleMenu(
    'Menu', ["Дюймы в сантиметры", "Сантиметры в дюймы", "Мили в километры", "Километры в мили", "Фунты в килограммы", "Килограммы в фунты", "Унции в граммы", "Граммы в унции", "Галлон в литры", "Литры в галлоны", "Пинты в литры", "Литры в пинты"], "Number:", 112, True)

if menuNumber == 1:
    length = int(input("Ввидите длину : "))
    temp = inchesConvertTOcentimeters(length)
    print(temp)
elif menuNumber == 2:
    length = int(input("Ввидите длину : "))
    temp = centimeterConvertTOInches(length)
    print(temp)
elif menuNumber == 3:
    length = int(input("Ввидите длину : "))
    temp = milesConvertTOkilometers(length)
    print(temp)
elif menuNumber == 4:
    length = int(input("Ввидите длину : "))
    temp = kilometersConvertToMiles(length)
    print(temp)
elif menuNumber == 5:
    massa = int(input("Ввидите массу : "))
    temp = poundsConvertToKilograms(massa)
    print(temp)
elif menuNumber == 6:
    massa = int(input("Ввидите массу : "))
    temp = kilogramsConvertToPounds(massa)
    print(temp)
elif menuNumber == 7:
    massa = int(input("Ввидите массу : "))
    temp = ouncesConvertToGrams(massa)
    print(temp)
elif menuNumber == 8:
    massa = int(input("Ввидите массу : "))
    temp = gramsConvertToOunces(massa)
    print(temp)
elif menuNumber == 9:
    volume = int(input("Ввидите объём : "))
    temp = gallonConvertTOliters(volume)
    print(temp)
elif menuNumber == 10:
    volume = int(input("Ввидите объём : "))
    temp = litersConvertToGallons(volume)
    print(temp)
elif menuNumber == 11:
    volume = int(input("Ввидите объём : "))
    temp = pintsConvertToLiters(volume)
    print(temp)
elif menuNumber == 12:
    volume = int(input("Ввидите объём : "))
    temp = litersConvertToPints(volume)
    print(temp)
