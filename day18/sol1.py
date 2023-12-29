import time

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

def answer(lines):
    directions, distances, colors = getPieces(lines)
    lines = tracePath(directions, distances)
    ans = areaInside(lines)
    return ans

def tracePath(directions, distances):
    L = len(directions)
    startCoord, n, m = getPlacement(directions, distances)
    print("dimensions:", n,m)
    symbols = [["." for _ in range(m)] for _ in range(n)]
    coords = startCoord
    for i in range(L):
        prevDirection = directions[i-1]
        currentDirection = directions[i]
        s = prevDirection + currentDirection
        d = distances[i]
        for _ in range(d):
            setSymbol(symbols, coords, s)
            s = currentDirection
            coords = addVecs(coords, toVec(currentDirection))
    [print("".join(line)) for line in symbols]
    return symbols



"""
stolen + modified from day10
"""
def areaInside(lines):
    numEnclosed = 0
    for line in lines:
        isInside = 0
        direction = 0
        for char in line:
            if char == "." and isInside == 0:
                continue
            numEnclosed += 1
            if char == "|":
                isInside = 1 - isInside
            elif char == "F":
                direction = 1
            elif char == "L":
                direction = -1
            elif char == "7":
                if direction == -1:
                    isInside = 1 - isInside
                direction = 0
            elif char == "J":
                if direction == 1:
                    isInside = 1 - isInside
                direction = 0
    return numEnclosed

def getPlacement(directions, distances):
    top = 0
    bottom = 0
    left = 0
    right = 0
    coords = [0,0]
    n = len(directions)
    for i in range(n):
        d = distances[i]
        vec = [x*d for x in toVec(directions[i])]
        coords = addVecs(coords, vec)
        top = min(top, coords[0])
        bottom = max(bottom, coords[0])
        left = min(left, coords[1])
        right = max(right, coords[1])
    n = bottom - top + 1
    m = right - left + 1
    coord1 = -top
    coord2 = -left
    return (coord1, coord2), n, m

def setSymbol(symbols, coords, currentDirection):
    # print("coords", coords)
    c = getChar(currentDirection)
    symbols[coords[0]][coords[1]] = c

def getChar(s):
    if s in "RL":
        return "-"
    if s in "UD":
        return "|"
    if s in ["UR", "LD"]:
        return "F"
    if s in ["RD", "UL"]:
        return "7"
    if s in ["DL", "RU"]:
        return "J"
    if s in ["LU", "DR"]:
        return "L"

def getPieces(lines):
    n = len(lines)
    directions = []
    distances = []
    colors = []
    for line in lines:
        x = line.split()
        directions.append(x[0])
        distances.append(int(x[1]))
        colors.append(x[2][1:-1])
    return directions, distances, colors

def toVec(direction):
    if direction == "L":
        return [0,-1]
    if direction == "R":
        return [0,1]
    if direction == "U":
        return [-1,0]
    if direction == "D":
        return [1,0]

def addVecs(v1,v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]

t = time.time()
main() 
print("finished in", time.time() - t, "seconds")