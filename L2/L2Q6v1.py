#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)
print ("shhh, Dave hides %s bananas" % n)
# define a flag for found/not found and counter on how many trials
found = False
count = 0
#Step 4: Give three chances to the players
p = int(input("Guess a number between 1 and 100."))

while found == False:
    if p < 1 or p > 100:
        print("Your guess is out-of-range!")
        count = count + 1
    elif p > n:
        print("Your guess is too high!")
        count = count + 1
    elif p < n:
        print("Your guess is too low!")
        count = count + 1
    elif p == n:
        found = True
        count = count + 1
        
    if count == 3 and found == False:
        print("Game over.")
        break
    
    else:
        
#Step 5: Display a message
        if found == True:
            print('You got the correct guess in %d trials' % count)
            print('Dave\'s banana are now all yours!')
        else:
            print("You failed to find the number of bananas Dave hid! Try again next")
            p = int(input("Guess a number between 1 and 100."))
        

