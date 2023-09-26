class Student:
    def __init__(self, name: str, roll_number: str, cgpa: float):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
def sort_students(student_objects: list[Student]):
    sorted_student_objects = sorted(student_objects, key=lambda student: student.cgpa, reverse=True)

    return sorted_student_objects
student_objects1 = [
    Student("karthika", 123456, 9.5),
    Student("lavanya", 654321, 9.0),
    Student("gokul", 789012, 8.5),
]
student_objects2 = [
    Student("Jehabar", 345678, 8.0),
    Student("lino", 901234, 7.5),
    Student("shane", 567890, 7.0),
]
sorted_student_objects1 = sort_students(student_objects1)
sorted_student_objects2 = sort_students(student_objects2)
for student in sorted_student_objects1:
    print(f"{student.name}: {student.cgpa}")
for student in sorted_student_objects2:
    print(f"{student.name}: {student.cgpa}")
