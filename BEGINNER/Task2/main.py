
    #TASK 2: UNIT CONVERTER

#......................
#.                    .
#.    Main Modul      . 
#.                    .
#......................

import screen

def main():    
        while True:
            try:
                print("\n******* WELCOME TO UNIT CONVERTOR *******")
                print("\nPlease make your choice below...")
                print("\n1. Temperature")
                print("2. Length")
                print("3. Weight")
                print("4. Quit")
                
                user_choice = int(input("\nYour choice: "))
            
                if (user_choice == 1):
                    screen.temperatureScreen()
                    
                elif (user_choice == 2):
                    screen.lengthScreen()
                    
                elif (user_choice == 3):
                    screen.weightScreen()
                    
                elif (user_choice == 4):
                    break
                else:
                    print("No such option. Please try again...")
            except ValueError:
                print("Please enter a number only.")
        return ""
 
main()
