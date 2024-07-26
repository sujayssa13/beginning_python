#calculate the area of the pentagon
import math
radius = eval(input("Enter the radius of pentagon :"))
#side calcualtion of a pentagon
s = 2*radius*(math.sin(math.pi/5))
#area calculation
area = (3*math.sqrt(3)*s*s/2)
print("The area of the pentagon is",format(area,".2f"))
