import time
import heapq

class Node:
    def __init__(self, pos, direction, pathCost):
        self.pos = pos
        self.dir = direction
        self.pathCost = pathCost

    def __lt__(self, other):
        return self.pathCost < other.pathCost
    
    def __repr__(self):
        dirmap = ["UP", "RIGHT", "DOWN", "LEFT"]
        return str(self.pos) +" "+ dirmap[self.dir] +" "+ str(self.pathCost)

def main():
    fname = "./input.txt"
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    f = open(fname)
    lines = [line[:-1] for line in f.readlines()]
    f.close()
    return lines
"""
    input size is 19_881 characters. Problem type is shortest path (dijkstra) with restriction
    what is the shortest path from coordinate (i,j) moving dir? make offers for people within length 3.
    Only restriction is you have to change direction each time, so it's a little tricky.
    A Node consists of coordinates (i,j) and the next direction DIR you will be moving in.
    Node A is adjacent to Node B if the vector AB points in A.DIR and B.DIR is perpendicular to
    A.DIR and exactly one coordinate differs by at most 3. Any given node A is adjacent to at most
    6 other nodes, depending on space. So there are V = 19_881 * 4 vertices in the graph and 
    at most E = V*6 directed edges.
"""
def answer(lines):
    n = len(lines)
    m = len(lines[0])
    costs = [[int(x) for x in y] for y in lines]
    start = (0,0)
    end = (n-1,m-1)
    return modified_dijkstra(start, end, costs)

def modified_dijkstra(start, end, costs):
    n = len(costs)
    m = len(costs[0])
    UP, RIGHT, DOWN, LEFT = list(range(4))
    h = [Node(start, DOWN, 0), Node(start, RIGHT, 0)]
    heapq.heapify(h)
    visited = set()
    while len(h):
        node = heapq.heappop(h)
        if node.pos == end:
            return node.pathCost
        state = (node.pos[0], node.pos[1], node.dir)
        if state in visited:
            continue
        visited.add(state)
        children = get_children(node, costs)
        for child in children:
            heapq.heappush(h, child)
        

def get_children(node, costs):
    direction = node.dir
    coords = node.pos
    delta = deltaDir(direction)
    children = []
    cost = node.pathCost
    for i in range(1,4):
        coords = add(coords, delta)
        if inBounds(coords, len(costs), len(costs[0])):
            cost += costs[coords[0]][coords[1]]
            for perp in perpDirs(direction):
                children.append(Node(coords, perp, cost))
    return children

def add(coord1, coord2):
    L = []
    for i in range(len(coord1)):
        L.append(coord1[i] + coord2[i])
    return tuple(L)

def inBounds(coords, n, m):
    return 0 <= coords[0] < n and 0 <= coords[1] < m

def deltaDir(direction):
    UP, RIGHT, DOWN, LEFT = list(range(4))
    if direction == UP:
        return (-1,0)
    elif direction == RIGHT:
        return (0,1)
    elif direction == DOWN:
        return (1,0)
    else:
        return (0,-1)

def perpDirs(direction):
    UP, RIGHT, DOWN, LEFT = list(range(4))
    dirs = [UP,RIGHT,DOWN,LEFT]
    return list(filter(lambda x: bool((direction + x)%2), dirs))
t = time.time()
main() 
print("finished in", time.time() - t, "seconds")