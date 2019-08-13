# L2 Q5: play rock-paper-scissor - Beat the King
# You need to win the king three times in a row in order to throw him away from his throne
# Carefully think about where a loop should be place
# Suggested Logic:
#
# Repeat the following until you really win
#        Challenge the king three times, in each challenge
#               pick a choice for the King and a choice for the player
#               Repeat this if it is draw
#                      pick a choice for the King and a choice for the player
#               if fail the challenge, break from this loop
#        




# Import necessary modules
import random
from random import randint
count = 0
status = 0


print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')
while count < 3:
    print("Please input your choice")
    print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""") 


    p_choice = int(input())
    m_choice = randint(1,3)
    if p_choice <1 or p_choice > 3:
        status = 4
        print("Invalid input!")
    else:
        if m_choice == 1:
            print("Minion chooses rock!")
        elif m_choice == 2:
            print("Minion chooses paper!")
        elif m_choice == 3:
            print("Minion chooses scissor!")
                
        if p_choice == 1:
            print("You choose rock!")
        elif p_choice == 2:
            print("You choose paper!")
        elif p_choice == 3:
            print("You choose scissor!")
               
        if p_choice == 1 and m_choice == 3:
            status = 1
            count = count + 1
            print("You win!")
        elif m_choice == 1 and p_choice == 3:
            status = 2
            count = 0
            print("Minion wins!")
            print("Try again!")
        elif p_choice > m_choice:
            status = 1
            count = count + 1
            print("You win!")
        elif p_choice < m_choice:
            status = 2
            count = 0
            print("Minion wins!")
            print("Try again!")
        elif p_choice == m_choice:
            status = 3
            print("Draw!")
        
if count == 3:
    print("Congratulations!You win the king three times in a row!")

         
