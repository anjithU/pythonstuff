import random 

word_list = ["aardvark", "baboon", "camel"]

# computer choosen work

choosen_word = random.choice(word_list)

print(choosen_word)



# choosen word to list


list_of_choosen_word = list(choosen_word)



# remove duplicate  and settig it as tries

tries =len(list(dict.fromkeys(list_of_choosen_word)))



 # place holder

place_holder = []


for i in range(len(choosen_word)):
    place_holder+= "_"


x_no_tries=tries

while x_no_tries:

    # user input

    guess = input("Guess a letter :\n").lower()

    print(f" Your Guess is {guess}\n")

    # COUNTER FOR APPLY
    x_no_tries-=1

    if guess in choosen_word:

        # Get only indices of a specific item

        indices = [i for i, x in enumerate(list_of_choosen_word) if x == guess]
        for i in indices:
            place_holder[i] = guess
        
        print(f"{place_holder} \n")

        # x will be reseted to orginal value

        x_no_tries=tries


        if place_holder ==list_of_choosen_word:
            
            print("You win")
            print()
            break

        

    else:
        print()
        print(f" you have {x_no_tries} tries left  ")
        print()
        print("your Guess dosent work")

        if x_no_tries == 0:
            print("You loose")




    


    


    


    



   

