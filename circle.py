import random
import numpy as np
from matplotlib import pyplot as plt

# to create a circle with center in (1,1) and radius 1 we need 2x2 square
a = 0
b = 2


# formula of a circle described earlier is (x - 1)^2 + (y - 1)^2 = 1
def f(x, y):
    return pow((x - 1), 2) + pow((y - 1), 2)


# if hit circle ok if not don't count
def aprox(n, a, b, m):
    c = 0
    for i in range(1, n + 1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        # if (x - 1)^2 + (y - 1)^2 <= 1 then (x, y) is in the circle
        if f(x, y) <= 1:
            c += 1
    # return aproximation of pi
    apr = (c / n) * (b - a) * m
    return apr


file1 = open("data.txt", "w")

for helper in range(1, 101):
    n = 50 * helper
    for k in range(1, 51):
        # saving data
        file1.write(str(aprox(n, a, b, 2)))
        file1.write("\n")



