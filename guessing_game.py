
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









# ---------------- LEVEL CHOOSER ----------------


def level_chooser():


    """
    a function for choosing levels
    
    """

    choice  = input("Choose a difficulty. Type 'easy' or 'hard':").lower().strip()

    #level chooser with list

    while  choice  not in ["easy", "hard"]:
        print("Invalid choice. Please type 'easy' or 'hard'.")
        choice = input("Choose a difficulty: ").lower().strip()

    return 10 if choice == "easy" else 5








# ---------------- RANDOM NUMBER ----------------



def target_number():

    "Generate a random number between 1 and 100 "

    return random.randint(1,100)











# ------------------------PLAYER GUESS -----------------
def guess():

    """
    input taker
    
    """

    while True:
        try:
            user_input = int(input("whats your guess :- "))

            if 1 <= user_input <=100:
                return user_input
            else:
                print("Please enter a value between 1 and 100")
        except ValueError:
            print("Please enter a valid number between 1 and 100")








# ---------------- COMPARISON LOGIC ----------------

def comapre(user_guess ,target):
    
    if user_guess<  target:
        print(" Try something Low ")
        return False
    elif user_guess> target:
        print(" Try something  High")
        return False
    else:
        print("You guessed it right ,Congrats! You win ")
        return True
    






# ------------------  Game Loop  -----------


def game_logic(target,attempts):

    while attempts >0:
        print(f"\n  You have  {attempts} attempts remaining")

        user_guess = guess()

        is_correct = comapre(user_guess,target)
        
        if is_correct:
            break
        attempts -=1
        if attempts ==0:
            print(f"\n You have run out of guesses.The number was the {target} target .Better luck next time! ")

#---------------Main Function-------------

def play():
    attempts = level_chooser()
    target = target_number()
    game_logic(target,attempts)

    

#------------------Run Game ----------------------

play()