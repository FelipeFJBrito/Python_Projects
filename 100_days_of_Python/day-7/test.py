import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
guess = input("Guess a letter: ").lower()

for i in chosen_word:
    display += "_" 
print(display)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# position will recive a number, that number will the position index
#When we say that letter = chosen_word[position], that means that letter is receving the data tha is in the position of index 0.

#At the first row we can see like that for example:
# we have camel as our word, and camel has 5 position 
# for position in range(0, 5): here position will recive what will be all position index of our word, so position at the firs row has position = 0

#at the second line letter will recive the letter that is in the [index position] that we passed to chosen_word,
# so letter will recive the letter that is in the position of index 0 of chosen_word: letter = chosen_word[position], in that case will be "c" 

#at the third line we will compare if the letter that we  got of the first position index [0] is == as the letter that we choose 
#if the letters are == , our display that is receving the same position index (in that case [0]), will take the data that exist in its position index and subistitute for the letter that we choose 

#guess = "c"
#chosen_word = camel
#for position in range(len(chosen_word)):   =>   for position in range(0,5):    
#letter = chosen_word[position]     =>      letter = chosen_word[0]     =>      "c" = chosen_word[0]
#if letter == guess:    =>  "c" == "c"
#display[position] = letter    =>   display[0] = "c"    =>    display[0] = ["index 0", "_", "_", "_", "_"] = "c"  display[0] = ["c", "_", "_", "_", "_"]
#and after that the code will repeat the process searching for more letters

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
  
                                                                                                               
         