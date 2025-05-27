class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:

        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f'{super().__str__()}, Record Book: {self.record_book}'

class Group:
    def __init__(self, number: str) -> None:
        self.number: str = number
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
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

    def __str__(self) -> str:
        all_students = '\n'.join(str(student) for student in self.students)
        return f'Group #{self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')