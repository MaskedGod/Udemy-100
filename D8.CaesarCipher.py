alphabet = "abcdefghijklmnopqrstuvwxyz"

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    finished_text = ""
    for char in text:
        if char in alphabet:
            character_place = alphabet.find(char)
            if direction == "encode":
                finished_text += alphabet[(character_place + shift) % 26]
            else:
                finished_text += alphabet[(character_place - shift) % 26]
        else:
            finished_text += char
    print(finished_text)

caesar(text, shift, direction)