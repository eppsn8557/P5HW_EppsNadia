#P5HW
#25 November 2023
#CTI-110 P5HW - Math Quiz
#Nadia Epps
#

print("Welcome to Math Quiz")

import random

def generate_numbers():
    num1 = random.randint(1, 250)
    num2 = random.randint(1, 250)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    print(f" {num1}\n + {num2}\n")
    guess = int(input("Enter answer.\n"))
    num_guess = 1
    result = num1 + num2
    while True:
        if guess == result:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {num_guess}")
            break
        elif guess > result:
            print("Sorry, guess is too high.")
            guess = int(input("Try again: "))
        else:
            print("Sorry, guess is too low.")
            guess = int(input("Try again: "))
        num_guess += 1

def subtract_numbers():
    num1, num2 = generate_numbers()
    print(f" {num1}\n - {num2}\n")
    guess = int(input("Enter answer.\n"))
    num_guess = 1
    result = num1 - num2
    while True:
        if guess == result:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {num_guess}")
            break
        elif guess > result:
            print("Sorry, guess is too high.")
            guess = int(input("Try again: "))
        else:
            print("Sorry, guess is too low.")
            guess = int(input("Try again: "))
        num_guess += 1

def display_menu():
    print()
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    
def math_quiz():
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice =="1":
            add_numbers()
        elif choice =="2":
            subtract_numbers()
        elif choice == "3":
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please try again.")
math_quiz()

    


