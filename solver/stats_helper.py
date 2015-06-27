import math

def calculate_mean(num):
    """calculates mean"""
    return sum(num) / len(num)

def calculate_stddev(num):
    """returns the standard deviation of num"""
    mn = calculate_mean(num)
    variance = sum([(e-mn)**2 for e in num])
    return math.sqrt(variance)