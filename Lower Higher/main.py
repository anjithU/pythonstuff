import random
from data import game_data
import art

#--------------- function to randomly select the given data choices ---------------------------------------


def  random_selector(data):

    return random.choice(data)






#---------------------Player 1------------------------------------------------------------------------------

def player_1():
    data_for_prcessing = random_selector(game_data)

    print(f"Compare A :{data_for_prcessing['name']  }   {data_for_prcessing['description']}   {data_for_prcessing['country']}")
    return data_for_prcessing['follower_count']






# ---------------------Player 2----------------------------------------------------
def player_2():
    data_for_prcessing = random_selector(game_data)

    print(f"Compare B :{data_for_prcessing['name']  }   {data_for_prcessing['description']}   {data_for_prcessing['country']}")
    return data_for_prcessing['follower_count']




#----------------------Game Logic -----------------------------------------------------

def game_logic():
    print(art.logo)

    while True:
        # score variable
        score = 0


        a = player_1()
        print()
        b = player_2()

        if a == b:
            a = player_1()
        print()
        print()
        user_input = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        print()
        print()

        while not  ['a','b']:
            print("Wrong input ")
            print()
            print()
            user_input = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
            print()
            print()


        



        if a > b:
            bigger ='a'
        else:
            bigger = 'b'


        if user_input == bigger:
            score +=1
        print(f"Your score is {score}")
        print()
        print()

        if user_input == bigger:
            print()
            print()
            print()
            print()
            print(art.logo)
            print(f"Your score is {score}")
            continue
        else:
            break
    
    
       


game_logic()