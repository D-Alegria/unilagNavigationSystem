import math, gc


class Node:
    def __init__(self, place, latitude, longitude):
        self.name = place
        self.longitude = longitude
        self.latitude = latitude

    def getAddress(self):
        address = [self.latitude, self.longitude]
        return address

    def getName(self):
        return self.name

    def getCost(self, toNode):
        x = math.pow((toNode.latitude - self.latitude), 2)
        y = math.pow((toNode.longitude - self.longitude), 2)
        return math.sqrt(x + y)

    def __str__(self):
        return str(self.name)


class Graph:
    def __init__(self):
        self.vertices = {}

    def addNode(self, fromWhere, toWhere):
        map = {}
        if not type(toWhere) is tuple:
            map[toWhere] = fromWhere.getCost(toWhere)
        else:
            for node in toWhere:
                map[node] = fromWhere.getCost(node)
        self.vertices[fromWhere] = map

    def find_shortest_path(self, source, destination):
        distances = {}
        previous = {}
        nodes = {}
        visited = []
        un_visited = {}

        for key, value in self.vertices.items():
            nodes[key] = value
            distances[key] = math.inf
            previous[key] = None
            un_visited[key] = math.inf
            if key == source:
                distances[key] = 0
                un_visited[key] = 0
                previous[key] = key

        while nodes:
            shortest = min(un_visited, key=un_visited.get)
            un_visited.pop(shortest)
            visited.append(shortest)
            for neighbour in self.vertices[shortest]:
                cost = distances[shortest] + self.vertices[shortest][neighbour]
                if cost < distances[neighbour]:
                    distances[neighbour] = cost
                    previous[neighbour] = shortest
                    if neighbour in un_visited:
                        un_visited[neighbour] = cost

            if shortest == destination:
                print("The shortest path from {0} to {1}".format(source, destination))
                print("=" * 50)
                path = []
                while previous[shortest]:
                    path.append(shortest)
                    shortest = previous[shortest]
                    if shortest in path:
                        path.reverse()
                        break
                for index in range(len(path) - 1):
                    next_index = index + 1
                    print("Move from {0} to {1}".format(path[index], path[next_index]))
                print(
                    "The shortest distance from {0} to {1} is {2}m".format(source, destination, distances[destination]))
                break
            if distances[shortest] == math.inf:
                break

    def getNodes(self):
        for obj in gc.get_objects():
            if isinstance(obj, Node):
                print(obj.getName())

    def getNodebyName(self, name):
        for obj in gc.get_objects():
            if isinstance(obj, Node):
                if obj.getName() == name:
                    return obj


