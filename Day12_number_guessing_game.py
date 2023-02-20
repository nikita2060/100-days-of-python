easy_attempt=10
hard_attempt=5
import art
import random
print(art.logo)
level=input("WELCOME TO NUMBER GUESSING GAME!!\nI am thinking of number between 1-100.\nChoose difficulty level:Easy or Hard\n")
def check_level():
  if level=="easy":
    return easy_attempt
  elif level=="hard":
    return hard_attempt
  else:
    print("Invalid  input!Try again.\n")
    return 0
target=random.randint(1,100)
count=0
attempt=check_level()
while attempt!=0:
  print(f"You have total {attempt} attempts left\n ")
  guess=int(input("Guess a number \n"))
  if target==guess:
    print(f"HURRAY YOU WON!!!The number was {target}.\n")
    count+=1
    break
  else:
    if guess>target:
      print("Too high!\nGuess again!")
    else:
      print("Too low!\nGuess again!")
    attempt-=1
if count==0:
  print(f"You lost!The number was {target}.")
