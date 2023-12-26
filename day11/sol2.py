
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
    prd, pcd = expandLines(lines)
    galaxyCoords = getGalaxyCoords(lines)
    s = 0
    for i in range(len(galaxyCoords)):
        c1 = galaxyCoords[i]
        for j in range(i+1, len(galaxyCoords)):
            c2 = galaxyCoords[j]
            s += taxicab(c1,c2, prd, pcd) 
    return s

def expandLines(lines):
    n = len(lines)
    m = len(lines[0])
    duplicationFactor = 2
    rowDistance = [duplicationFactor for _ in range(n)]
    columnDistance = [duplicationFactor for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if lines[i][j] == "#":
                rowDistance[i] = 1
                columnDistance[j] = 1
    return getPrefixSum(rowDistance), getPrefixSum(columnDistance)
"""
arr[i] should return the sum up to and including the ith element
arr[j] - arr[i] should return the sum of all elements between i and j,
excluding i and including j.
"""
def getPrefixSum(arr):
    prefixs = [0]
    for element in arr:
        prefixs.append(prefixs[-1] + element)
    return prefixs[1:]


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

def taxicab(c1,c2, prd, pcd):
    return abs(prd[c1[0]] - prd[c2[0]]) + abs(pcd[c1[1]] - pcd[c2[1]])


main() 