
def main():
    fname = "./input.txt"
    lines = getLines(fname)
    res = answer(lines)
    writeFile(res)

def getLines(fname):
    f = open(fname)
    lines = [line[:-1] for line in f.readlines()]
    f.close()
    return lines

def writeFile(res):
    fname = "./output.txt"
    f = open(fname, 'w')
    f.writelines(res)
    f.close()

def answer(lines):
    lines = [list(s) for s in lines]
    start = findStart(lines)
    prevLeft = start
    prevRight = start
    left, right = findInitials(start, lines)
    visited = {start, left, right}
    while left != right:
        left, prevLeft = update(prevLeft, left, lines), left
        right, prevRight = update(prevRight, right, lines), right
        visited.add(left)
        visited.add(right)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i,j) not in visited:
                lines[i][j] = "."
    return ["".join(chars)+ "\n" for chars in lines]
    
def findStart(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return (i,j)

def findInitials(start, lines):
    rows = len(lines)
    cols = len(lines[0])
    neighbors = getNeighbors(start, rows, cols)
    initials = []
    for neighbor in neighbors:
        if start in pointsAt(neighbor, lines):
            initials.append(neighbor)
    return initials

def update(previous, current, lines):
    for val in pointsAt(current, lines):
        if val != previous:
            return val

def getNeighbors(start, rows, cols):
    neighbors = []
    i,j = start
    if i < rows - 1:
        neighbors.append((i+1, j))
    if i > 0:
        neighbors.append((i-1, j))
    if j < cols - 1:
        neighbors.append((i, j+1))
    if j > 0:
        neighbors.append((i, j-1))
    return neighbors

def pointsAt(current, lines):
    i,j = current
    val = lines[i][j]
    if val == "|":
        return  [(i+1, j), (i-1,j)]
    if val == "-":
        return [(i, j+1), (i,j-1)]
    if val == "F":
        return [(i+1, j), (i, j+1)]
    if val == "7":
        return [(i+1, j), (i, j-1)]
    if val == "L":
        return [(i-1, j), (i, j+1)]
    if val == "J":
        return [(i-1, j), (i, j-1)]
    if val == ".":
        return []

main() 