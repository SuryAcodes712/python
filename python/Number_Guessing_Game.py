import random

guesssNumber= random.randint(1,10)
print("Number Guessing Game")
print("Guess a number between 1 and 10")

while True:
    try:
        useeGuess=int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if useeGuess==guesssNumber:
        print("Congratulations! You guessed the number.")
        break
    elif useeGuess<guesssNumber:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")   
    