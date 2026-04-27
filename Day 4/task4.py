
#! in task 4 we make a rock paper scissors game where user gives a number which value is equivalent to either rock, paper or scissors and computer generates its answer and either win, lose or draw



import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
human = [rock,paper,scissors]
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

if human_choice == 0:
    print(f"Your Choice\n {rock}")
elif human_choice == 1:
    print(f"Your Choice\n {paper}")
elif human_choice == 2:
    print(f"Your Choice\n {scissors}")

game = [rock, paper, scissors]
computer_choice = random.randint(0,2)

print(f"Computer Choice: \n {game[computer_choice]}")

if human_choice >= 3 or human_choice < 0:
    print("You typed an invalid number. You lose!")
elif human_choice == 0 and computer_choice == 2:
    print("You win")
elif human_choice == 1 and computer_choice == 0:
    print("You Win")
elif human_choice == 2 and computer_choice == 1:
    print("You Win")
elif computer_choice == human_choice:
    print("Its a draw")
else:
    print("You lose")

