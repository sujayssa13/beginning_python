#bodymassindex
weight = eval(input("Enter the weight in KG :"))
height = eval(input("Enter height in CM :"))
HeightInMeters = height/100

BMI = weight/(HeightInMeters**2)
print("BMI for ",weight,"KG","and", height,"cm is :", BMI)
