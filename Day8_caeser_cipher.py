from art import logo
print(logo)

repeat = "yes"


def caesar_cipher(text, shift, direction):
    encoded_msg = ""
    alphabet = [chr(ord('a') + i)
                for i in range(26)]  # ASCII codes for lowercase letters

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            index1 = alphabet.index(char)
            # Using modulo to handle wrapping around the alphabet
            index2 = (index1 + shift) % 26
            encoded_msg += alphabet[index2]
        else:
            encoded_msg += char

    print(f"The encoded text is {encoded_msg}")


while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    repeat = input("Type 'yes' if you want to continue and 'no' if you want to end\n")
