class Faculty:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def rename_faculty(self, name):
        self.name = name


class Student:
    def __init__(self, full_name, birth_year, result_exam):
        self.full_name = full_name
        self.birth_year = birth_year
        self.result_exam = result_exam

    def get_full_name(self):
        return self.full_name

    def rename_full_name(self, full_name):
        self.full_name = full_name

    def get_birth_year(self):
        return self.birth_year

    def rename_birth_year(self, birth_year):
        self.birth_year = birth_year

    def get_exam_scores(self):
        return self.result_exam

    def rename_exam_scores(self, result_exam):
        self.result_exam = result_exam

    def average_exam_score(self):
        return sum(self.result_exam) / len(self.result_exam)


def main():
    faculty = Faculty("Факультет Компьютерных Систем и Сетей")

    faculty.rename_faculty("Факультета Информационной Безопасности")

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

