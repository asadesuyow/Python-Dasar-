class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car Class
boat1 = Boat("Ibiza", "Tour20") #Create a Boat Class
plane1 = Plane("Boeing", "747") #Create a Plane Class

for x in (car1, boat1, plane1):
    x.move()
    