import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:

    while True:
        try:
            guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("Please type a number.")

    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        print("You guessed it in", attempts, "tries!")
        break
