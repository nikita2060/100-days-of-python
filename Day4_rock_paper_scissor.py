import random

# Constants for the options
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
    user_choice = input("What do you choose? Rock, Paper, or Scissors? ").lower()
    while user_choice not in OPTIONS:
        print("Invalid choice. Please try again.")
        user_choice = input("What do you choose? Rock, Paper, or Scissors? ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(list(OPTIONS.keys()))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "DRAW"
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    if win_conditions[user_choice] == computer_choice:
        return "YOU WIN"
    else:
        return "YOU LOSE"

def print_choices(user_choice, computer_choice):
    print(f"You chose:\n{OPTIONS[user_choice]}")
    print(f"Computer chose:\n{OPTIONS[computer_choice]}")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print_choices(user_choice, computer_choice)
    winner = determine_winner(user_choice, computer_choice)
    print(winner)

if __name__ == "__main__":
    play_game()
