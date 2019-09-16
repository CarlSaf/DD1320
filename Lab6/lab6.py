#stmt = statement, d som säger vad man ska ta tid på
#number = Time number executions of the main statement. This executes the setup statement once, and then returns the time it takes to execute the main statement a number of times, measured in seconds as a float.
#timeit = sätt att ta kort på korta delar av pythonkod
#vad skrivs ut?= returnerar tidtagningen i sekunder

class song:
    def __init__(self, data):
        self.trackID=data[0]
        self.songID=data[1]
        self.artist=data[2]
        self.songName=data[3]
        
    def __lt__(self, other):
        pass

    def __str__(self):
        return "\n\nTrack Id: " + str(self.trackID) + "\nSong Id: " + str(self.songID) + "\nArtist: " + str(self.artist) + "\nSong Name: " + str(self.songName)


if __name__ == '__main__':

    trackList=[]
    trackDictionary={}

    with open("unique_tracks_short.txt", "r", encoding = "utf-8") as songFile:
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
    
    print(trackDictionary['Tiger Lou'][0])
    print(len(trackList))
    print(len(trackDictionary))