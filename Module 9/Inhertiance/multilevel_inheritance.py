class Vehicle:
    def  __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year} ")

class Car(Vehicle):
    def __init__(self,make,model,year,body_style):
        super().__init__(make,model,year)
        self.body_style = body_style

class ElectricCar(Car):
    def __init__(self,make,model,year,body_style,battery_cappacity):
        super().__init__(make,model,year,body_style)
        self.battery_cappacity = battery_cappacity

    def charge(self):
        print("Charging the eletric car.")

tesla = ElectricCar("Tesla","CyberTruck",2023,"Triangular",222)
tesla.charge()
tesla.display_info()
print("Body Style",tesla.body_style)
print("Battery Capacity",tesla.battery_cappacity)

