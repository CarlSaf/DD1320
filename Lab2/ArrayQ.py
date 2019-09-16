from array import array

class ArrayQ():
	def __init__(self):
		self.__kort_array=array('i') #Skapar en array som tar datatypen signed int
	
	def enqueue(self, kort): #Metoden enqueue, insertar 'kortet' länst fram i listan
		self.__kort_array.insert(0,kort) #insertar kortet på plats 0 i listan
		#print("enqueue", self.kort_array)

	def dequeue(self): #Metod, returnerar sista kortet i listan
		return(self.__kort_array.pop()) #Använder funktinen pop för att returnera det sista kortet i listan och sen ta bort den
		#print("kortet", x, "dequeue", self.kort_array)

	def isEmpty(self): #Metod som kontrollerar om lisan är tom eller inte
		if len(self.__kort_array)==0: #Om längden av listan är noll returneras sant
			return True
		else:
			return False