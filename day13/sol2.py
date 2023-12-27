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
    N = len(lines)
    total = 0
    grids = []
    g = []
    for i in range(N):
        line = lines[i]
        if line == "":
            grids.append(g)
            g = []
        else:
            g.append(line)
    for grid in grids:
        h = horizontalTest(grid)
        v = verticalTest(grid)
        if h:
            total += h
        else:
            v = verticalTest(grid)
            total += v
    return total

def horizontalTest(g):
    nums = []
    for row in g:
        num = toNum(row)
        nums.append(num)
    ans = reflectionAt(nums)*100

    return ans

def verticalTest(g):
    n = len(g)
    m = len(g[0])
    nums = []
    for i in range(m):
        num = toNum([g[j][i] for j in range(n)])
        nums.append(num)
    ans = reflectionAt(nums)
    return ans

def toNum(r):
    num = 0
    for c in r:
        num = num << 1
        if c == "#":
            num += 1
    return num

def reflectionAt(nums):
    n = len(nums)
    for i in range(n-1):
        numChanges = 0

        w = min(i+1, n - i - 1)
        for j in range(w):
            L = i - j
            R = i + 1 + j
            numChanges += numOnesInBinary(nums[L] ^ nums[R])
        if numChanges == 1:
            return i+1
    return 0

def numOnesInBinary(number):
    count = 0
    while number > 0:
        count += number % 2
        number = number>>1
    return count
main() 