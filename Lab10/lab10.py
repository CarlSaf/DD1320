from linkedQFile import *
import unittest
import string
import sys
import re
from molgrafik import *
from tkinter import *


# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...

#Eventuell kolla tom input
def formel_check(q):
	mol_check(q)
	if q.peek() != '#':
		raise SyntaxError('Felaktig gruppstart')
	return rutan

def mol_check(q):
	if q.peek() is '(' or check(q.peek()):
		rutan=group_check(q)
		if q.isEmpty():
			rutan.next=mol_check(q)

	return

def group_check(q):
	rutan = Ruta()
	if q.peek() is '#':
		return

	if q.peek() is '(': #----------------------     <(mol)>
		q.dequeue()
		if q.peek() is ')':
			raise SyntaxError('Saknad högerparentes')
		rutan.down=mol_check(q)
		if q.peek() is not ')':
			raise SyntaxError('Saknad högerparentes')
		q.dequeue()
		if not is_num(q.peek()):
			raise SyntaxError('Saknad siffra')
		rutan.num=number_check(q)
		return #-------------------------------     <(mol)>

	rutan.atom=atom_check(q) #----------------------------     <atom>
	rutan.num=number_check(q) #--------------------------     <atom><number>
	return rutan

def atom_check(q):
	if is_num(q.peek()):
		raise SyntaxError('Felaktig gruppstart')
	if not Letter_check(q.peek()):
		raise SyntaxError('Saknad stor bokstav')
	atom=q.dequeue() #------------------------      <A>
	if letter_check(q.peek()):
		a=q.dequeue()
		atom+=a #-----------------------------      <Aa>
	if atom in atomlista:
		return atom
	else:
		raise SyntaxError('Okänd atom')

def number_check(q):
	if is_num(q.peek()):
		num = q.dequeue()
		num_collect=num
		if num is '0':
			raise SyntaxError('För litet tal')
		num=q.peek()
		if q.isEmpty() is False:
			while is_num(num) is True:
				num_collect += q.dequeue()
				if q.isEmpty() is True:
					break
				num=q.peek()
		if num_collect is '1':
			raise SyntaxError('För litet tal')
		return num_collect


def Letter_check(l):
	if l is not None:
		if l in string.ascii_uppercase:
			return True
	return False
def letter_check(l):
	if l is not None:
		if l in string.ascii_lowercase:
			return True
	return False
def is_num(n):
	# print(n, 'kommer in i is_num')
	if n is not None:
		if re.search('^[0-9]$', n):
			# print(n, 'passerade')
			return True
	# print(n, 'kuggades')
	return False
def check(char):
	if not (letter_check(char) or Letter_check(char) or is_num(char)):
		return False
	else:
		return True
def rest_of_list(q):
	remaining=""
	while q.isEmpty() is False:
		remaining += q.dequeue()
	return remaining.strip('#')
def que(lista):
	if len(lista) > 0:
		q=LinkedQ()
		for i in lista:
			q.enqueue(i)
		return q
	else:
		raise SyntaxError("Tom input")
def controll(test):
	a=formel_check(test)
	return a

###############################################################################


class Ruta:
	def __init__(self, atom="( )", num=1):
		self.atom = atom
		self.num = num
		self.next = None
		self.down = None

if __name__ == '__main__':
	atomlista = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y"," Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U"," Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"]
	molekyl = input("Molekyl: ")
	
	try:
		q=que(str(molekyl+'#'))
		if controll(q) is True:
			print("Formeln är syntaktiskt korrekt")
			
	except SyntaxError as fel:
		error_message=str(fel) + ' vid radslutet ' + rest_of_list(q)
		print(error_message)