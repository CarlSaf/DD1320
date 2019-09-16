from linkedQFile import *
import unittest
import string

"""<molekyl> ::= <atom> | <atom><num>
	  <atom>  ::= <LETTER> | <LETTER><letter>
	  <LETTER>::= A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
	  <letter>::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
	  <num>   ::= 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""

class check_syntax(unittest.TestCase):
	def test_correct(self):
		self.assertEqual(controll("H"),True)
		self.assertEqual(controll("H2"),True)
		self.assertEqual(controll("H2222"),True)
		self.assertEqual(controll("Ha"),True)
		self.assertEqual(controll("Ha2"),True)
		self.assertEqual(controll("Ha2222"),True)
	def test_fail (self):
		with self.assertRaises(SyntaxError):
			controll("HH")
		with self.assertRaises(SyntaxError):
			controll("h")
		with self.assertRaises(SyntaxError):
			controll("2")
		with self.assertRaises(SyntaxError):
			controll("Haa")
		with self.assertRaises(SyntaxError):
			controll("Ha1")
		with self.assertRaises(SyntaxError):
			controll("Ha0")
		with self.assertRaises(SyntaxError):
			controll("Ha1a")
		with self.assertRaises(SyntaxError):
			controll("Ha.2")
		with self.assertRaises(SyntaxError):
			controll("H2O")
		with self.assertRaises(SyntaxError):
			controll("Hi12h")
		with self.assertRaises(SyntaxError):
			controll("Hi1h")
		with self.assertRaises(SyntaxError):
			controll(".Hi")
		with self.assertRaises(SyntaxError):
			controll("iH")
		with self.assertRaises(SyntaxError):
			controll("å")
		with self.assertRaises(SyntaxError):
			controll("Å")
		with self.assertRaises(SyntaxError):
			controll("")

def mol_check(q):
	atom_check(q)
	if q.isEmpty() != True:
		number_check(q)

def atom_check(q):
	Letter_check(q)
	if not q.peek() == None:
		if q.peek() in string.ascii_lowercase:
			letter_check(q)

def Letter_check(q):
	l=q.dequeue()
	if l in string.ascii_uppercase:
		# print(l, "passerade som stor bokstav")
		pass
	else:
		raise SyntaxError ("Ej stor bokstav")

def letter_check(q):
	l=q.dequeue()
	if l in string.ascii_lowercase:
		# print(l, "passerade som liten bokstav")
		pass
	else:
		raise SyntaxError ("Ej liten bokstav")

def number_check(q):
	n=q.dequeue()
	# print(n, "testas som siffra")
	try:
		a=int(n)
		if a in number_list:
			# print (a, "passerade som siffra")
			if q.isEmpty() is not True:
				number_check(q)
			else:
				pass
		else:
			raise SyntaxError ("Fel siffra")
	except ValueError:
		raise SyntaxError ("Förväntar en siffra eller liten bokstav")

def que(lista):
	if len(lista) > 0:
		q=LinkedQ()
		for i in lista:
			# print(i,"Queas")
			q.enqueue(i)
		return q
	else:
		raise SyntaxError("Tom input")


def controll(test):
	mol_check(que(test))
	return True

if __name__ == '__main__':
	number_list=[2,3,4,5,6,7,8,9]
	if controll(input("Testa ett syntax: ")) is True:
		print("Korrekt syntax")
	unittest.main()