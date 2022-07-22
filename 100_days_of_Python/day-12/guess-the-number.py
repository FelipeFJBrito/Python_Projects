import random
from art import logo

easy_level_turns = 10
hard_level_turns = 5
turns = 0

def choose_difficult():
    difficult = input("Choose a difficult. Type 'hard' or 'easy' ").lower()
    if difficult == "hard":
        return hard_level_turns
    elif difficult == "easy":
        return easy_level_turns       
    else:
        print("Not a valible word")


def compare_numbers(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        return f"You got it the answer is {answer}"

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pssst, the corect answer is {answer}")

    turns = choose_difficult()

    guess =  0
    while guess != answer:

        print(f"You have {turns} attempts")
        guess  = int(input("Make a guess: "))
        turns = compare_numbers(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
    
game()