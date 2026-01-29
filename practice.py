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

player = input("rock, paper or scissor\nrock")
print (player)

computer = [rock,paper,scissors]
abc = (random.choice(computer))
print(abc)

#if player = rock
if player == rock:
    if abc == scissors:
        print ("Its a win!! You Win")
    elif abc == paper:
        print ("You Lose")
    elif abc == rock:
        print ("Its a  draw")
    else:
        print ("Its a  draw")

if player == paper:
    if abc == rock:
        print ("Its a win!! You Win")
    elif abc == scissors:
        print ("You Lose")
    elif abc == paper:
        print ("Its a  draw")

if player == scissors:
    if abc == paper:
        print ("Its a win!! You Win")
    elif abc == rock:
        print ("You Lose")
    elif abc == scissors:
        print ("Its a  draw")