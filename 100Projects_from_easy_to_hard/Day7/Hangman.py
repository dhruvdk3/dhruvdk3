import os
import random
from words import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
print("Welcome to hangman. Here you have total of 6 lives. If you are able to guess the word correctly without loosing all the lives you will win. Otherwise its you loss.\nGood Luck")
chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



display = []
for _ in range(len(chosen_word)):
    display.append("_")

lives = 6
while (True):
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    i= 0
    if guess in chosen_word:
        for letter in chosen_word:
            if letter == guess:
                display.pop(i)
                display.insert(i, letter)
                i += 1
            else:
                i += 1
        print(stages[lives])
    else :
        lives-=1
        print(f"\n{guess} wasn't in the letter. you lost one life")
        print(f"Lives remaining : {lives}")
        print(stages[lives])
        if lives == 0:
            print("You lost")
            break


    print(display)
    if "_" not in display:
        print("You Won.")
        break
