import classes

class Employee:
	empCount = 0

	def __init__ (self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	
	def display (self):
		print ('total number of employee = ',  Employee.empCount)

	def dispEmpl (self):
		print ('name = ', self.name, 'salary = ', self.salary)

	def __del__(self):
		print (self.__class__.__name__, 'destroyed')

emp1 = Employee ("dksjfa", 1000)
emp2 = Employee ("hsdfjk", 2000)
emp1.display ()
emp1.dispEmpl ()
emp2.dispEmpl ()
student1 = classes.Student ("sumit", 20)
student1.disp()

