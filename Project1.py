# Project 1. Number Guessing Game (CLI)

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

        try:
            file = open("highscore.txt", "r")
            best_score = int(file.read())
            file.close()
        except:
            best_score = guesses

            if guesses <= best_score:
                file = open("highscore.txt", "w")
                file.write(str(guesses))
                file.close()
                print("New High Score!")
            else:
                print("Best Score is", best_score)

                break
