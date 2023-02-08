class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))

p, q, r = 10, 20 ,30
print(p, q, r)

var = "James" * 2  * 3
print(var)



var= "James Bond"
print(var[2::-1])

print(5 ** 2)

