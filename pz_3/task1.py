import math


class Square:
    def __init__(self, l: float):
        self.l = l

    def perimeter(self) -> float:
        return 4 * self.l

    def area(self) -> float:
        return self.l ** 2

    def diagonal(self) -> float:
        return self.l * math.sqrt(2)


def main():
    square = Square(5)
    print("Периметр квадрата:", square.perimeter())
    print("Площадь квадрата:", square.area())
    print("Диагональ квадрата:", square.diagonal())


if __name__ == '__main__':
    main()
