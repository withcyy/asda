class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

student1 = Student("Bob", 16, 100)
student1.add_course("AI")
student1.add_course("Math")

print(f"Student: {student1.name}, Age: {student1.age}, Grade: {student1.grade}, Courses: {student1.courses}")
