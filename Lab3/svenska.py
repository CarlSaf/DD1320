from bintreeFile import Bintree

print("\n")
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")
if input("Vill du skiva ut den svenska ordlistan? (y):") == "y": 
    svenska.write()

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