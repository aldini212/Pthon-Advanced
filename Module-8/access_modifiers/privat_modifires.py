class Myclass:
    def __init__(self):
        self.__private_variable = "This is a privat variable"

    def __private_method(self):
        print("This is a private method")

myclass = Myclass()
print(myclass.__private_variable)
print(myclass.__private_method())