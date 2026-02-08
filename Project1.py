# Project 1. Number Guessing Game (CLI)


# Goal: Build a terminal game where the computer picks a number and the user guesses with

# feedback.

# Concepts: input/output, int conversion, while loop, random, conditionals

# Core tasks:

# • Generate a random integer in a range (e.g., 1-100).

# • Loop until the user guesses correctly or quits.

# • Validate input (non-numbers, out-of-range).

# • Track number of attempts and show a final score.

# Stretch goals:

# • Add difficulty modes (different ranges / max attempts).

# • Keep a high-score list in a file.


import random

num = random.randint(1, 100)
guesses = 0

while True:
    guess = input("Guess the number between 1 and 100: ")
    if guess == "exit":
        print("Game Exit!")
        break
    guess = int(guess)
    guesses += 1
    if guess < num:
        print("Your guess is less than the number")
    elif guess > num:
        print("Your guess is higher than the number")
    else:
        print(f"Congratulations! You guessed the number in {guesses} tries")
        break
