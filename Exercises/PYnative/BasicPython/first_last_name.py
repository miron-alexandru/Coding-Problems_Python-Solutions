def first_last_same(number_list):
	first_num = number_list[0]
	last_num = number_list[-1]

	if first_num == last_num:
		return True
	else:
		return False

l1 = [10, 20, 30, 40, 10]
print(first_last_same(l1))

l2 = [75, 20, 30, 40, 10]
print(first_last_same(l2))