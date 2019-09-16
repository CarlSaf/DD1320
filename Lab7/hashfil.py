import timeit
import sys
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
    counter=0
    with open(filename, "r", encoding = "utf-8") as songFile:
        songFile=islice(songFile, nr)
        for row in songFile:
            ID=row.strip()
            ID=ID.split("\t")
            songData=song(ID)
            dictionary_hash.store(songData.artist, songData)
            counter+=1

class HashNode:
    def __init__(self, value, key):
        self.value=value
        self.key=key
        
class Hashtabell:
    def __init__(self, size):
        self.size=size
        self.HD=[None]*size
        print("nu skapas en dict med storlek med storlek", size)

    def __contains__(self, nyckel):
        pass
        # return check_keyerror(nyckel)

    def store(self, key, data):
        hkey=hash2(key, self.size)
        if self.HD[hkey] is None:
            self.HD[hkey]=[HashNode(data, hkey)]
        else:
            conflict_list=self.HD[hkey]
            conflict_list.append(HashNode(data, hkey))
            self.HD[hkey]=conflict_list

    def search(self, key):
        key_hashed=hash2(key, self.size)
        try:
            if self.HD[key_hashed] is not None:
                returnlist=[]
                for i in range(len(self.HD[key_hashed])):
                    if key == self.HD[key_hashed][i].value.namn:
                        returnlist.append(self.HD[key_hashed][i])
                if len(returnlist) != 0:
                    return returnlist
            raise KeyError
        except KeyError:
            print("KeyError, artisten finns inte i listan")
            sys.exit()

def hash2(s,size):             # Beräknar hashkoden för en sträng enligt
    result = 0            # s[0]*32^[n-1] + s[1]*32^[n-2] + ... + s[n-1]
    for c in s:                    
        result = result*32 + ord(c)
    # print(result%size)#, "\n")
    return (result%size)

if __name__ == '__main__':
    filename = "sang-artist-data.txt"
    number_songs=1000
    size=number_songs*2

    dictionary_hash=Hashtabell(size)
    readfile(filename, number_songs)

    test_key="a"
    dictionary_hash.search(test_key)
    test_key="Aerosmith"

    print(hash2("eva", size))
    print(hash2("ave", size))
    print(hash2("vea", size))


    nr_same=0
    if dictionary_hash.search(test_key) is not None:
        for i in range(len(dictionary_hash.search(test_key))):
            print(dictionary_hash.search(test_key)[i].value)
            print("key:",dictionary_hash.search(test_key)[i].key)
            nr_same+=1
        print("\nNumber of", test_key, "songs in the list are:", nr_same)