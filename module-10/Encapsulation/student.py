class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age #me set ja nderron emrin  e me get e vendos emrin#

student1 = Student ("Alice",17)
print("You'r Name:",student1.get_name())
print("You'r Age:",student1.get_age())


student1.set_name("Dini")
print("Uptadet name:", student1.get_name())

student1.set_age(19)
print("Uptadet age:", student1.get_age())

