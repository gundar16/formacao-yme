import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 50.")
    print("Take turns guessing until someone gets it right!\n")

    # Generate a random number between 0 and 50
    secret_number = random.randint(0, 50)

    # Keep track of how many guesses have been made
    attempts = 0

    while True:
        guess = input("Enter your guess (0-50): ")

        # Validate the input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 0 or guess > 50:
            print("That number is out of range! Try again.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"It took {attempts} attempts to guess correctly.")
            break

guessing_game()