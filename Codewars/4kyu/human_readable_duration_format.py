# Problem Link: https://www.codewars.com/kata/52742f58faf5485cae000b9a


# My Solution:
def format_duration(s):
    if s == 0:
        return "now"

    # Calculate seconds, minutes, hours, days, years
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day

    years = s // year
    s %= year
    days = s // day
    s %= day
    hours = s // hour
    s %= hour
    minutes = s // minute
    s %= minute

    duration = []
    if years > 0:
        duration.append("{} year{}".format(years, "" if years == 1 else "s"))
    if days > 0:
        duration.append("{} day{}".format(days, "" if days == 1 else "s"))
    if hours > 0:
        duration.append("{} hour{}".format(hours, "" if hours == 1 else "s"))
    if minutes > 0:
        duration.append("{} minute{}".format(minutes, "" if minutes == 1 else "s"))
    if s > 0:
        duration.append("{} second{}".format(s, "" if s == 1 else "s"))

    if len(duration) == 1:
        return duration[0]
    elif len(duration) == 2:
        return " and ".join(duration)
    else:
        return ", ".join(duration[:-1]) + " and " + duration[-1]
