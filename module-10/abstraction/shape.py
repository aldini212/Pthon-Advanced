from abc import ABC, abstractmethod

class Shape(ABC):


    @abstractmethod
    def area(self):
        pass


class  Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(7)
print(circle.area())


class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length * self.length

square = Square(2)
print(square.area())