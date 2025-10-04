repeat = True
auction = {}

while repeat:



    name = input("What is your name?\n \t")
    bid = input("What is your bid?\n\t")
    repeat_loop = input("Are there any other bidders? Type 'y or 'n'. \n\t").lower()
    # TODO-2: Save data into dictionary {name: price}

    auction[name] = bid

    if repeat_loop == "n":
        print(f"the biggest value is {auction[name]}")
        break
    else:
        if name in auction:
            big = auction[name]

            if bid > auction[name]:
                big =  auction[name]


                print(f"the biggest value is {auction[name]}")





