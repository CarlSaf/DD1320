from bintreeFile import Bintree

from linkedQFile import LinkedQ

def makechildren(startord, q):
    strlista = []
    gamla.put(startord)
    for i in range(3):
        lista = list(startord)
        for j in range(25):
            lista[i] = chr(97+j)
            byttbokstav = "".join(lista)
            strlista.append(byttbokstav)

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
                    q.enqueue(ordet)
                gamla.put(ordet)

if __name__ == '__main__':

    # count = 0;

    startord = input("Vilket är ditt startord? ")
    
    slutord = input("Vilket är ditt slutord? ")

    q = LinkedQ()

    q.enqueue(startord)

    ordlista = Bintree()
    
    gamla = Bintree()

    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in ordlista:
                continue #print(ordet, end = " ") 
            else:
                ordlista.put(ordet)             # in i sökträdet

    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, q)
        # count += 1
        if nod == slutord:
            print("Det finns en väg till", slutord)
            # print("Antal gånger i while", count)
            break