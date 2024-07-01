import random
from os import system

system("clear")

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

letters_count = int(input("How many letters would you like?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(letters_count):
    password_list.append(random.choice(letters))
for char in range(symbols_count):
    password_list.append(random.choice(symbols))
for char in range(numbers_count):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password_str = ""
for char in password_list:
    password_str += char
print(f"Generated password is: {password_str}")