import math


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
        self.vertices[fromWhere] = toWhere

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
            print(shortest)
            un_visited.pop(shortest)
            visited.append(shortest)
            for neighbour in self.vertices[shortest]:
                cost = distances[shortest] + self.vertices[shortest][neighbour]
                if cost < distances[neighbour]:
                    distances[neighbour] = cost
                    previous[neighbour] = shortest
                    if neighbour in un_visited:
                        un_visited[neighbour] = cost
            print(distances)
            print(previous)
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


def main():
    unilagMap = Graph()

    unilagMap.addNode("A", {"B": 8, "C": 2, "D": 5})
    unilagMap.addNode("B", {"A": 8, "D": 2, "F": 13})
    unilagMap.addNode("C", {"A": 2, "D": 2, "E": 5})
    unilagMap.addNode("D", {"A": 5, "B": 2, "C": 2, "E": 1, "F": 6, "G": 3})
    unilagMap.addNode("E", {"C": 5, "D": 1, "G": 1})
    unilagMap.addNode("F", {"B": 13, "D": 6, "H": 3, "G": 2, "I": 2})
    unilagMap.addNode("G", {"D": 3, "E": 1, "F": 2, "H": 6})
    unilagMap.addNode("H", {"F": 3, "G": 6})
    unilagMap.addNode("I", {"F": 2})

    unilagMap.find_shortest_path("A", "I")


main()
