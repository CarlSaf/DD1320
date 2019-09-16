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

def skriv(p):
    if p != None:
        skriv(p.left)
        print(p.word)
        skriv(p.right)


if __name__ == '__main__':
    print("\n")
    svenska = Bintree()
    gamla=Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ")
                gamla.put(ordet)
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")
    if input("Vill du skiva ut den svenska ordlistan? (y):") == "y": 
        svenska.write()


    gamla=Bintree()


    engelska=Bintree()
    with open("engelska.txt", "r", encoding = "utf-8") as engfil:
        for rad in engfil:
            ordet=rad.strip(",")
            for ordet in rad.split():
                if not(ordet in engelska):
                    engelska.put(ordet)
                    if ordet in svenska:
                            print(ordet, end = " ")
    if input("Vill du skiva ut den engelska ordlistan? (y):") == "y": 
        engelska.write()