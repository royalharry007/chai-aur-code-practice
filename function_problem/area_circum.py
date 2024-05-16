import math

def area(radius):
    area= math.pi*radius**2
    circumference = 2*math.pi*radius
    return area, circumference

result1,result2 = area(5)
print(round(result1,2))
print(round(result2,2))


