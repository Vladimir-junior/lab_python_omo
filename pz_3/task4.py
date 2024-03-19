import datetime
from uuid import uuid4

class Car:

    total_cars = 0

    def __init__(self, brand: str, model: str, year: int, color: str):
        self.id_car = str(uuid4())
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self._incr_total_cars()

    @classmethod
    def _incr_total_cars(cls) -> None:
        cls.total_cars += 1

    def display_info(self) -> str:
        return f"id_car: {self.id_car}, {self.year} {self.brand} {self.model}, {self.color}"


    @staticmethod
    def number_of_years(year_car: int) -> int:
        date = datetime.datetime.now()
        year_n = date.year
        return year_n - year_car


    @classmethod
    def display_total_cars(cls) -> str:
        return f"Всего автомобилей: {cls.total_cars}"


def main():
    car1 = Car("Mercedes", "CLS", 2019, "черный")
    car2 = Car("BMW", "X5", 2017, "серебристый")
    car3 = Car("AUDI", "Q7", 2021, "красный")
    print(car1.display_info())
    print(f"Автомобилю:{Car.number_of_years(2018)} лет.")
    print(car2.display_info())
    print(f"Автомобилю:{Car.number_of_years(2012)} лет.")
    print(car3.display_info())
    print(f"Автомобилю:{Car.number_of_years(2019)} лет.")
    print(Car.display_total_cars())


if __name__ == '__main__':
    main()
