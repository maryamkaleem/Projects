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

print("Select Difficulty: ")
print("1. Easy (1 - 10)")
print("2. Medium (1 - 50)")
print("3. Hard (1 - 100)")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    max_range = 10
elif choice == "2":
    max_range = 50
else:
    max_range = 100

num = random.randint(1, max_range)
guesses = 0

while True:
    guess = input("Guess the number between 1 and {max_range} (or type 'exit'): ")
    if guess == "exit":
        print("Game Exit!")
        break

    if not guess.isdigit():
        print("Enter numbers only")
        continue

    guess = int(guess)

    if guess < 1 or guess > max_range:
        print("Number is out of range")
        continue

    guesses += 1
    if guess < num:
        print("Your guess is less than the number")
    elif guess > num:
        print("Your guess is higher than the number")
    else:
        print(f"Congratulations! You guessed the number in {guesses} tries")
        break
