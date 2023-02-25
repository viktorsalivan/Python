from tkinter import Spinbox


class TMNT():
    """
     Описание TMNT:
     name - имя
     weapon - оржие
     power - сила
     """

    def __init__(self, name, weapon, power):
        """Constructor"""
        self.__name = name
        self.__weapon = weapon
        self.__power = power

    # Геттор и сеттор для имя
    def getName(self):
        return self.__name

    def setWeapon(self, value):
        self.__name = value

    # Геттор и сеттор для оружия
    def getWeapon(self):
        return self.__weapon

    def setWeapon(self, value):
        self.__weapon = value

    # Геттор и сеттор для сила
    def getPower(self):
        return self.__power

    def setPower(self, value):
        self.__power = value
# Методы

    def display_info(self):
        return f"Имя: {self.__name}\nОружия:{self.__weapon}\nСила:{self.__power}\n"


leonardo = TMNT("Леонардо", "Катана", "90")
print(leonardo.display_info())
donotello = TMNT("Донотелло", "Бо", 70)
print(donotello.display_info())
micilangelo = TMNT("Микиланжело", "Нунчаки", "50")
print(micilangelo.display_info())
rafael = TMNT("Рафаэль", "Саи", "90")
splinter = TMNT("Сплинтер", "Палка", "100")
print(splinter.display_info())
