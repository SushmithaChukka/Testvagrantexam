from collections import Counter


class Planet:
    def __init__(self, name, gasses, moons, hasrings):
        self.name = name
        self.gasses = gasses
        self.moons = moons
        self.hasrings = hasrings
planet = Planet("Mercury","",0,"No")
planet1 = Planet("Venus","carbondioOxide, Nitrogen",0,"No")
planet2 = Planet("Earth","Nitrogen, Oxygen",1,"No")
planet3 = Planet("Jupitor","Hydrogen , Helium",79,"Yes")
planet4 = Planet("Saturn","Hydrogen , Helium",83,"Yes")
planet5 = Planet("Uranus","Hydrogen , Helium, Methane",27,"Yes")
planets = []
planets.append(planet)
planets.append(planet1)
planets.append(planet2)
planets.append(planet3)
planets.append(planet4)
planets.append(planet5)

print(planets)
def countofmoons(planets):
    summ =0
    for i in planets:
        if i.hasrings == "Yes":
            summ += i.moons
    return summ
print(countofmoons(planets))

def maxgas(planets):
    gassessublist = []
    for i in planets:
        gassessublist.append(i.gasses.split(","))
    gasseslist = [item for sublist in gassessublist for item in sublist]
    dictt = Counter(gasseslist)
    ll = [i for i in dictt if dictt[i]==max(list(dictt.values()))]
    return ll
print(maxgas(planets))
