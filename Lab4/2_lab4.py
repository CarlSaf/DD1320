from linkedQFile import LinkedQ

class CreateNode():
    def __init__(self, value):
        self.left=None
        self.right=None
        self.word=value

class Bintree():
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        self.root = putta(self.root,newvalue)
       
    def __contains__(self,value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")

def putta(root,newvalue):
    if root is None: #Basfall
        #print("Root är skapt")
        return CreateNode(newvalue)
    node=root
    if (newvalue < node.word) == True:
        if node.left is None:
            #print("Left node has been created")
            node.left = CreateNode(newvalue)
            return root
        putta(node.left,newvalue)
    elif (newvalue > node.word) == True:
        if node.right is None:
            #print("Right node has been created")
            node.right = CreateNode(newvalue)
            return root
        putta(node.right,newvalue)
    return root

def finns(p,value):     
    if p == None: 
        return False
    if value == p.word:
        return True
    if value < p.word:
        return finns(p.left,value)
    if value > p.word:
        return finns(p.right,value)

def makechildren(startord,q):
    gamla.put(startord)
    for a in range(3):
        s = list(startord)
        for i in range(26):
            s[a]=chr(97+i)
            ordet="".join(s)
            if ordet in svenska and not(ordet in gamla):
                gamla.put(ordet)
                q.enqueue(ordet)
                print(ordet)

if __name__ == '__main__':
    svenska = Bintree()
    gamla = Bintree()
    q=LinkedQ()
    q.enqueue(input("Startord??"))
    slutord=input("Slutord??")

    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                pass
                #makechildren(ordet,q)
            else:
                svenska.put(ordet)
        print("\n")
    print("ute" in svenska)
    print("hit" in svenska)

    while not q.isEmpty():
        nod = q.dequeue()
        makechildren(nod, q)
        if nod == slutord:
            print("found it")
            break