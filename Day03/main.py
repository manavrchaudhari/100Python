print("⭐️ Welcome to Treasure Island ⭐️")

choice1 = input('You\'re at a cross road. Where do you want to go? [LEFT / RIGHT] \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. [SWIM / WAIT] \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. Which color do you choose? [RED / YELLOW / BLUE]\n").lower()
    if choice3 == "red":
      print("It's a room full of fire 🔥 Game Over ☠️")
    elif choice3 == "yellow":
      print("You found the treasure 🎉 You Win 🎉")
    elif choice3 == "blue":
      print("You enter a room of beasts 👹 Game Over ☠️")
    else:
      print("You chose a door that doesn't exist! Game Over ☠️")
  else:
    print("You get attacked by an angry trout! Game Over 👹")
else:
  print("You fell into a hole! Game Over ☠️")