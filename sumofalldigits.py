#extractinng digits
number = eval(input("Enter a four digit number : "))
fourth_digit = number//1000
thirdRemainder = number%1000

print("4th digit:", fourth_digit)
#print("thirdRemainder",thirdRemainder)
third_digit = thirdRemainder//100
print("3rd digit", third_digit)

second_digit = thirdRemainder%100
print("2nd digit", second_digit//10)
print("1st digit", second_digit%10)

sum_of_all_digits = fourth_digit + third_digit + second_digit//10 + second_digit%10

print("sum of all digits",sum_of_all_digits)
