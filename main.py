#HANGMAN GAME USING PYTHON

import random
import hangman_words
from hangman_arts import logo,stages
from replit import clear
#printing logo
print(logo)
chosen_word = random.choice(hangman_words.word_list)


#Create blanks
display=[]
for letter in chosen_word:
  display.append("_")
print(display)

#checking user's input
lives=6
end_of_game=False
while not end_of_game:
  guess = input("\n\nGuess a letter: ").lower()
  clear()
  
  if guess not in display:
    i=0
    number_of_displacement=0
    for letter in chosen_word:
      if letter == guess:
        display[i]=letter
        number_of_displacement+=1
          
      i+=1
  else:
    print(f"\nYou have already guessed the letter '{guess} '! Try another one.")
  if number_of_displacement==0:
    print(f"\nOOPS! You guessed '{guess}' which is not in the word\n")
    lives=lives-1
  print(display) 
  print(stages[lives])
  #checking if game should end or continue
  if "_" not in display:
    end_of_game=True
    print("YOU WON!!!!!!!\n");
  if lives==0:
    end_of_game=True
    print("YOU LOST!!!!!!")
    print(f"\nThe word was {chosen_word}!")
