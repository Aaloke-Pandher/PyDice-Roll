# Dice Roll Simulator 

# Import Random 
import random

# Main Program Loop 
loop = True 
while loop: 
    # Print Menu
    print("\nDice Roll Simulator Menu")  
    print("1. Roll Dice Once") 
    print("2. Roll Dice 5 Times") 
    print("3. Roll Dice 'n' Times")  
    print("4. Roll Dice until Snake Eyes")  
    print("5. Exit") 

    # Get Menu Selection from User
    selection = input("Enter Selection (1-5): ") 

    # Action from Menu 
    dice1 = random.randrange(1,7) 
    dice2 = random.randrange(1,7)
    if selection == "1":
        print(dice1, dice2, "sum:", int(dice1) + int(dice2)) 
    elif selection == "2": 
        n = 0 
        for n in range(5): 
            print(dice1, dice2, "sum:", int(dice1) + int(dice2)) 
    elif selection == "5": 
        print("Goodbye")
        loop = False