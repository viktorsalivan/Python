class DC():
    """
     Описание DC:
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
        print(
            f"Имя: {self.__name}\tОружия: {self.__weapon}\tСила: {self.__power}")
