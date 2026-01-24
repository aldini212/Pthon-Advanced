class person:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def greet(self):

        print(f"Hello,I am {self.name}, And I am {self.age} years old ")
person1 = person("Alice",24)
person2 = person("Bob",25)

person1.greet()

person2.greet()