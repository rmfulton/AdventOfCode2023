import time
def main():
    fname = "./input.txt"
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    f = open(fname)
    lines = [list(line[:-1]) for line in f.readlines()]

    f.close()
    return lines

def answer(lines):
    offset, period = getPeriod(lines)
    num_cycles = 1_000_000_000

    numCyclesAfterOffSet = ((num_cycles - offset) % period)
    totalCycles = offset + numCyclesAfterOffSet
    s = toString(lines)
    n = len(lines)
    for i in range(totalCycles):
        s = cycle(s,n)
    
    return totalLoad(toArr(s,n))




def getPeriod(lines):
    n = len(lines)
    memo = {}
    s = toString(lines)
    count = 0
    while s not in memo:
        memo[s] = count
        s = cycle(s, n)
        count += 1
    period = count - memo[s]
    return memo[s], period


def toString(arr):
    return "".join(["".join(line) for line in arr])
def toArr(s, n):
    m = len(s)//n
    return [[char for char in s[m*i: m*(i+1)]] for i in range(n)]
"""
verified good linear function
"""
def totalLoad(lines):
    N = len(lines)
    M = len(lines[0])
    total = 0
    for i in range(M):
        for j in range(N):
            if lines[j][i] == "O":
                total += N - j
    return total
"""
verified good linear function
"""
def cycle(s,n):
    lines = toArr(s,n)
    lines = shiftUp(lines)
    lines = shiftLeft(lines)
    lines = shiftDown(lines)
    lines = shiftRight(lines)
    return toString(lines)

def shiftUp(lines):
    N = len(lines)
    M = len(lines[0])
    for j in range(M):
        swapQ = []
        for i in range(N):
            if lines[i][j] == ".":
                swapQ.append(i)
            elif lines[i][j] == "#":
                swapQ = []
            elif len(swapQ):
                k = swapQ.pop(0)
                lines[k][j] = "O"
                lines[i][j] = "."
                swapQ.append(i)
    return lines

def shiftLeft(lines):
    f = conjugate(transpose, shiftUp)
    return f(lines)

def shiftDown(lines):
    f = conjugate(hflip, shiftUp)
    return f(lines)

def shiftRight(lines):
    f = conjugate(transpose, shiftDown)
    return f(lines)

def conjugate(f1, f2):
    return lambda x: f1(f2(f1(x)))

def transpose(arr):
    n = len(arr)
    m = len(arr[0])
    return [[arr[i][j] for i in range(n)] for j in range(m)]

def hflip(arr):
    n = len(arr)
    m = len(arr[0])
    return [[arr[i][j] for j in range(m)] for i in range(n-1,-1,-1)]

t = time.time()
main()
print(time.time() - t)