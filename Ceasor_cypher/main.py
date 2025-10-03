
Play_again = True


while Play_again:
    # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.


    def encrypt(text,shift,alphabet):

    # message to list
        text_list =list(text)

        # getting the index of the list from alphabet

        indexes = [alphabet.index(ch) for ch in text_list]

        #shifted letters

        shifted_letters = [i+shift for i in indexes]

        # encrypted message and converting into human formatable form

        encrypted_message = [alphabet[i] for i in shifted_letters]

        print(f""" your secret code is {"".join(encrypted_message)}""")


    def decrypt(text,shift,alphabet):
        # message to list
        text_list =list(text)

        # getting the index of the list from alphabet

        indexes = [alphabet.index(ch) for ch in text_list]

        #shifted letters

        shifted_letters = [i- shift for i in indexes]

        # decrypted message and converting into human formatable form

        encrypted_message = [alphabet[i] for i in shifted_letters]

        print(f""" your message is {"".join(encrypted_message)}""")
    




    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'e' to encrypt, type 'decode' to d:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))



    if direction =="e":
        encrypt(text,shift,alphabet)
    elif direction =="d":
        decrypt(text,shift,alphabet)
    else:
        print("wrong selection")

    


    
    
    Play_again = input("do you wanna play again Y or N").lower()

    if Play_again =='n':
        Play_again = False









