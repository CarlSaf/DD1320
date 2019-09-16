class Bok:
	def __init__(self, datarad):
		datarad = datarad.strip()
		datarad = datarad.split("...")
		self.titel = datarad[0]
	def __str__(self):
		return self.titel

with open("Pokedata.csv", encoding = "utf8") as Pokedata:
	titelrad = Pokedata.readline()
	print(titelrad)
	datarad = Pokedata.readline()
	b = Bok(datarad)
	#print(b)