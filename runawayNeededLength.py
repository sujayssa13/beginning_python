#calculate the airport runway length 
velocity = eval(input("Enter the velocity of the aircraft :"))
acceleration = eval(input("Enter the acceleration of the aircraft :"))

runwayNeeded = velocity**2/(2*acceleration)

print("The minimum needed runway length is : ", runwayNeeded)
