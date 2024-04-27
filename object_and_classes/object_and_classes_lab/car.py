class Vehicle:

    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age

    def info(self):
        return f"{self.brand} - {self.model} from {self.age}"


car = Vehicle("Mercedes", "SL500", 1994)
print(car.info())
