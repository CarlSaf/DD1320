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

def readfile(filename, nr):
    with open(filename, "r", encoding = "utf-8") as songFile:
        songFile=islice(songFile, nr)
        for row in songFile:
            ID=row.strip()
            ID=ID.split("\t")
            songData=song(ID)
            dictionary_hash.store(songData.artist, songData)

class DictHash:
    def __init__(self):
        self.HD={}
        print("nu skapas en dict")

    def __contains__(self, nyckel):
        return key in self.dictionary_hash

    def store(self, key, data):
        hkey=hash(key)
        self.HD[hkey]=data

    def search(self, key):
        key=hash(key)
        if key in self.HD:
            return self.HD[key]
        else:
            return False

if __name__ == '__main__':
    filename = "sang-artist-data.txt"
    number_songs=1000
    dictionary_hash=DictHash()

    readfile(filename, number_songs)

    test_key="Aerosmith"
    print(dictionary_hash.search(test_key))