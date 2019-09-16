from random import randint #hämtar randintklassen från ramdom-modulen

class Pokemon_class:    #Klass
    def __init__(self, data_list, nr):
        self.Name = data_list[nr][2]
        self.HP = data_list[nr][3]
        self.Att = data_list[nr][4]
        self.Type = data_list[nr][10]
        self.Weight = data_list[nr][16]
        self.nr = nr

    def __str__(self):
        return str(self.Name) + " -HP: " + str(self.HP) + " -Att: " + str(self.Att) + " -Type: " + str(self.Type) + " -Weight: " + str(self.Weight)

    def __lt__(self):
        if self.Weight > other.Weight:
            return True
        else:
            return False

    def __repr__(self):
        return str(self) #Printar lista m obj

    def metod5(self, max):
        return(randint(0,max))

class Gym:
    def __init__(self, pokemon_list):
        self.gymlist=pokemon_list

    def __str__(self):
        return "Första pokemon du kommer möta är: " + str(self.gymlist[0])

    def __repr__(self):
        return str(self) #Printar lista m obj

    def __contains__(self, pokemon):
        print(pokemon, "söks nu efter")
        return sokpokemon(pokemon)

def sokpokemon(pokemon):
    for i in range(int(number)):
        if pokemon == name_list[i]:
            print("den fanns")
            return True
    return False

def readData():
    filename="Pokedata.csv"
    pokemon_array=[]
    with open(filename, encoding = "utf-8") as pokemon_read:
        for pokemon in pokemon_read:
            pokemon_array.append(pokemon.split(","))
    return pokemon_array

def createPokemonList(pokemon_array, number):
    pokeList=[] 
    name_list=[]
    for i in range(int(number)):
        a=randint(0, len(pokemon_array))
        pokeList.append(Pokemon_class(pokemon_array, a))
        name_list.append(Pokemon_class(pokemon_array, a).Name)

    b=randint(0, len(pokeList)-1)
    c=randint(0, len(pokeList)-1)
    print(pokeList[b].Name,"har mer HP än",pokeList[c].Name)
    print(pokeList[b].HP < pokeList[c].HP,"\n")
    print(pokeList[b].Name,"har mer Att än",pokeList[c].Name)
    print(pokeList[b].Att < pokeList[c].Att,"\n")
    return(pokeList, name_list)

if __name__ == '__main__':
    pokemon_array=readData()
    number=input("Hur många pokemon vill du skapa i ditt gym: ")
    print("\n\n")

    pokemon_list, name_list =createPokemonList(pokemon_array, number)

    gym=Gym(pokemon_list)
    print(gym)

    print("\nGymlistan består utav:")
    for i in range(int(number)):
        print(gym.gymlist[i])

    a=True
    while a is True:
        b=input("\nSök efter en pokemon i gymlistan: ")
        c=(b in gym)
        if c is False:
            print(b,"fanns ej")
            break