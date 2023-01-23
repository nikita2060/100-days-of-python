from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

repeat="yes"
def caeser(text,shift,direction):
  encoded_msg=""
  if(direction=="decode"):
    shift*=-1
  for char in text:
    if char in alphabet:
      index1 = alphabet.index(char)
      index2=index1+shift
      if index2>26:
        index2-=26
      encoded_msg+=alphabet[index2]
    else:
      encoded_msg+=char
  print(f"The encoded text is {encoded_msg}")
    
while repeat=="yes":
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))
 caeser(text,shift,direction)
 repeat=input("Type 'yes' if you want to continue and 'no' if you want to end\n") 
 
