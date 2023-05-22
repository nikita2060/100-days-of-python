# Password Generator Project
import random
import string


def generate_password(num_letters, num_symbols, num_numbers, strength='medium'):
    """Generate a random password with the given number of letters, symbols, and numbers, and specified strength."""
    password_chars = []
    password_chars.extend(random.choices(
        string.ascii_lowercase, k=num_letters))

    if strength == 'medium' or strength == 'hard':
        password_chars.extend(random.choices(
            string.ascii_uppercase, k=num_letters//2))
    if strength == 'hard':
        password_chars.extend(random.choices(string.digits, k=num_numbers//2))

    password_chars.extend(random.choices(string.punctuation, k=num_symbols))

    random.shuffle(password_chars)
    return ''.join(password_chars)


print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))
strength = input(
    "What strength of password would you like? (weak/medium/hard)\n")

password = generate_password(num_letters, num_symbols, num_numbers, strength)
print(f"Your password is: {password}")