#Testar klassen Hashtabell i filen hashfil.py
from hashfil import Hashtabell

class Atom:

    def __init__(self, namn, vikt):
        self.namn = namn
        self.vikt = vikt

    def __str__(self):
        return "{" + self.namn + " " +  str(self.vikt) + "}"

def skapaAtomlista():
    """Returnerar en lista med atomernas namn och vikt"""
    print("\n-------------------------------------------------------")
    print(" * Skapar en lista med alla atomer...")
    data = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"
    atomlista = data.split(";")
    return atomlista

def lagraHashtabell(atomlista):
    """Lagrar atomlistans element i en hashtabell"""
    print("\n-------------------------------------------------------")
    print(" * Lagrar listans atomer i hashtabell...")
    antalElement = len(atomlista)
    hashtabell = Hashtabell(antalElement)
    for element in atomlista:
        namn, vikt = element.split()
        nyAtom = Atom(namn, float(vikt))
        hashtabell.store(namn, nyAtom)
    return hashtabell

def allaAtomerFinns(hashtabell, atomlista):
    """Kan man hitta alla atomer i hashtabellen?"""
    antal = 0
    OK = True
    print("\n-------------------------------------------------------")
    print(" * Testar att hitta alla atomer i hashtabellen...")
    for kontrollAtom in atomlista:
        namn, vikt = kontrollAtom.split()
        vikt = float(vikt)
        try:
            hashadAtom = hashtabell.search(namn)
            # print("Längd på krocklista:",len(hashadAtom))
            for i in range(len(hashadAtom)):
                Atom_finns=False
                
                if hashadAtom[i].value.vikt == vikt:
                    print(hashadAtom[i].value)
                    antal += 1
                    Atom_finns=True
                    break

            if Atom_finns is False:
                print(namn, "har fel vikt.")
        except KeyError:
            print(namn, "fanns inte med i hashtabellen.")
            OK = False
    print( antal, "element hashades korrekt.")
    return OK

def knasAtomFinnsInte(hashtabell):
    """Ger hashtabellen KeyError om vi testar med atom som inte finns?"""
    knasnamn = "Zz"
    print("\n-------------------------------------------------------")
    print( " * Testar att hitta en atom som inte finns:", knasnamn, "...")
    try:
        atom = hashtabell.search(knasnamn)
        print("Hejes")
        print(knasnamn, "fanns med i hashtabellen.")
        return False
    except KeyError:
        print(knasnamn, "fanns inte med i hashtabellen.")
        return True

atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)
allaAtomerFinns(hashtabell, atomlista)    
knasAtomFinnsInte(hashtabell)
