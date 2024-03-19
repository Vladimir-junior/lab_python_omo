class Faculty:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


class Student:
    def __init__(self, full_name: str, birth_year: int, result_exam: list[int]):
        self.full_name = full_name
        self.birth_year = birth_year
        self.result_exam = result_exam

    def get_full_name(self) -> str:
        return self.full_name

    def set_full_name(self, full_name: str) -> None:
        self.full_name = full_name

    def get_birth_year(self) -> int:
        return self.birth_year

    def set_birth_year(self, birth_year: int) -> None:
        self.birth_year = birth_year

    def get_exam_scores(self) -> list[int]:
        return self.result_exam

    def set_exam_scores(self, result_exam: list[int]) -> None:
        self.result_exam = result_exam

    def average_exam_score(self) -> float:
        return sum(self.result_exam) / len(self.result_exam)


def main():
    faculty = Faculty("Факультет Компьютерных Систем и Сетей")

    faculty.set_name("Факультета Информационной Безопасности")

    students_info = [
        {"full_name": "Борисенко Владимир Валерьевич", "birth_year": 2005, "result_scores": [5, 9, 7]},
        {"full_name": "Ваганова Арина Владленовна", "birth_year": 2005, "result_scores": [8, 9, 7]},
        {"full_name": "Драгун Егор Юрьевич", "birth_year": 2045, "result_scores": [7, 6, 8]}
    ]

    students = []
    for el in students_info:
        student = Student(el["full_name"], el["birth_year"], el["result_scores"])
        students.append(student)

    for i in students:
        print("Студент:", i.get_full_name())
        print("Год рождения:", i.get_birth_year())
        print("Результаты сессии:", i.get_exam_scores())
        print("Средний балл:", i.average_exam_score())




if __name__ == '__main__':
    main()

