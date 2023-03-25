class Vehicle():
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage

v1 = Vehicle(300, 20)
print(v1.max_speed, v1.mileage)

class Vehicle():
	pass

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Buss(Vehicle):
	pass



b1 = Buss('School Volvo', 180, 12)
print('Vehicle Name:', b1.name, 'Speed:', b1.max_speed, 'Mileage:', b1.mileage)
print()

