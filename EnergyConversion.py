# computation of energy to  heat the water
waterWeight = eval(input("Enter the water in Kg :"))
initialTemp = eval(input("Please write the Initial tempreature: "))
finalTemp = eval(input("Please write the and Final tempreature: "))
energyNeeded = waterWeight * (finalTemp-initialTemp)*4184
print("Energy needed is", energyNeeded)
