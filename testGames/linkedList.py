# Program to implement linked list.

class Node:
	def __init__ (self, data = None):
		self.data = data
		self.nextLink = None
	

class LinkedList:
	def __init__(self):
		self.head = None
	
	def insert (self, data):
		NewNode = Node (data)

	#	if (self.head == None):
	#		self.head = NewNode

	#	else:
		NewNode.nextLink = self.head	
		self.head = NewNode

	def printList (self):
		temp = self.head
		while temp is not None:
			print (temp.data)
			temp = temp.nextLink

# Main starts from here

if __name__ == "__main__":
	List = LinkedList ()

	List.insert (100)
	List.insert (200)
	List.insert (300)
	List.printList()


			

