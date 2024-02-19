import datetime

class Car:

    total_cars = 0

    def __init__(self, id_car, make, model, year, color):
        self.id_car = id_car
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Car.total_cars += 1


    def display_info(self):
        return f"id_car: {self.id_car}, {self.year} {self.make} {self.model}, {self.color}"


    @staticmethod
    def number_of_years(year_car):
        date = datetime.datetime.now()
        year_n = date.year
        return year_n - year_car


    @classmethod
    def display_total_cars(cls):
        return f"Всего автомобилей: {cls.total_cars}"







def main():
    car1 = Car(12, "Mercedes", "CLS", 2019, "черный")
    car2 = Car(34, "BMW", "X5", 2017, "серебристый")
    car3 = Car(2, "AUDI", "Q7", 2021, "красный")
    print(car1.display_info())
    print(car2.display_info())
    print(f"Автомобилю:{Car.number_of_years(2019)} лет.")
    print(Car.display_total_cars())


if __name__ == '__main__':
    main()
