def add_time(start, duration, day=None):
    DAYS = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]

    start_hour, start_min = start.split()[0].split(":")
    period = start.split()[1]
    if period == "PM":
        start_hour = int(start_hour) + 12
    else:
        start_hour = int(start_hour)
    start_min = int(start_min)

    duration_hour, duration_minute = duration.split(":")
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)
    end_min = start_min + duration_minute
    end_hour = start_hour + duration_hour
    end_day = 0

    end_hour = end_hour + (end_min // 60)
    end_min = end_min % 60
    end_day = end_day + (end_hour // 24)
    end_hour = end_hour % 24

    if end_hour > 12:
        end_hour = end_hour - 12
        end_period = "PM"
    elif end_hour == 12:
        end_period = "PM"
    elif end_hour == 0:
        end_hour = 12
        end_period = "AM"
    else:
        end_period = "AM"

    new_time = "{}:{:02d} {}".format(end_hour, end_min, end_period)

    if day:
        new_time += ", " + DAYS[(DAYS.index(day.lower()) + end_day) % 7].title()

    # If end_day > 0, add the number of days
    if end_day > 0:
        if end_day == 1:
            new_time += " (next day)"
        else:
            new_time += " ({} days later)".format(end_day)

    return new_time
