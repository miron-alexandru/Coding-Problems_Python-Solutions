previous_num = 0

for i in range(1, 11):
    x_sum = previous_num + 1
    print(
        "Current number", i, "Previous Number ", previous_num, "Sum ", previous_num + i
    )
    previous_num = i
