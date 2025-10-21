import art



#--------------------------User input----------------------------------------------------

def user_input():

	user_input = input("What would you like? (espresso/latte/cappuccino):").lower().strip()


	while user_input not in ['espresso','latte','cappuccino','off' ,'report']:
		print("You entered the wrong input")
		user_input = input("What would you like? (espresso/latte/cappuccino):").lower().strip()
		if user_input =='off':
			exit



	if user_input == 'report':
		coffe_resources =current_resourses(None)
		print(coffe_resources)




	if user_input =='espresso':
		espresso =  { 'needed_to_make': {
    	"water": 50,      # in ml
    	"coffee": 18,      # in g
		} ,"price" :1}

		return espresso




	elif user_input == 'latte':
		latte ={ 'needed_to_make' :{
    	"water": 200,      # in ml
    	"milk": 150,        # in ml
    	"coffee": 24,      # in g
		},"price" :2 }

		return latte




	elif user_input =='cappuccino':
		cappuccino ={ 'needed_to_make' :{
    	"water": 250,      # in ml
    	"milk": 100,        # in ml
    	"coffee": 24,      # in g
    	"money": 2.5       # in USD
		},"price" :3}

		return cappuccino




#------------------Current Resources --------------------------------------------------------

def current_resourses(deduction):

	value = deduction if deduction is not None else 0 

	print(deduction)
	coffee_data = {
	"water":300,
   "milk": 200,        # in ml
    "coffee": 100,      # in g
    "money": 0      # in USD
	}


	return coffee_data



#-------------------Money -----------------------------------------------------------------

def coin():
	print("Please insert coins")

	#----------------Coin checker ----------------


	def get_init(prompt):


		while True:

			try:
				value = int(input(prompt))
				if 1 <= value <=100:
					return value
				else:
					print("Please Enter a Valid Number between 1 and 100")

			except ValueError:
				print("Please Enter a Valid Number")



	def main():

		quarters = get_init("How many quarters : ")
		dimes = get_init("How many quarters : ")
		nickels = get_init("How many quarters : ")
		pennies = get_init("How many quarters : ")

		total_money  =  ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies)/100

		print(f" Your total is $ {total_money}")


		return total_money

	total_money = main()

	return total_money




			
#-------------Game Logic ----------------


def game():
	print(art.logo)
	coffee =user_input()

	if coffee is None:
		return

	print(coffee['price'])

	price = coin()

	print(price)

	if price == coffee['price']:
		print ('Making your coffe')
		coffe_resources(coffee)
	elif price > coffee['price']:
		print ('Making your coffe')
		print(f"Your change is {price - coffee['price']}")
		coffe_resources(coffee)
	else:
		print("not enough money")







game()










