import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_MODE
    else:
        return HARD_MODE

def check_answer(user_guess , actual_guess , turns):
    if user_guess > actual_guess:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too low!")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_guess}!")

def game():
    print(logo)
    print("Welcome to GEUSS THE NUMBER game! ")
    answer = random.randint(0, 100)
    print("Im thinking of a number between 1 and 100.")
    turns = set_difficulty()
    guess = 0

    while guess != answer :
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
