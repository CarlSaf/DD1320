class Node(): #En klass nod skapas
	def __init__(self,value): #Varje nod har två egenskaper
		self.value=value #Egenskap 1: ett värde
		self.next=None #Egenskap 2: en pekare

class LinkedQ(): #En 'pekar-kö'(?) skapas
	def __init__(self):
		self.__first=None #Kön har ett första värde (Privat)
		self.__last=None #Kön har ett sistavärde (Privat)
	
	def enqueue(self, kort): #Metoden enqueue, insertar 'kortet' länst fram i listan
		if self.__first==None: #Om det är första kortet som 'enqueue:as' körs denna
			self.__first=Node(kort) #Listpekaren First pekas mot noden
			self.__last=self.__first #Listpekaren Last pekas mot noden också, enbart en sak i listan => första=sista
		
		else: #Om det inte är det första kortet körs denna
			n = Node(kort) #En ny nod skapas med 'value' satt till kortets
			n.next = self.__first #Nodens nextpekare pekas om till den nuvarande 'first'
			self.__first=n #Firstpekaren uppdateras till den nya noden

	def dequeue(self): #Metod, returnerar sista kortet i listan, innehåller tre fall
		if self.__first==self.__last: #Fall 1: om första kortet också är det sista (Ett kort i leken)
			val=self.__first.value #Värdet sparas ner i 'val'
			self.__first=None #Pekarna first och last pekas om till 'None'
			self.__last=None
			return val #Det nersparade värdet val returneras
		
		if self.__first.next==self.__last: #Fall två, om pekaren next pekar mot det sista kortet (två kort i leken)
			val=self.__last.value #Det sista (längst bak) värdet sparas ner i 'val'  
			self.__last=self.__first #Last pekas om till det första värdet (det andra kortet)
			return val #Värdet val returneras
		
		a=self.getLast(self.__first) #Fall 3: om det är tre eller fler kort i leken, kallar på en rekursiv funktion getLast
		return a.value #Returnerar det värde som hämtas i funktionen

	def isEmpty(self): #Metod som kontrollerar om listan är tom eller inte
		if self.__last==None: #ifsats som kollar om det 'last' pekar mot None
			return True
		else:
			return False

	def getLast(self, node): #rekursiv funktion som går igenom alla next-pekare från 'first' till tredje 'last'
		#print("Nu körs getLast")
		#print("vi står nu på",node.next.value)
		if node.next.next.next==None: #Om tredje pekaren från aktuell nod är None (slut på listan)
			self.__last=node.next #pekar om 'last'pekaren till nästa nod, näst sista elementet
			val=node.next.next #Sparar noden från den sista listplatsen till ett värde 'val'
			node.next.next=None #pekar om samma nod till None
			#print("nu är self.Last", self.__last.value)
			return val #Returnerar noden
		else:
			return self.getLast(node.next) #Om inte tidigare if-sats uppfylls påkallas funktionen igen