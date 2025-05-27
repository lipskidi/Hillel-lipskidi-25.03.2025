class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:

        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

class Group:
    def __init__(self, number: str) -> None:
        self.number: str = number
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        if len(self.students) >= 10:
            raise GroupIsFullException()
        if self.find_student(student.last_name) is None:
            self.students.append(student)

    def find_student(self, last_name: str) -> str | None:
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

class GroupIsFullException(Exception):
    def __init__(self, message="Група переповнена."):
        super().__init__(message)

group = Group("ІТ-01")

try:
    for i in range(11):
        student = Student("male", 20, f"Name{i}", f"Surname{i}", f"RB{i}")
        group.add_student(student)
except GroupIsFullException as e:
    print(e)