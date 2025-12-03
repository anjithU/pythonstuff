#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open(r"C:\Users\Anjith Mathew\Documents\Programming\Python\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as f:
    data = f.read()

my_list = data.split("\n")



with open(r"C:\Users\Anjith Mathew\Documents\Programming\Python\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt","r") as letter_data:
    letter = letter_data.read()

print(letter)

for i in range(len(my_list)):
        new_letter = letter.replace("[name]",my_list[i])

        with open(f'{my_list[i]}.txt', 'w') as output:
            output.write(new_letter)


