rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user=input("What do you choose Rock ,Paper, Scissors?\n ").lower()
if(user=="rock"):
  print(rock)
elif(user=="scissors"):
  print(scissors)
else:
  print(paper)
list=[rock,paper,scissors]
computer=random.choice(list)
print("Computer chose:\n")
if(computer==rock):
  print(rock)
elif(computer==scissors):
  print(scissors)
else:
  print(paper)
#possible conditions
if(computer==rock and user=="paper"):
  print("YOU LOSE!")
elif(computer==paper and user=="rock"):
  print("YOU WIN!")
elif(computer==rock and user=="scissors"):
  print("YOU LOSE!")
elif(computer==scissors and user=="rock"):
  print("YOU WIN!")
elif(computer==scissors and user=="paper"):
  print("YOU LOSE!")
elif(computer==paper and user=="scissors"):
  print("YOU WIN!")
else:
  print("DRAW!!!")
