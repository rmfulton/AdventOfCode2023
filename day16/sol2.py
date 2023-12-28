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
    RIGHT, LEFT, UP, DOWN = list(range(4))
    n = len(lines)
    m = len(lines[0])
    starts = []
    for j in range(m):
        starts.append((0,j,DOWN))
        starts.append((n-1, j, UP))
    for i in range(n):
        starts.append((i, 0, RIGHT))
        starts.append((i, m-1, LEFT))
    
    bestScore = 0
    L = len(starts)
    for i in range(L):
        start = starts[i]
        if i % (L//10) == 0:
            print(f"{i*100//L}%")
        bestScore = max(bestScore, energyFrom(lines, start))
    return bestScore
    

def energyFrom(lines, start):
    RIGHT, LEFT, UP, DOWN = list(range(4))
    n = len(lines)
    m = len(lines[0])
    energized = [[False for _ in range(m)] for _ in range(n)]
    visited = set()
    stateQ = [start]
    while len(stateQ):
        state = stateQ.pop()
        row, col, direction = state
        if state in visited:
            continue
        energized[row][col] = True
        visited.add(state)

        symbol = lines[row][col]
        nextStates = getNextStates(row,col,direction, symbol)
        for state in nextStates:
            if inBounds(state[0], state[1], n, m):
                stateQ.append(state)
    for i in range(n):
        s = ""
        for j in range(m):
            if energized[i][j]:
                s += "#"
            else:
                s += "."
    return sum([sum(row) for row in energized])


def getNextStates(row, col, direction, symbol):
    RIGHT, LEFT, UP, DOWN = list(range(4))
    if direction == RIGHT:
        if symbol in ".-":
            return [(row, col+1, direction)]
        elif symbol == "|":
            return [(row-1, col, UP), (row+1, col, DOWN)]
        elif symbol == "/":
            return [(row-1, col, UP)]
        elif symbol == "\\":
            return [(row+1, col, DOWN)]

    elif direction == LEFT:
        if symbol in ".-":
            return [(row, col-1, direction)]
        elif symbol == "|":
            return [(row-1, col, UP), (row+1, col, DOWN)]
        elif symbol == "/":
            return [(row+1, col, DOWN)]
        elif symbol == "\\":
            return [(row-1, col, UP)]
    elif direction == UP:
        if symbol in ".|":
            return [(row-1, col, direction)]
        elif symbol == "-":
            return [(row, col+1, RIGHT), (row, col-1, LEFT)]
        elif symbol == "/":
            return [(row, col+1, RIGHT)]
        elif symbol == "\\":
            return [(row, col-1, LEFT)]
    elif direction == DOWN:
        if symbol in ".|":
            return [(row+1, col, direction)]
        elif symbol == "-":
            return [(row, col+1, RIGHT), (row, col-1, LEFT)]
        elif symbol == "/":
            return [(row, col-1, LEFT)]
        elif symbol == "\\":
            return [(row, col+1, RIGHT)]


def inBounds(row,col,n,m):
    return 0 <= row < n and 0 <= col < m

t = time.time()
main() 
print(time.time() - t)