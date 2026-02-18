import random

while True:
    print("Select difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Select difficulty: ")

    if choice == "1":
        max_num = 50
        tries = 10
        print("You have chosen Easy mode!")
        break
    elif choice == "2":
        max_num = 100
        tries = 7
        print("You have chosen Medium mode!")
        break
    elif choice == "3":
        max_num = 500
        tries = 5
        print("You have chosen Hard mode!")
        break
    else:
        print("Invalid choice. Try again.\n")

print("Game starting...")

number = random.randint(1, max_num)
attempts = 0

print("Welcome to the Guessing Game!")
print(f"I'm thinking of a number between 1 and {max_num}.")

while True:

    if attempts >= tries:
        print("You ran out of tries!")
        print("The number was", number)
        break

    while True:
        try:
            guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("Please type a number.")

    attempts += 1
    print("Attempts left:", tries - attempts)

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        print("You guessed it in", attempts, "tries!")
        break
