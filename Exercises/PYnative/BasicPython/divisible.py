def divisible_by(numbers):
	for i in numbers:
		if i % 5 == 0:
			print(i)

numbers = [10, 20, 33, 46, 55]
print(divisible_by(numbers))