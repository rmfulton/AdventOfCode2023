import time

class State:
    def __init__(self, location, visited):
        self.loc = location
        self.visited = visited

    def getChildStates(self, lines):
        valid_neighbors = self.getValidNeighbors(lines)
        new_neighbors = list(filter(lambda x: x not in self.visited, valid_neighbors))
        states = []
        for n in new_neighbors:
            visited = {x for x in self.visited}
            visited.add(n)
            states.append(State(n, visited))
        return states
    
    def getValidNeighbors(self, lines):
        i, j = self.loc
        n, m = len(lines), len(lines[0])
        candidates = [ (i-1,j), (i+1, j), (i, j-1), (i,j+1) ]
        inBounds = list(filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < m, candidates))

        acceptableValues = {(1,0): '.v', (0,1): '.>', (-1,0): '.^', (0,-1): '.<'}
        vec_minus = lambda x, y: tuple([x[i] - y[i] for i in range(len(x))])
        linesAt = lambda x: lines[x[0]][x[1]]
        properValues = filter(lambda x: linesAt(x) in acceptableValues[ vec_minus(x,self.loc) ], inBounds)

        return properValues




def main(t):
    fname = "./sample.txt"
    lines = getLines(fname)
    res = answer(lines,t)
    print(res)

def getLines(fname):
    with open(fname) as f:
        lines = [line[:-1] for line in f.readlines()]
    return lines

def answer(lines,t):
    n = len(lines)
    m = len(lines[0])
    dest = (n-1,m-2)
    stateStack = initializeStateStack(lines)
    longestPath = 0
    numPaths = 0
    while len(stateStack):
        s = stateStack.pop()
        if s.loc == dest:
            longestPath = max(longestPath, len(s.visited))
            numPaths += 1
            if numPaths % 100 == 0:
                print(longestPath, numPaths, time.time() - t)
            continue
        for state in s.getChildStates(lines):
            stateStack.append(state)
    return longestPath - 1, numPaths

def initializeStateStack(lines):
    i = 0
    j = 1
    loc = (i,j)
    visited = set([loc])
    state = State(loc, visited)
    stateStack = [state]
    return stateStack



t = time.time()
main(t) 
print("finished in", time.time() - t, "seconds")