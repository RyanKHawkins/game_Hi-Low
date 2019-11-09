# Hi/Low
# Created 6/29/2019
# Creator:  Ryan Hawkins

import random

title = "HI/LOW"
title_space = (" "*(len(title)//2))

print("-" * (len(title) * 2))
print(f"{title_space}{title}")
print("-" * (len(title) * 2))

keep_going = True
tries = 0
secret_number = random.randint(1, 11)

print()
while keep_going and tries < 5:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("You win.")
        break
    elif guess > secret_number:
        print("Too high. Guess lower.")
    elif guess < secret_number:
        print("Too low. Guess higher.")

    tries += 1

if tries > 5:
    print("Too many tries. You lost.")
else:
    print(f"Contratulations. You guessed the number in {tries} tries.")
