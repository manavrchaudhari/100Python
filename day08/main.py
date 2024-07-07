from os import system
from time import sleep

alphabet = [
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
]


def caesar_cipher(direction, text, shift):
    coded_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index + shift) % 26
            new_char = alphabet[new_index]
            coded_text += new_char
        else:
            coded_text += char
    print(f"{direction}d text is :: {coded_text}")


do_continue = True
while do_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt :: \n"
    ).lower()
    text = input("Type your message :: \n").lower()
    shift = int(input("Type the shift number :: \n"))
    caesar_cipher(direction, text, shift)
    status = input("Do you want for a different text? [YES/EXIT] :: ").lower()
    if status == "exit":
        print("Have a good day 👋")
        sleep(2)
        do_continue = False
    system("clear")
