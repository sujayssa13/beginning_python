#computing loan
annualInterestRate = eval(input("Enter the interest rate :"))

monthlyInterestRate = annualInterestRate/1200

numberOfYears = eval(input("Enter numbers of years :"))

loanAmount = eval(input("Enter loan amount :"))

monthlyPayment = loanAmount * monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))

totalPayment = monthlyPayment*numberOfYears*12

print("Monthly payment is", int(monthlyPayment*100)/100)
print("The total payment is", int(totalPayment*100)/100)
