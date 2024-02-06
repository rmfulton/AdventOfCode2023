import time
from heapq import heappush, heappop
# import 

class Brick:
    def __init__(self, line, identifier):
        self.ID = identifier
        left, right = line.split("~")
        self.p1 = [int(x) for x in left.split(",")]
        self.p2 = [int(x) for x in right.split(",")]
        self.restsOn = set() 
        self.supports = set()

    def updateCoords(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def isSingleParent(self):
        for b in self.supports:
            if len(b.restsOn) == 1:
                return True
        return False

    def descendByOne(self):
        dx = [0,0,-1]
        newp1 = [self.p1[i] + dx[i] for i in range(3)]
        newp2 = [self.p2[i] + dx[i] for i in range(3)]
        self.updateCoords(newp1,newp2)
    
    def coordsOccupied(self):
        delta = [ (self.p2[i] - self.p1[i]) // max(1,abs(self.p1[i] - self.p2[i])) for i in range(3) ]
        x = self.p1
        occupied = []
        occupied.append(x)
        while x != self.p2:
            x = [x[i] + delta[i] for i in range(3)]
            occupied.append(x)
        return occupied

    def coordsBeneath(self):
        occupied = self.coordsOccupied()
        dx = [0,0,-1]
        beneath = []
        for coord in occupied:
            under = [coord[i] + dx[i] for i in range(3)]
            beneath.append(under)
        return beneath

    def isSupported(self, occupied):
        if self.height() == 1:
            return True
        answer = False
        for coord in self.coordsBeneath():
            t = tuple(coord)
            if t in occupied:
                self.restsOn.add(occupied[t])
                occupied[t].supports.add(self)
                answer = True
        return answer


    def canBeDisintegrated(self):
        return not(self.isSingleParent())
    
    def height(self):
        return min(self.p1[2],self.p2[2])
        
    def __lt__(self, other):
        return self.height() < other.height()
    
    def __repr__(self):
        res = self.char
        res += "\n" + "supports: " + "".join([el.char + " " for el in self.supports])
        res += "\n" + "restsOn: " + "".join([el.char + " " for el in self.restsOn])
        res += "\n" + str(self.p1) + str(self.p2)
        res += "\n"
        return res

class Bricks:
    def __init__(self, bricks):
        self.brickQ = bricks
    def addBrick(self, b):
        self.bricks.append(b)
    def getBricks(self,lines):
        i = 0
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        L = len(chars)
        for line in lines:
            identifier = chars[i//L] + chars[i % L]
            heappush(self.brickQ, Brick(line, identifier))
            i += 1
    def settle(self):
        newQ = []
        occupiedCoords = {}
        while len(self.brickQ):
            b = heappop(self.brickQ)
            while not b.isSupported(occupiedCoords):
                b.descendByOne()
            for coord in b.coordsOccupied():
                occupiedCoords[tuple(coord)] = b
            heappush(newQ, b)
        self.brickQ = newQ



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
    bricks = Bricks([])
    bricks.getBricks(lines)
    bricks.settle()
    count = 0
    for brick in bricks.brickQ:
        count += brick.canBeDisintegrated()
    return count




t = time.time()
main() 
print("finished in", time.time() - t, "seconds")