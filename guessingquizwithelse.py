import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)
 
if num1<num2:
     num1,num2 = num2,num1
    
answer = eval(input("What is " +str(num1) + " - " + str(num2) + "  = ?? :"))

if num1 - num2 == answer:
    print("Your answer is correct")
else:
    print("Your answer is wrong\n", num1," - ", num2, "is", num1-num2)
