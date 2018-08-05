# Write your solutions for 1.5 here!
class superheros():
 	"""docstring for superheros"""
 	def __init__(self, name,superpower,strength):
 		self.name = name
 		self.superpower = superpower
 		self.strength = strength
 	def print_na_str(self):
 		print("his name is " + self.name + " and his trength level is "+self.strength)
 	def save_civil(self, work):
 		if(work > self.strength):
 			print(self.name + " is not strong enough")
 		else:
 			self.strength = self.strength - work
 			