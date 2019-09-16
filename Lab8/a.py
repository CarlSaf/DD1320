# Syntaxkontroll

from wordqueue import WordQueue

class Grammatikfel(Exception):
    pass

def readMening(q):
    readSats(q)                                     
    if q.peek() == ".": 
        q.dequeue()
    else:                              
        readKonj(q)                                   
        readMening(q)                                 

def readSats(q):
    readSubj(q)                                  
    readPred(q)                                 

def readSubj(q):
    word = q.dequeue()                    
    if word == "JAG":
        return                  
    if word == "DU":  
        return                  
    raise Grammatikfel("Fel subjekt: " + word)       

def readPred(q):
    word = q.dequeue()                    
    if word == "TROR": 
        return                 
    if word == "VET":  
        return                 
    raise Grammatikfel("Fel predikat: " + word)      

def readKonj(q):
    word = q.dequeue()                    
    if word == "ATT": 
        return                  
    if word == "OCH": 
        return                  
    raise Grammatikfel("Fel konjunktion: " + word)          

def printQueue(q):
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end = " ")
    print()

def storeSentence(mening):
    q = WordQueue()
    mening = mening.split()
    for ordet in mening:
        q.enqueue(ordet)
    q.enqueue(".")
    return q


def kollaGrammatiken(mening):
    q = storeSentence(mening)

    try:                                  
        readMening(q)                                 
        return "Följer syntaxen!"     
    except Grammatikfel as fel:                            
        return str(fel) + " före " + str(q)

def main():
    q = "hej"
    mening = input("Skriv en mening: ")
    resultat = kollaGrammatiken(mening)
    print(resultat)

if __name__ == "__main__":
    main()