import math


def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    return a + b + c
