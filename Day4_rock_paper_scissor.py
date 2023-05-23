import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

OPTIONS = {
    "rock": ROCK,
    "paper": PAPER,
    "scissors": SCISSORS
}


def get_user_choice():
    user_choice = input(
        "What do you choose? Rock, Paper, or Scissors? ").lower()
    while user_choice not in OPTIONS:
        print("Invalid choice. Please try again.")
        user_choice = input(
            "What do you choose? Rock, Paper, or Scissors? ").lower()
    return user_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "DRAW"
    if (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "YOU WIN"
    else:
        return "YOU LOSE"


def print_choices(user_choice, computer_choice):
    print(f"You chose:\n{OPTIONS[user_choice]}")
    print("Computer chose:\n")
    print(OPTIONS[computer_choice])


def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = random.choice(list(OPTIONS.keys()))
    print_choices(user_choice, computer_choice)
    winner = determine_winner(user_choice, computer_choice)
    print(winner)


play_game()
