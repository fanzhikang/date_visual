from random import randint 
class Die(object):
	"""docstring for Die"""
	def __init__(self, num_sides=6):
		
		self.num_sides = num_sides


	def roll(self):
		return randint(1,self.num_sides)

