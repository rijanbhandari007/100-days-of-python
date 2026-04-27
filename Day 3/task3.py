
#! in today's task, I had to use multiple if statements and nested if statements to make a treasure hunt program where right answer would lead to the treasure and wrong answer would lead to game being over. and i had to use lower() function to convert data to lower case to match the if statement

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

left_right = input ("You're in a crossroad, press 'Right' to go right or press 'left' to go left: ").lower()
if left_right == "right":
    print("you fell into a hole\n Game Over ")
elif left_right == "left":
    swim_wait = input("You've come upto a lake. Do you want to 'swim' or 'wait': ").lower()
    if swim_wait == "swim":
        print( "you were attacked by the crocodiles\n Game Over")
    elif swim_wait == "wait":
        which_door = input("The lake dried up and 3 doors arrears in front of you. 'Red', 'blue', 'yellow': ").lower()
        if which_door == "red":
            print ("You were burnt by fire!!\n Game Over")
        elif which_door == "blue":
            print("You were attacked by a beast!\n Game Over")
        elif which_door =="yellow":
            print("You won!\n Now you possess unlimited wealth")
        else:
            print("Game Over")
    else:
        print("Wrong Choice\n Game Over")
else:
    print("Wrong Choice\n Game Over")


