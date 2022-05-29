print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_move = input('You are at a crossroad.  Where do you want to go? Type "left" or "right".\n').lower()

#first move choice
if first_move == "left":
  second_move = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()

  if second_move == "wait":
    third_move = input("You arrive at the island unharmed. There is a house with 3 doors.  One red, one yellow and one blue. Which color do you choose?\n").lower()

    if third_move == "red":
      print("You found the hidden treasure!  You win!!")

    elif third_move == "yellow":
      print("You enter a room full of beasts. Game over!")

    elif third_move == "blue":
      print("It's a room full of fire. Game over!")

    else:
      print("You chose a door that doesn't exist and floated away into the abyss! Game Over!")

  else:
    print("You got slapped by an angry bass and drown.  Game Over!")

else:
  print ("You fall into a hole. Game over!")
