grades = {
    ("John", "Math"): 2,
    ("violet", "art"): 4,
    ("Adam", "history"): 5,
    ("Einstain", "Physics"): 5
}

john_math = grades["John", "Math"]
print("The grade of john in math is", john_math)

grades[("Florjon", "Edukate fizike")] = 5

print(grades)

keys = list(grades.keys())
print(keys)

student, subject = keys[0]
print(student,"'s grade in",subject, "is", john_math)