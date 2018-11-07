class Stats:
	def __init__(self, name, strength, defence, agility, health):
		self.name = name
		self.strength = strength
		self.defence = defence
		self.agility = agility 
		self.health = health 
	def add_strength(self, num):
		self.strength = self.strength + num
	def add_agility(self, num):
		self.agility = self.agility + num
	def add_defence(self, num):
		self.defence = self.defence + num
	def add_health(self, num):
		self.health = self.health + num

	def lose_health(self, num):
		self.health = self.health - num

Hero = Stats(name, 10, 10, 10, 20)
