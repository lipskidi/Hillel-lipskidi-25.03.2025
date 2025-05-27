from Student import Student

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