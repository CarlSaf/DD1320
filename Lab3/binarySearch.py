from random import randint

class Node():
	def __init__(self, value):
		self.left=None
		self.right=None
		self.value=value

class BinSearch():
	def __init__(self):
		self.root=None
	
	def adQue(self,value):
		print(value)
		if self.root==None:
			self.root=Node(value)
			print("Root has been set")
		else:
			self.findNext(value)
			
	def findNext(self,value):
		node=self.root
		while True:
			if value == node.value:
				print("detta tal finns redan")
				break
			if value > node.value:
				#print("right")
				if node.right == None:
					node.right=Node(value)
					#print("node.right var tom och har ansatts till value")
					break
				else:
					node=node.right
			if value < node.value:
				#print("left")
				if node.left == None:
					node.left=Node(value)
					#print("node.left var tom och har ansatts till value")
					break
				else:
					node=node.left

def inorder(p):
    if p != None:
        inorder(p.left)
        print(p.value)
        inorder(p.right)

def finns(p,value):
	if p == None: 
		return False
	if value == p.value:
		return True
	if value < p.value:
		return finns(p.left,value)
	if value > p.value:
		return finns(p.right,value)


def antal(p): #Hur många noder finns i binärträdet?
    if p == None:
        return 0
    else:
        return 1 + antal(p.left) + antal(p.right)

if __name__ == '__main__':
	tree=BinSearch()
	#input()
	for i in range (100):
		tree.adQue(randint(1,100))
	print("\nAntal nodes i det binära trädet: ")
	print(antal(tree.root))
	print(finns(tree.root,50))
	inorder(tree.root)