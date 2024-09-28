
# TASK 10: 	ROCK-PAPER-SCISSORS GAME 

import random

user_score = 0
comp_score = 0

comp_random = random.randint(1, 3)

def game():       
    global user_score, comp_score
    while True:    
        if (user_choice == comp_random): 
                print("Tie!")
                user_score += 1
                comp_score += 1
        elif (user_choice == 1 and comp_random == 3) or \
                (user_choice == 2 and comp_random == 1) or \
                (user_choice == 3 and comp_random == 2):
                print("You won!")
                user_score += 1
        else:
                print("Computer won!")
                comp_score += 1
        
        print("\nYour score: ", user_score)
        print("\nComputer's score: ", comp_score)
        
        return "" 

while True:
        
   try:
       print("\n***** ROCK-PAPER-SCISSORS GAME *****")
       print("\n1. Rock")
       print("2. Paper")
       print("3. Scissors")
       print("4. Exit") 
       user_choice = int(input("\nPlease enter a number(1, 3): "))
                
       if user_choice in [1, 2, 3]:
           game()
       elif user_choice == 4:
           print("Quitting...")
           break
       else:
           print("\nInvalid number! Please enter 1, 2, or 3.")
   except ValueError:
       print("\nInvalid input! Please enter a valid number only.")
            

    


            














   
    
    
