import art

# -------------------- MENU --------------------
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# -------------------- RESOURCES --------------------
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


# -------------------- USER INPUT --------------------
def customer_want():
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    while customer_input not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Please enter a valid input\n")
        customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    return customer_input


# -------------------- COINS --------------------
def coins():
    print("Please insert coins")

    def get_int(prompt):
        while True:
            try:
                value = input(prompt)
                if value == "":
                    return 0  # Press Enter to skip
                value = int(value)
                if 0 <= value <= 50:
                    return value
                else:
                    print("Please enter a valid coin between 0 and 50")
            except ValueError:
                print("Please Enter valid number")

    quarters = get_int("How many quarters (25¢): ")
    dimes = get_int("How many dimes (10¢): ")
    nickels = get_int("How many nickels (5¢): ")
    pennies = get_int("How many pennies (1¢): ")

    total_money = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies) / 100
    print(f"💰 Your total is ${total_money:.2f}\n")
    return total_money


# -------------------- REPORT --------------------
def current_resources():
    print("\nCurrent Machine Resources:")
    for item, value in resources.items():
        print(f"{item}: {value}")
    print()


# -------------------- MAKE COFFEE --------------------
def make_coffee(coffee_name):
    """Check resources, deduct ingredients, and add money."""
    global resources

    recipe = MENU[coffee_name]

    # Check if enough resources
    for item, amount_needed in recipe["ingredients"].items():
        if resources.get(item, 0) < amount_needed:
            print(f"❌ Not enough {item} to make your {coffee_name}!")
            return False

    # Deduct ingredients
    for item, amount_needed in recipe["ingredients"].items():
        resources[item] -= amount_needed

    # Add money
    resources["money"] += recipe["cost"]
    return True


# -------------------- GAME LOGIC --------------------
def game_logic():
    print(art.logo)
    while True:
        choice = customer_want()

        if choice == "off":
            print("☕ Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            current_resources()
            continue

        recipe = MENU.get(choice)

        print(f"The {choice} costs ${recipe['cost']}")
        payment = coins()

        if payment < recipe["cost"]:
            print("❌ Not enough money. Money refunded.")
            continue
        elif payment > recipe["cost"]:
            change = round(payment - recipe["cost"], 2)
            print(f"Here is your change: ${change}")

        if make_coffee(choice):
            print(f"☕ Making your {choice}...\nEnjoy your drink!\n")


# -------------------- RUN PROGRAM --------------------
game_logic()
