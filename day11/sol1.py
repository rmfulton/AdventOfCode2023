
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
    lines = expandLines(lines)
    galaxyCoords = getGalaxyCoords(lines)
    s = 0
    for i in range(len(galaxyCoords)):
        c1 = galaxyCoords[i]
        for j in range(i+1, len(galaxyCoords)):
            c2 = galaxyCoords[j]
            s += taxicab(c1,c2) 
    return s

def expandLines(lines):
    n = len(lines)
    m = len(lines[0])
    rowsToDuplicate = [True for _ in range(n)]
    columnsToDuplicate = [True for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if lines[i][j] == "#":
                rowsToDuplicate[i] = False
                columnsToDuplicate[j] = False
    return duplicated(lines, rowsToDuplicate, columnsToDuplicate)

def duplicated(lines, rowsToDuplicate, columnsToDuplicate):
    n = len(rowsToDuplicate)
    m = len(columnsToDuplicate)
    newLines = []
    for i in range(n):
        s = ""
        for j in range(m):
            s += lines[i][j]
            if columnsToDuplicate[j]:
                s += lines[i][j]
        newLines.append(s)
        if rowsToDuplicate[i]:
            newLines.append(s)
    return newLines

def getGalaxyCoords(lines):
    coords = []
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j in range(m):
            if lines[i][j] == "#":
                coords.append((i,j))
    return coords

def taxicab(c1,c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


main() 