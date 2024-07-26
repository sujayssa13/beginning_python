#area of a triangle
x1,y1,x2,y2,x3,y3 = eval(input("Enter the points of triangle: "))

side1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
side2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
side3 = ((x3-x1)**2 + (y3-y1)**2)**0.5

side = (side1 + side2 + side3)/2

area = ((side*(side-side1)*(side-side2)*(side-side3))**0.5)
print("Area of the triangle is :", area)
