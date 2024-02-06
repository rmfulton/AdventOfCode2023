import time

class Node:
    def __init__(self, name, coord, adj):
        self.name = name
        self.coord = coord
        self.adj = adj

class Graph:
    def __init__(self, lines):
        nodeLocations = self.getNodeLocations(lines)
        self.nodes = {}
        i = 0
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for loc in nodeLocations:
            self.nodes[loc] = Node( alphabet[i//26] + alphabet[i%26], loc, {})
            i += 1
        self.computeDistances(lines)
    
    def getNodeLocations(self, lines):
        n = len(lines)
        m = len(lines[0])
        locations = [(0,1), (n-1,m-2)]
        for i in range(n):
            for j in range(m):
                if lines[i][j] == "#":
                    continue
                neighbors = self.getNeighbors(lines, (i,j))
                if len(neighbors) > 2:
                    locations.append((i,j))
        return locations

    def computeDistances(self, lines):
        for loc, n in self.nodes.items():
            neighbors = self.getNeighbors(lines, n.coord)
            for loc2 in neighbors:
                d = 1
                current = loc2
                prev = loc
                while current not in self.nodes:
                    nextCurrent = list(filter(lambda x: x != prev, self.getNeighbors(lines, current)))[0]
                    prev = current
                    current = nextCurrent
                    d += 1
                self.nodes[loc].adj[current] = d
        
              
    def getNeighbors(self, lines, coord):
        i = coord[0]
        j = coord[1]
        n = len(lines)
        m = len(lines[0])
        candidates = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]
        inBounds = list(filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < m, candidates))
        charAt = lambda x: lines[x[0]][x[1]]
        validValues = list(filter(lambda x: charAt(x) != "#", inBounds))
        return validValues

    def longestPathBF(self, start, end):
        maxLength = 0
        pathStack = [(start, set([start]), 0)]
        while len(pathStack):
            current, visited, L = pathStack.pop()
            if current == end:
                if L > maxLength:
                    print(L)
                    maxLength = L
                continue
            neighbors = self.nodes[current].adj.keys()
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                newVisited = {element for element in visited}
                newVisited.add(neighbor)
                pathStack.append((neighbor, newVisited, L + self.nodes[current].adj[neighbor]))

        return maxLength




def main():
    fname = "./input.txt"
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    with open(fname) as f:
        lines = [line[:-1] for line in f.readlines()]
    return lines

def answer(lines):
    n, m = len(lines), len(lines[0])
    start = (0,1)
    end = (n-1, m-2)
    g = Graph(lines)
    return g.longestPathBF(start, end)



def printGraph(g):
    with open("graph.dot", 'w') as f:
        s = "graph {\n"
        i = 0
        lines = [s]
        visited = set()
        for node in g.nodes.values():
            if node in visited:
                continue
            for key in node.adj:
                n2 = g.nodes[key]
                if n2 in visited:
                    continue
                lines.append(node.name + " -- " + n2.name + f' [label= {node.adj[key]}]'+ "\n")
            visited.add(node)
        lines.append("}\n")
        f.writelines(lines)
    



t = time.time()
main() 
print("finished in", time.time() - t, "seconds")