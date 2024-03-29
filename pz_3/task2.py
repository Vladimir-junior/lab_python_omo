class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self) -> None:
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self) -> None:
        super().draw()
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self) -> None:
        super().draw()
        print("Отрисовка карандашом")


class Handle(Stationery):
    def draw(self) -> None:
        super().draw()
        print("Отрисовка маркером")


def main():
    pen = Pen("Ручка")
    pen.draw()

    pencil = Pencil("Карандаш")
    pencil.draw()

    handle = Handle("Маркер")
    handle.draw()



if __name__ == '__main__':
    main()



