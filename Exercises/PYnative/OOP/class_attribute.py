class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print(
    School_bus.color,
    School_bus.name,
    "Speed:",
    School_bus.max_speed,
    "Mileage:",
    School_bus.mileage,
)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
