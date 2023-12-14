#P5HW
#25 November 2023
#CTI-110 P5HW - Math Quiz
#Nadia Epps
#

print("Welcome to Math Quiz")

import random

def math_quiz():
    random1 = random.randint(1, 250)
    random2 = random.randint(1, 250)
    answer = random1 + random2
    guess = int(input(f"  {random1}\n + {random2}\n"))
    num_guess = 1

    while guess != answer:
        if guess < answer:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input())
        num_guess += 1

    print(f"Congratulations! You got the correct answer in {num_guess} guesses.")

math_quiz()

