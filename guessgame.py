#guess number
import random

number = random.randint(0,100)

guess = 0
while guess != number:
    guess = eval(input("Enter your guess: "))
    if guess == number:
      print("Yes the number is", number)
    elif guess>number:
      print("Your guess is too high")
    else:
      print("Your guess is too low")
