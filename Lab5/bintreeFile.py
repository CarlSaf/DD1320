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