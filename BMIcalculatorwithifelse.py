#compute BMI
weight = eval(input("Enter the weight in KG : "))
height = eval(input("Enter the height in CM : "))

BMI = weight/((height/100)**2)

#indexing BMI accoring to ratios
print("BMI is", format(BMI,".2f"))
if BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Over Weight")
else:
    print("Obese")
