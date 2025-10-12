
import random


art = r"""
                                                                                                 
                                                                                                    
        $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\        $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
        $$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      $$  __$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
        $$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\        $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
        $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\       $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
        \$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |      \$$$$$$$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
        \____$$ | \______/  \_______|\_______/ \_______/        \____$$ | \_______|\__| \__| \__| \_______|
        $$\   $$ |                                              $$\   $$ |                                  
        \$$$$$$  |                                              \$$$$$$  |                                  
        \______/                                                \______/                                   

 
"""

print(art)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")



# levels 

EASY_LEVEL =10
HARD_lEVEL = 5



def level_chooser():


    """
    a function for choosing levels
    
    """

    level_chooser = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

    #level chooser with list

    while  level_chooser  not in ["easy", "hard"]:
        print("Invalid choice. Please type 'easy' or 'hard'.")
        level_chooser = input("Choose a difficulty: ").lower()

        """
        writing a loop to return global variable

        """
        return EASY_LEVEL if level_chooser == "easy " else HARD_lEVEL



def target_number():

    "Generate a random number between 1 and 100 "

    return random.randint(1,100)



def guess():

    """
    input taker
    
    """

    while True:
        try:
            user_input = int(input("whats your guess :- "))
            return user_input
        except ValueError:
            print("Please enter a valid number between 1 and 100")



def comapre(user_input_logic,target_logic):
    if user_input_logic<  target_logic:
        print("Too Low ")
        return False
    elif user_input_logic> target_logic:
        print("Too High")
        return False
    else:
        print("You guessed it right")
        return True
    

def game_logic(target_for_logic,attempts):
    for attempt  in range(attempts,0,-1):
        print(f"you have {attempt} attempts remaining")
        user_input_logic = guess()
    
    if comapre(user_input_logic,target_logic):
        return
    else:
        if attempt -1>0:
            print("Guess again")
        else:
            print(f"❌ You've run out of guesses. The number was {target_for_logic}.")
    

    

def play():
    target = target_number()
    attempts = level_chooser()
    game_logic(target,attempts)




play()