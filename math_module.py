def factorial(n):
    result = 1
    for number in range(1 , n + 1):
        result = result * number
    return result
def module(x):
    if x < 0:
        x = -x
    else:
        x = x
    return x