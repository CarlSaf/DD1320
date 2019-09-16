from bintreeFile import Bintree
from linkedQFile import LinkedQ

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, child): #metod som skriver ut vägen rekursivt
        if not child.parent is None:
            self.writechain(child.parent) #kallar på sig själv med argumentet parent
            print(child.word)

def makechildren(nod, q):
    strlista = []
    gamla.put(nod.word)
    for i in range(3):
        lista = list(nod.word)
        for j in range(25):
            lista[i] = chr(97+j)
            byttbokstav = "".join(lista)
            strlista.append(byttbokstav)

        #Specialfall å,ä,ö
        lista[i] = chr(229)
        byttbokstav = "".join(lista)
        strlista.append(byttbokstav)
        lista[i] = chr(228)
        byttbokstav = "".join(lista)
        strlista.append(byttbokstav)
        lista[i] = chr(246)
        byttbokstav = "".join(lista)
        strlista.append(byttbokstav)

        for ordet in strlista:
            if ordet in ordlista:
                if ordet not in gamla:
                    p=ParentNode(ordet)
                    p.parent=nod
                    q.enqueue(p)
                gamla.put(ordet)

if __name__ == '__main__':
    
    startord = input("Vilket är ditt startord? ")
    slutord = input("Vilket är ditt slutord? ")

    q = LinkedQ()
    q.enqueue(ParentNode(startord))

    ordlista = Bintree()
    gamla = Bintree()

    #Läser in textfilen
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in ordlista:
                continue #print(ordet, end = " ") 
            else:
                ordlista.put(ordet)             # in i sökträdet

    while not q.isEmpty(): #Körs så länge kön med startordets barn är full
        nod = q.dequeue()
        makechildren(nod, q)
        if nod.word == slutord:
            print("Det finns en väg från", startord, "till", slutord)
            print(startord) #Skriver startordet
            nod.writechain(nod) #Skriver vägen mellan noderna rekursivt
            break