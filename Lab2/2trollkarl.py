from ArrayQ import ArrayQ

def start_kort(arrayQ): #Funktion som tar kort-input
	print("Ess är 1 och kung är 13")
	for i in range (13):
		arrayQ.enqueue(int(input("Ange vilket kort som väljs härnsäst: "))) #Kortet stoppas längst bak i listan

def test(): #Testfunktion för att kontrollera enqueue och dequeue
	q = ArrayQ()
	q.enqueue(1)
	q.enqueue(2)
	x = q.dequeue()
	y = q.dequeue()
	if (x == 1 and y == 2):
		print("Fungerar")
	else:
		print("Något är fel. 1 och 2 förväntades men vi fick", x, y)

if __name__ == '__main__':
	test()
	arrayQ = ArrayQ() #en array skapas
	start_kort(arrayQ) #anrpoar funktionen start_kort
	
	i = 0
	while not arrayQ.isEmpty():
		i+=1
		kortet = arrayQ.dequeue() #raden anropar kortet längst bak i listan
		if i%2 != 0: #När i är delbart med 2 (varranan gång) körs följande
			#print("nu placeras ett kort längst bak")
			arrayQ.enqueue(kortet) #Enqueue körs 
		else:
			print("kort", kortet, "placeras på bordet")