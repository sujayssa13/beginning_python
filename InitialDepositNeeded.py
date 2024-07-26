#Financial applciation for detailing initial deposit needed
final_amount = eval(input("Enter the final amount needed : "))
annualInterestRate = eval(input("Enter the annual interest rate : "))
yearsNeeded = eval(input("Enter years needed : ")) 

monthlyInterestRate = (annualInterestRate/52)/100
numberOfMonths = yearsNeeded*52

initialDeposit = ((final_amount)/((1+monthlyInterestRate)**numberOfMonths))
print("Initial deposit needed : ", initialDeposit)
