class Square:
    def __init__(self):
        self._length = "this varibale is with length 5 guy"
    def _area(self):
        return self._length * self._length

square = Square()
print(square._length)