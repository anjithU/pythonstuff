
"""
functions that does the calc

"""


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


memory = {}
firstNumber = int(input("Enter the first number: \n\t"))

while True:
    """ 
    inputs 
    """

    print("+ \n- \n/ \n* ")
    calc = input("choose an operator: \n\t")
    secondNumber = int(input("Enter the second number: \n\t"))

    """

    output

    """

    if calc == "+":
        print("The result is: ", add(firstNumber, secondNumber))

        memory[calc] = add(firstNumber, secondNumber)


    if calc == "-":
        print("The result is: ", subtract(firstNumber, secondNumber))
        memory[calc] = subtract(firstNumber, secondNumber)

    if calc == "*":
        print("The result is: ", multiply(firstNumber, secondNumber))

        memory[calc] = multiply(firstNumber, secondNumber)

    if calc == "-":
        print("The result is: ", subtract(firstNumber, secondNumber))

        memory[calc] = subtract(firstNumber, secondNumber)

    print(memory)

    repeat_calc = input("Do you want to repeat yes for  y or n for no: \n\t")

    if repeat_calc == "n":
        memory = {}
    elif repeat_calc == "y":
        firstNumber = memory[calc]

        if len(memory) > 1:
            firstkey = next(iter(memory.keys()))
            del memory[firstkey]


    print(memory)