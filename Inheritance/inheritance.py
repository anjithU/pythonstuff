class Animal:

	def __init__(self):
		self.num_of_eyes = 2


	def breath(self):

		print('Inhale Exhale')


class Fish(Animal):
	def __init__(self):
		super().__init__()

	def breath(self):
		super().breath()
		print('Under Watttttter!')

	def swim(self):
		print("Where is water! . I want to swim")



nemo = Fish()
nemo.swim()
nemo.breath()

#____________Another_Example_________________

class Dog:

	def __init__(self):
		self.temperament = "loyal"

	def bark(self):
		print("Woof! ,Woof!")


class Labrador(Dog):
	def __init__(self):
		super().__init__()
	def bark(self):
		super().bark()


sparky = Labrador()
sparky.bark()