class Node():
	def __init__(self, element, next=None):
		self.element = element
		self.next = next

class LinkedQ():

	def __init__(self):
		self.__forsta = None
		self.__sista = None

	def enqueue(self, element):
		enNode = Node(element)
		if self.__forsta == None:
			self.__forsta = enNode
			self.__sista = enNode
		else:
			self.__sista.next = enNode
			self.__sista = enNode

	def dequeue(self):
		forstaelement = self.__forsta.element
		self.__forsta = self.__forsta.next    # Pekare flyttas
		return forstaelement

	def isEmpty(self):
		# return self.__forsta == None
		if self.__forsta == None:
			return True
		else:
			return False

	def peek(self):
		if not self.isEmpty():
			return self.__forsta.element
		else:
			return None

