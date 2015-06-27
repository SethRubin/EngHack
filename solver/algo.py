from average_time import get_past_average_times
from stats_helper import calculate_mean, calculate_stddev

def is_current_min(past_average_times, current):
    min_time = current
    for i in range(0, len(past_average_times)):
        if past_average_times[i] <= min_time:
            return False
    return True

def is_current_in_second_std_dev(past_average_times, current):
    mean = calculate_mean(past_average_times)
    stddev = calculate_stddev(past_average_times)
    return (current >= mean - 2*stddev) and (current <= mean + 2*stddev)

def solver(word):
    average_times = get_past_average_times(word)
    print average_times
    past_average_times = average_times[1:]
    if average_times[0] == None:
        return False
    if average_times[1] == None:
        return True
    a = is_current_min(past_average_times, average_times[0])
    b = is_current_in_second_std_dev(past_average_times, average_times[0])
    return a and not b

x = solver("marriage")
print(x)
