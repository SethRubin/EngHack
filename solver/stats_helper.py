import math

def calculate_mean(arr):
    """calculates mean"""
    return sum(arr) / len(arr)

def calculate_stddev(arr):
    """returns the standard deviation of num"""
    mn = calculate_mean(arr)
    variance = sum([(e-mn)*(e-mn) for e in arr])/len(arr)
    return math.sqrt(variance)