# Dice Roll Simulator

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
    selection = input("Enter Selection (1-4): ") 

    # Action from Menu
    if selection == "1":
        print()
    elif selection == "5": 
        print("Goodbye")
    loop = False