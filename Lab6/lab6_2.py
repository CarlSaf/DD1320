import timeit
from itertools import islice

class song:
    def __init__(self, data):
        self.trackID=data[0]
        self.songID=data[1]
        self.artist=data[2]
        self.songName=data[3]
        
    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        else:
            return False

    def __str__(self):
        return "\n\nTrack Id: " + str(self.trackID) + "\nSong Id: " + str(self.songID) + "\nArtist: " + str(self.artist) + "\nSong Name: " + str(self.songName)

def linsok(the_list, key):
    for x in the_list:
        if x == key:
            return True
    return False

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

def binary_search(the_list, key):
   low = 0
   high = len(the_list)-1
   found = False

   while low <= high and not found:
      middle = (low + high)//2
      if the_list[middle].artist == key:
         found = True
      else:
         if key < the_list[middle].artist:
            high = middle - 1
         else:
            low = middle + 1
   return found

def readfile(filename, nr):
    with open(filename, "r", encoding = "utf-8") as songFile:
        songFile=islice(songFile, nr)
        for row in songFile:
            ID=row.strip()
            ID=ID.split("<SEP>")
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
    filename = "unique_tracks.txt"
    number_songs=1000

    trackList=[]
    trackDictionary={}

    lista, dictionary = readfile(filename, number_songs)

    antal_element = len(lista)
    print("Antal element =", antal_element)
    sista = lista[antal_element-1]
    testartist = sista.artist

    sorted_lista=mergesort(lista)

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 1000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
    bintid = timeit.timeit(stmt = lambda: binary_search(sorted_lista, testartist), number = 1000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")
    mergetid = timeit.timeit(stmt = lambda: mergesort(lista), number = 1000)
    print("Mergesorteringen tog", round(mergetid, 4) , "sekunder\n")