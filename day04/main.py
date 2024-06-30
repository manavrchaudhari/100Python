import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

symbols = [rock, paper, scissors]

print("0: Rock")
print("1: Paper")
print("2: Scissors")
user_choice = int(input("\nWhat do you choose?\n"))
computer_choice = random.randint(0, 2)
print("\nComputer chose..\n")
print(symbols[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid input given, you lose 😕")
elif user_choice == 0 and computer_choice == 2:
    print("You WIN 🎉")
elif computer_choice == 0 and user_choice == 2:
    print("You LOSE 😕")
elif user_choice > computer_choice:
    print("You WIN 🎉")
elif computer_choice > user_choice:
    print("You LOSE 😕")
elif computer_choice == user_choice:
    print("It's a DRAW ⛔️")