def main():
    unilagMap = Graph()

    # Node
    # Utilities
    unilagGate = Node("Unilag gate", 10, 22)
    secondGate = Node("Second gate", 5, 3)
    ubaPark = Node("Uba park", 13, 22)
    fireStation = Node("Fire Station", 32, 23)
    medicalCenter = Node("Medical Center", 34, 14)
    sportCenter = Node("Sport Center", 21, 19)
    cathedral = Node("Cathedral", 19, 22)
    mosque = Node("Mosque", 21, 24)
    mainLibrary = Node("Main Library", 42, 26)
    senate = Node("Senate", 39, 24)
    dli = Node("DLI", 24, 9)
    lagoonFront = Node("Lagoon front", 44, 23)
    mainAuditorium = Node("Main Auditorium", 43, 24)
    multiHall = Node("Multipurpose Hall", 17, 19)
    yemyem = Node("Unilag Shopping complex", 27, 23)
    newHall = Node("New Hall", 26, 24)
    busTerminal = Node("Bus terminal", 30, 22)
    cits = Node("CITS", 33, 22)
    powerStation = Node("Power Station", 34, 23)
    bookShop = Node("Book Shop", 38, 23)

    # Faculties
    edu = Node("Education", 14, 18)
    science = Node("Science", 41, 14)
    fss = Node("Social Sciences", 24, 17)
    art = Node("Art", 38, 25)
    law = Node("Law", 39, 26)
    eng = Node("Engineering", 42, 22)

    # Hostel
    guestHouse = Node("Guest House", 35, 24)
    # male
    jaja = Node("Jaja Hall", 39, 18)
    mariere = Node("Mariere Hall", 38, 21)
    eniNjoku = Node("Eni Njoku Hall", 29, 24)
    biobaku = Node("Biobaku Hall", 16, 16)

    # females
    moremi = Node("Moremi Hall", 36, 21)
    mTH = Node("Madam Tinubu Hall", 25, 26)
    fagunwa = Node("Fagunwa Hall", 27, 25)
    kofo = Node("Kofo Hall", 13, 16)
    # amina = unilagMap.addNode("Amina Hall")
    # honours = unilagMap.addNode("Honours")

    # Egdes
    # unilagGate
    unilagMap.addNode(unilagGate, (ubaPark, edu, multiHall))
    # secondGate
    unilagMap.addNode(secondGate, (dli))
    # ubaPark
    unilagMap.addNode(ubaPark, (cathedral, unilagGate))

    # fireStation
    unilagMap.addNode(fireStation, (powerStation, newHall, eniNjoku))
    # medicalCenter
    unilagMap.addNode(medicalCenter, (dli, science, jaja, moremi))
    # sportCenter
    unilagMap.addNode(sportCenter, (multiHall, yemyem))
    # cathedral
    unilagMap.addNode(cathedral, (mosque, ubaPark))
    # mosque
    unilagMap.addNode(mosque, (cathedral, newHall))
    # mainLibrary
    unilagMap.addNode(mainLibrary, (mainAuditorium, senate, law))
    # senate
    unilagMap.addNode(senate, (bookShop, guestHouse, art, law, mainAuditorium, mainLibrary))
    # dli
    unilagMap.addNode(dli, (science, newHall, biobaku, secondGate))
    # lagoonFront
    unilagMap.addNode(lagoonFront, (eng, mainAuditorium))
    # mainAuditorium
    unilagMap.addNode(mainAuditorium, (lagoonFront, eng, mainLibrary, senate))
    # multiHall
    unilagMap.addNode(multiHall, (sportCenter, edu, unilagGate))
    # yemyem
    unilagMap.addNode(yemyem, (fss, newHall, sportCenter, busTerminal))
    # newHall
    unilagMap.addNode(newHall, (mosque, fagunwa, mTH, eniNjoku, fireStation, yemyem))
    # busTerminal
    unilagMap.addNode(busTerminal, (cits, yemyem))
    # cits
    unilagMap.addNode(cits, (busTerminal, bookShop, moremi))
    # powerStation
    unilagMap.addNode(powerStation, (guestHouse, fireStation))
    # bookShop
    unilagMap.addNode(bookShop, (senate, mariere, cits, moremi))
    # edu
    unilagMap.addNode(edu, (unilagGate, kofo, biobaku, multiHall))
    # science
    unilagMap.addNode(science, (medicalCenter, jaja))
    # fss
    unilagMap.addNode(fss, (dli, yemyem))
    # art
    unilagMap.addNode(art, (senate, law))
    # law
    unilagMap.addNode(law, (art, mainLibrary, senate))
    # eng
    unilagMap.addNode(eng, (lagoonFront, mainAuditorium, mariere))
    # guestHouse
    unilagMap.addNode(guestHouse, (senate, powerStation))
    # jaja
    unilagMap.addNode(jaja, (science, mariere, medicalCenter, moremi))
    # mariere
    unilagMap.addNode(mariere, (eng, bookShop, jaja, moremi))
    # eniNjoku
    unilagMap.addNode(eniNjoku, (newHall, mTH, fireStation))
    # biobaku
    unilagMap.addNode(biobaku, (dli, kofo, edu))
    # moremi
    unilagMap.addNode(moremi, (bookShop, mariere, jaja, cits, medicalCenter))
    # mTH
    unilagMap.addNode(mTH, (eniNjoku, newHall))
    # fagunwa
    unilagMap.addNode(fagunwa, (newHall, mTH))
    # kofo
    unilagMap.addNode(kofo, (biobaku, edu))
    # amina
    # honours

    unilagMap.getNodes()
    print("Hint copy and paste location\n")
    source = unilagMap.getNodebyName(input("Enter where you are:"))
    destination = unilagMap.getNodebyName(input("Enter where you are going to: "))
    unilagMap.find_shortest_path(source, destination)

    # def getInput():|


main()
