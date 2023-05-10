# All these results are in seconds
start_time = (6 * 60 + 52) * 60  # start_time is 6:52
easy_time = (
    8 * 60 + 15
) * 2  # miles run at easy pace is 8:15/mile & total 2 miles run at easy pace
tempo_time = 7 * 60 + 12  # miles run at tempo is 7:12/mile & total 3 miles run at tempo

# calculate the total time being run
breakfast_hour = (start_time + easy_time + tempo_time) / (
    60 * 60
)  # hours in double format
breakfast_int_hour = int(breakfast_hour)  # hours in int format

breakfast_minute = (
    breakfast_hour - breakfast_int_hour
) * 60  # minutes in double format
breakfast_int_minute = int(breakfast_minute)  # minutes in int format

# display the results
print("Breakfast is at {}.{}".format(breakfast_int_hour, breakfast_int_minute))
