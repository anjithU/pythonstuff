from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_MoneymakingMachine = MoneyMachine()
my_Coffemaker = CoffeeMaker()
my_Menu = Menu()

# report 





#Menu
is_on = True
while is_on :
	options = my_Menu.get_items()
	choice = input(f"What would you like {options} ?\n")
	
	if choice =='off':
		is_on =False
	elif choice =='report':
		my_MoneymakingMachine.report()
		my_Coffemaker.report()

	# my_MoneymakingMachine.make_payment()

	else:
		drink = my_Menu.find_drink(choice)
		print(my_Coffemaker.is_resource_sufficient(drink))
			

