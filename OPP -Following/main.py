class User:
	def __init__(self,id,user_name):
		print("new User is going to created")
		self.id = id
		self.user_name = user_name
		self.follwers = 0
		self.following = 0

	def follow(self,user):
		user.follwers+=1
		self.following+=1

user1 = User(1,"anjith")
user2 = User(2,"Ponnu")
print(user1.follwers)

user1.follow(user2)
print(user1.following)
print(user2.follwers)
