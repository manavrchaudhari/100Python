import random
from os import system
from time import sleep
from art import logo, stages
from words import word_list

lives = 6
game_over = False
print(logo)

guessed_list = []
selected_word = random.choice(word_list)
len_selected_word = len(selected_word)
for char in selected_word:
    guessed_list += "_"
print(f"\nThe word is of length {len_selected_word} characters\n")

while not game_over:
    user_guess = input("\nMake your guess :: ").lower()

    if user_guess in guessed_list:
        print("\nYou have already made the guess.")

    # If guess is correct replace blank with the guessed character
    for char in range(len_selected_word):
        if user_guess == selected_word[char]:
            guessed_list[char] = user_guess

    # If incorrect guess, reduce lives
    if user_guess not in selected_word:
        lives -= 1
        print("Looks like you made wrong guess. You lose a life.")
        if lives == 0:
            game_over = True
            print("YOU LOSE 😕")

    if "_" not in guessed_list:
        game_over = True
        print("YOU WON 🎉")

    print(stages[lives])
    print(f"\n{' '.join(guessed_list)}")
    sleep(3)
    system("clear")
