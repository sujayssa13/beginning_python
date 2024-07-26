import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)

answer = eval(input("what is " + str(num1)+ "+ " + str(num2) + "? " ))

print(num1,"+", num2, "=", answer, " is ", num1+num2==answer)
