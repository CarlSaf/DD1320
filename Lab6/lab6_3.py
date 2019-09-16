import timeit
from itertools import islice

class song:
    def __init__(self, data):
        self.artistID=data[0]
        self.artist=data[1]
        self.songTitle=data[2]
        self.songLen=data[3]
        self.year=data[4]
        
    def __lt__(self, other):
        if float(self.songLen) < float(other.songLen):
            return True
        else:
            return False

    def __str__(self):
        return "\n\nSong lenght: " + str(self.songLen) + "\nSong Title: " + str(self.songTitle) + "\nArtist: " + str(self.artist)

def songLenght(lista, index):
	redanHittad=[]
	for i in range(index):
		longest=lista[0]
		for j in range(len(lista)):
			curretPointer=lista[j]
			if (longest < curretPointer) and not (curretPointer in redanHittad):
				longest=curretPointer
		redanHittad.append(longest)
		# print("Den", i, "längsta låtlängden är", longest.songLen)
	return longest.songLen

def mergesort(data):
	if len(data) > 1:
	    mitten = len(data)//2
	    vensterHalva = data[:mitten]
	    hogerHalva = data[mitten:]

	    mergesort(vensterHalva)
	    mergesort(hogerHalva)

	    i, j, k = 0, 0, 0

	    while i < len(vensterHalva) and j < len(hogerHalva):
	        if vensterHalva[i] < hogerHalva[j]:
	            data[k] = vensterHalva[i]
	            i = i + 1
	        else:
	            data[k] = hogerHalva[j]
	            j = j + 1
	        k = k + 1

	    while i < len(vensterHalva):
	        data[k] = vensterHalva[i]
	        i = i + 1
	        k = k + 1

	    while j < len(hogerHalva):
	        data[k] = hogerHalva[j]
	        j = j + 1
	        k = k + 1
	return data

def readfile(filename, nr):
    with open(filename, "r", encoding = "utf-8") as songFile:
        songFile=islice(songFile, nr)
        for row in songFile:
            ID=row.strip()
            ID=ID.split("\t")
            songData=song(ID)
            trackList.append(songData)
            if songData.artist in trackDictionary:
                dublett=[trackDictionary[songData.artist]]
                dublett.append(songData)
                trackDictionary[songData.artist]=dublett
            else:
                trackDictionary[songData.artist]=songData
        return trackList, trackDictionary

if __name__ == '__main__':
    filename = "sang-artist-data.txt"
    number_songs=1000

    trackList=[]
    trackDictionary={}

    lista, dictionary = readfile(filename, number_songs)

    antal_element = len(lista)
    print("Antal element =", antal_element)
    sista = lista[antal_element-1]
    testartist = sista.artist

    a=2
    print("The", a, ":th longest song is",songLenght(lista, a), "seconds long")

    linsok = timeit.timeit(stmt = lambda: songLenght(lista, 17), number = 1000)
    print("linjärsökningen tog", round(linsok, 4) , "sekunder")
    mergetid = timeit.timeit(stmt = lambda: mergesort(lista), number = 1000)
    print("Mergesorteringen tog", round(mergetid, 4) , "sekunder\n")