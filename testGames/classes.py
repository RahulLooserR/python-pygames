class Student:
	
	def __init__ (self, name, roll):
		self.name = name
		self.roll = roll

	def disp (self):
		print ('display method')

	def __del__(self):
		print (self.__class__.__name__, 'class destroyed')


