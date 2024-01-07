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
"""
solution approach: 
    write a slow solution that can be tested on the sample, then 
    write a fast solution that can run on the input, and
    test the fast solution against the slow solution before accepting

"""
def answer(lines):
    start = getStart(lines)
    S = 26501365
    # slow_ans = exactlySAwayQuadratic(lines, start, S)
    d = getDiagonals(lines, S, start)
    s = getSides(lines, S, start)
    c = getCenter(lines, S, start)
    return d + s + c

def getCenter(lines, S, start):
    d = distances(lines, start)
    res = reachable(d,S)
    return res

def getSides(lines,S, start):
    n, m = len(lines), len(lines[0])
    sides = [(start[0], m-1), (start[0], 0), (n-1, start[1]), (0, start[1])]
    res = 0
    for pt in sides:
        res += sideContribution(start, lines,S,pt)
    return res

def exactlySAwayQuadratic(lines, start, S):
    frontier = {start}
    prevFrontier = set()

    numKaway = [0 for _ in range(S+1)]
    ans = 0
    for i in range(S+1):
        L = len(frontier)
        numKaway.append(L)
        if (S - i) % 2  == 0:
            ans += L
        
        newf = set()
        for pt in frontier:
            for c in get_valid_neighbors(pt, lines):
                if c not in prevFrontier:
                    newf.add(c)
        prevFrontier = frontier
        frontier = newf
    return ans
        
def getStart(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return (i,j)

def getDiagonals(lines,S,start):
    n, m = len(lines), len(lines[0])
    diags = [(0,m-1), (0,0), (n-1,m-1), (n-1,0)]
    res = 0
    for pt in diags:
        res += diagContribution(start, lines, S, pt)
    return res

def get_valid_neighbors(coord, lines):
    x,y = coord
    orthogonals = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    filtered = []
    for pt in orthogonals:
        if lines[pt[0] % len(lines)][pt[1] % len(lines[0])] in ".S":
            filtered.append(pt)
    return filtered

def distances(lines, pt):
    d = []
    frontier = {pt}
    visited = {pt}
    while len(frontier):
        d.append(len(frontier))
        newf = set()
        for p in frontier:
            for n in valid_neighbors(lines, p):
                if n not in visited:
                    visited.add(n)
                    newf.add(n)
        frontier = newf
    return d


def valid_neighbors(lines, p):
    options = [(p[0], p[1] + 1), (p[0], p[1] - 1), (p[0] - 1, p[1]), (p[0] + 1, p[1])]
    in_bounds = lambda p: 0 <= p[0] < len(lines) and 0 <= p[1] < len(lines[0])
    is_dot = lambda p: lines[p[0]][p[1]] in ".S"
    return list(filter(lambda x: in_bounds(x) and is_dot(x), options))

def sideContribution(start, lines, S, pt):
    n, m = len(lines), len(lines[0])
    w = m if start[0] == pt[0] else n
    d = distances(lines, pt)
    initial = taxicab_d(start, pt, (n,m))
    res = 0
    for b in range((S-initial)//w + 1):
        remaining = S - initial - b*w
        res += reachable(d,remaining)
    return res

def diagContribution(start, lines,S,pt):
    n, m = len(lines), len(lines[0])
    w = n # Assume m = n
    d = distances(lines, pt)
    initial = taxicab_d(start, pt, (n,m))
    res = 0
    for b in range((S-initial)//w + 1):
        remaining = S - initial - b*w
        res += (b+1)*reachable(d,remaining)
    return res


def taxicab_d(origin, p, dim):
    x = (dim[0] - abs(p[0] - origin[0])) % dim[0]
    y = (dim[1] - abs(p[1] - origin[1])) % dim[1]
    return x + y

def reachable(d, remaining):
    res = 0
    for i in range(len(d)):
        if i > remaining: break
        if (remaining - i) % 2 == 0:
            res += d[i]
    return res

t = time.time()
main() 
print("finished in", time.time() - t, "seconds")