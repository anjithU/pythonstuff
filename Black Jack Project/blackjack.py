

from logo import art
import random


#-------------Random Cards--------------

def cards():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)



#------------------------Comparison Function--------------


def game_logic(dealers_hand,user_hand):

    if sum(dealers_hand) <17:
        dealers_hand.append(cards())


    print(f"\nYour dealer contain {dealers_hand} this card and the sum is {sum(dealers_hand)} ")


    if sum(dealers_hand) == sum(user_hand):
        print("Oh its a tie !")
        
    
    elif sum(dealers_hand) < sum(user_hand) <=21:
        print("You win")
        
    
    elif sum(dealers_hand)>21:
        print("You Win")
        
    
    else:
        print("You Loose")
       
    
# ---------------------Play Logic --------------- 

def play():

    dealers_hand = [cards() for i in range(2) ]
    user_hand  =  [cards() for i in range(2) ]

    #--------------Formating The Output------------------

    print()
    print()
    print()
    print(art)
    print()
    print("Welcome to Black Jack")

    print(f" Your cards {user_hand} Current Score  {sum(user_hand)} ")
    print(f"Dealers first card {dealers_hand[0]}")
    print()
    
    #---------------------- User input & Logic ----------------------------------
    while True:
        user_input=input("Type 'y' to get another card, type 'n' to pass :-  ").lower().strip()
        while user_input not in ['y','n']:
            print("Invalid Choice")
            user_input=input("Type 'y' to get another card, type 'n' to pass :- ").lower().strip()
        
        if user_input =='y':
            user_hand.append(cards())
            print(f"\nYour cards {user_hand} Current Score  {sum(user_hand)} ")


            
        else:
            game_logic(dealers_hand,user_hand)
            break
    
    
    

    

play()