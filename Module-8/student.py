class student:

    school_name = "Digital School"

    def __init__(self, name, age, course):

        self.name = name
        self.age = age
        self.course = course

student_1 = student("Alice", 15, "Python")

student_2 = student("Bob", 16, "JavaScript")

print(student_1.course, student_1.age)

print(student_2.course)