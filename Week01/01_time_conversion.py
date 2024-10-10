def seconds_to_time(seconds):
    secondsInHour = 3600
    secondsInMinute = 60

    hours = seconds // secondsInHour
    seconds %= secondsInHour

    minutes = seconds // secondsInMinute

    seconds %= secondsInMinute

    return (hours, minutes, seconds)

print(seconds_to_time(0) == (0, 0, 0))
print(seconds_to_time(1) == (0, 0, 1))
print(seconds_to_time(69) == (0, 1, 9))
print(seconds_to_time(420) == (0, 7, 0))
print(seconds_to_time(3661) == (1, 1, 1))
print(seconds_to_time(86399) == (23, 59, 59))