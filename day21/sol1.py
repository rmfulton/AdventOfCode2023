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
    seedCoords = getStartCoord(lines)
    for _ in range(64):
        seedCoords = oneAway(seedCoords, lines)
    return len(seedCoords)

def getStartCoord(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return [(i,j)]

def oneAway(seedCoords, lines):
    res = set()
    n = len(lines)
    m = len(lines[0])
    for coord in seedCoords:
        neighbors = get_neighbors(coord, n, m)
        for point in neighbors:
            x,y = point
            if lines[x][y] in '.S':
                res.add((x,y))
    return res

def get_neighbors(coord, n, m):
    x,y = coord
    candidates = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    filtered = []
    for pt in candidates:
        if 0 <= pt[0] < n and 0 <= pt[1] < m:
            filtered.append(pt)
    return filtered


t = time.time()
main() 
print("finished in", time.time() - t, "seconds")