# Number Guessing Game

# Python has a built-in module that we can use to make random numbers.
import random # Importing random module

# Taking User Input for lower bound values
lower = int(input("Enter lower bound: "))
# Taking User Input for upper bound values 
upper = int(input("Enter upper bound: "))

x = random.randint(lower,upper) # randint function returns a random function between the given range.

# Taking User Input for first number to guess:
user_n = int(input("Enter your guessed number:"))

while user_n != x:
    if(x<user_n):
        print("You Guessed high number, Try again :) ")
    else:
        print("You Guessed smaller number, Try again :) ")
    
    user_n = int(input("Enter your guessed number:"))

if(x==user_n):
    print("Congratulations you did it :) ")
    print("Number was:", x)

    