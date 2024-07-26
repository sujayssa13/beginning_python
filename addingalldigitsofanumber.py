#sum of all digits entered
# example
number = eval(input("Enter a number between 100 to 999: "))

#extracting tenth digit
zero_digit = number%10
print("zero digit :",zero_digit)
tenth_digit = number//10
print("tenth_digit :",tenth_digit%10)
hundreth_digit = number//100
print("hundreth_digit :",hundreth_digit)

sum_of_all_digit = zero_digit + tenth_digit%10+ hundreth_digit
print("Sum of all digits is :", sum_of_all_digit)
