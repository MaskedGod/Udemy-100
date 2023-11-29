import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_list = []
password = ""
i = 0

while i < nr_letters:
    pass_list.append(str(random.choice(letters)))
    i += 1
i = 0

while i < nr_symbols:
    pass_list.append(str(random.choice(symbols)))
    i += 1
i = 0

while i < nr_numbers:
    pass_list.append(str(random.choice(numbers)))
    i += 1

random.shuffle(pass_list)
for char in range(len(pass_list)-1):
    password += pass_list[char]

print(f"Your new password: \n{password}")