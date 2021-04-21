from math import pi

def radians_to_degrees(n):
    return round(n * 180 / pi,2)

a = radians_to_degrees(1)

print(a)


