import random
from hangman_words import word_list
import hangman_art 

print(hangman_art.logo)

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
guessed =  []

print(f'Pssst, the solution is {chosen_word}.')

#Here we have the empty display
display = []
for i in range(len(chosen_word)):
    display += "_" 


while not end_of_game:

    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
                
    if guess not in chosen_word:
        guessed.append(guess)
        print(f"\nThe letter that you have chosen is not in the word, you lose a life \n chosen letter list{guessed}")
        lives  -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")  
            
    if "_" not in display: #the key word (in) in a if allows us to see if a particular element exist inside a list 
        end_of_game = True
        print("You won")

    #stages will recive the data of lives as the index position
    print(hangman_art.stages[lives])
    print(display)                                  