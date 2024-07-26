#converting entered number from number of seconds to minutes, hours, days and weeks
seconds = eval(input("Enter a number that indicates number of seconds : "))
inMinutes = seconds/60
print("Minutes is : ", inMinutes)
inHours = inMinutes/60
print("in hours is : ", inHours)
inDays = inHours/24
print("In days : ",inDays)
