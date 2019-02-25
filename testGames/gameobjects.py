import math

class Vector2 (object):
	# constructor for Vector2 object
	def __init__ (self, x=0.0, y=0.0):
		self.x = x
		self.y = y
	
	# method returning cordinates in string format
	def __str__ (self):
		return "(%s, %s)"%(self.x, self.y)
	
	#  method calculating the distance from p1 to p2
	@staticmethod
	def from_points (P1, P2):
		return Vector2 (P2[0] - P1[0], P2[1] - P1[1])
	
	# calculating the magnitude of distance
	def get_magnitude (self):
		return math.sqrt (self.x**2, self.y**2)
	
	# calculating unit vector for direction
	def normalize (self):
		magnitude = self.get_magnitude ()
		self.x /= magnitude
		self.y /= magnitude
	
	# adding two vectors
	def __add__ (self, rhs):
		return Vector2 (self.x + rhs.x, self.y + rhs.y)
	
	# subtracting two vectors
	def __sub__ (self, rhs):
		return Vector2 (self.x - rhx.x, self.y - rhs.y)

	# negation of vector
	def __neg__ (self):
		return Vector2 (-self.x, -self.y)
	
	# multiplication of vector with some scalar value
	def __mul__ (self, scalar):
		return (self.x * scalar, self.y * scalar)
	
	# division of vector with some scalar value
	def __div__ (self, scalar):
		return (self.x / scalar, self.y / scalar)


# class for 3d vector
class Vector3 (object):
	def __init__ (self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def get_magnitude (self):
		return math.sqrt (self.x**2, self.y**2, self.z**2)
	
	# method returning cordinates in string format
	def __str__ (self):
		return "(%s, %s, %s)"%(self.x, self.y, self.z)
	
	#  method calculating the distance from p1 to p2
	@staticmethod
	def from_points (P1, P2):
		return Vector2 (P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2])
	
	# calculating unit vector for direction
	def normalize (self):
		magnitude = self.get_magnitude ()
		self.x /= magnitude
		self.y /= magnitude
		self.z /= magnitude
	
	# adding two vectors
	def __add__ (self, rhs):
		return Vector2 (self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)
	
	# subtracting two vectors
	def __sub__ (self, rhs):
		return Vector2 (self.x - rhx.x, self.y - rhs.y, self.z - rhs.z)

	# negation of vector
	def __neg__ (self):
		return Vector2 (-self.x, -self.y, -self.z)
	
	# multiplication of vector with some scalar value
	def __mul__ (self, scalar):
		return (self.x * scalar, self.y * scalar, self.z * scalar)
	
	# division of vector with some scalar value
	def __div__ (self, scalar):
		return (self.x / scalar, self.y / scalar, self.z / scalar)


	# parallel perspective
	def parallel_project (vector3):
		return (vector3.x, vector3.y)

	# Perspective projection
	def perspective_project (vector3, d):
		x, y, z = vector3
		return(x * d/z, -y * d/z)
