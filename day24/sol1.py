import time
import numpy as np


class Stone:
    def __init__(self,line):
        self.line = line
        commaSeparated = line.split('@')
        xstring = commaSeparated[0].split(',')
        vstring = commaSeparated[1].split(',')
        self.x = [int(x) for x in xstring][:2]
        self.v = [int(v) for v in vstring][:2]
        self.x = np.vstack(np.array(self.x))
        self.v = np.vstack(np.array(self.v))
    """
    determines if the difference in position is a linear combination of the velocities
    """
    def intersects(self, other):
        dx = self.x - other.x
        dependent = lambda a, b: a[0]*b[1] == b[0]*a[1] #and a[0]*b[2] == a[2]*b[0]
        return not(dependent(self.v, other.v)) or dependent(self.v, dx) or dependent(other.v, dx)
        # if dependent(self.v, other.v):
        #     return dependent(dx, self.v) or dependent(dx, other.v)

        # dependent = np.linalg.det(np.hstack([dx, self.v, other.v])) == 0
        # print(self)
        # print(other)
        # print(f"dependent?: {dependent}")
        # print()
        # return dependent

    """
    a + da*s = b + db*t
    a - b = [da, db]*[-s,t]^T
    """
    def intersectsFutureInRegion(self, other, m, M):
        if not self.intersects(other):
            return False

        A = np.hstack([self.v, other.v])
        dx = self.x - other.x

        t = np.linalg.lstsq(A,dx, rcond=None)[0]
        inFuture = t[0] <= 0 and t[1] >= 0
        if not inFuture:
            return False

        intersection = other.x + other.v*t[1]
        inBounds = m <= intersection[0] <= M and m <= intersection[1] <= M
        return inBounds

    def __repr__(self):
        return self.line

def main():
    fname = "./input.txt"
    # fname = './sample.txt'
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    with open(fname) as f:
        lines = [line[:-1] for line in f.readlines()]
    return lines

def answer(lines):
    m = 200_000_000_000_000
    M = 400_000_000_000_000
    # m, M = 7,27
    stones = []
    for line in lines:
        stones.append(Stone(line))

    s = len(stones)
    res = 0
    for i in range(s):
        for j in range(i+1,s):
            res += stones[i].intersectsFutureInRegion(stones[j], m, M)
    return res

t = time.time()
main() 
print("finished in", time.time() - t, "seconds")
