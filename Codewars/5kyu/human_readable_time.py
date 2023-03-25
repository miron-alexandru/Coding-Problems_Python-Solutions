# Problem Link: https://www.codewars.com/kata/52685f7382004e774f0001f7



# My Solution:
def make_readable(seconds):
    # calculate the hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

    # format the time as a string
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
