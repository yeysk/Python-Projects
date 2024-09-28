
# TASK 10: 	ROCK-PAPER-SCISSORS GAME 

# çökmüyor. ama işlem bitince kapanıyor.

import random

"""def main():
    print("***** \nROCK-PAPER-SCISSORS GAME *****")
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")"""
    
def game():
    while True:
        user_score = 0
        comp_score = 0
        
        comp_random = random.randint(1, 3)
        
        while True:
            try:
                print("\n***** ROCK-PAPER-SCISSORS GAME *****")
                print("\n1. Rock")
                print("2. Paper")
                print("3. Scissors")
                user_choice = int(input("\nPlease enter a number(1, 3): "))
                
                if user_choice in [1, 2, 3]:  
                    break                     
                else:
                    print("\nInvalid input! Please enter 1, 2, or 3.")
            
            except ValueError:
                print("\nInvalid input! Please enter a valid number.")
           
        if (user_choice == comp_random): 
            print("Tie!")
            user_score = 0
            comp_score = 0
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
        """while True: 
            try:
                another = input("\nDo you want to play again?(Y/N): ").lower()
                    
                if another == 'y':
                    break    
                elif another == 'n':
                    break
                else:
                    print("Invalid input! Please enter y or n.")
            except ValueError:
                    print("Invalid input! Please do not enter a number.")"""
        return "" 
                
        
#main()
game()
            

    


            














   
    
    
