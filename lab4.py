class Ship:
    """Клас «Корабель»."""

    def __init__(self, tonnage=0.0, name="Невідомо", passengers_count=0,
                 ship_id=0, ship_type="Невідомо"):

        self.__tonnage = tonnage
        self.__name = name
        self.__passengers_count = passengers_count
        self.ship_type = ship_type

        self.ship_id = ship_id


    def get_tonnage(self):
        return self.__tonnage

    def get_name(self):
        return self.__name

    def get_passengers_count(self):
        return self.__passengers_count

    def set_tonnage(self, tonnage):
        self.__tonnage = tonnage

    def set_name(self, name):
        self.__name = name

    def set_passengers_count(self, passengers_count):
        self.__passengers_count = passengers_count

    def __str__(self):
        return (f"Корабель «{self.__name}»: тонаж = {self.__tonnage}, "
                f"пасажирів = {self.__passengers_count}, "
                f"id = {self.ship_id}, тип = {self.ship_type}")

    def __repr__(self):
        return (f"Ship(tonnage={self.__tonnage!r}, name={self.__name!r}, "
                f"passengers_count={self.__passengers_count!r}, "
                f"ship_id={self.ship_id!r}, ship_type={self.ship_type!r})")

    def __del__(self):
        print(f"Об'єкт «{self.__name}» знищено")


def main():
    ship1 = Ship()
    ship2 = Ship(50000, "Титанік", 2435, 1, "Лайнер")
    ship3 = Ship(12000.5, "Одеса", 800, 2, "Пором")
    ship4 = Ship(12000.5, "Одеса", 800, 2, "Пором")

    ship4.set_name("Титанік")




    for ship in (ship1, ship2, ship3, ship4):
        print("Назва:", ship.get_name())
        print("Тонаж:", ship.get_tonnage())
        print("Кількість пасажирів:", ship.get_passengers_count())
        print("ID:", ship.ship_id)
        #//print("Тип:", ship.ship_type)//#
        print("str:", str(ship))
        print("repr:", repr(ship))
        print("-" * 40)




if __name__ == "__main__":
    main()