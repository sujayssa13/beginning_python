#selection statments
import math

radius = eval(input("Enter radius of the circle: "))

if radius < 0:
    print("Incorrect input")
else:
    area = radius*radius*math.pi
    print("Area is", format(area,".2f"))
