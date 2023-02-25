class Car():
    def __init__(self, brand, model, year, speed):
        """Машина
        Args:
            brand Марка
            model Модель
            year Год
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def display_info(self):
        return f"Марка: {self.brand}\nМодель:{self.model}\nГод:{self.year} Скорость: {self.speed}\n"

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def def_speed(self):
        self.speed = 0


car1 = Car("Марка тест", "Модель тест", 1997, speed=0)
car1.speed_up()
car1.def_speed()
print(car1.display_info())
