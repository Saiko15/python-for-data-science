def my_max2(a, b):
    if a>b:
        return a
    return b

def my_max3(a, b, c):
    if my_max2(a, b) > c:
        return my_max2(a, b)
    return c

def my_max4(a, b, c, d):
    if my_max3(a, b, c) > d:
        return my_max3(a, b, c)
    return d

def my_max5(a, b, c, d, e):
    if my_max4(a, b, c, d) > e:
        return my_max4(a, b, c, d)
    return e

def my_max6(a, b, c, d, e, f):
    if my_max5(a, b, c, d, e) > f:
        return my_max5(a, b, c, d, e)
    return f

print(my_max6(5, 3, 8, 2, 10, 3))