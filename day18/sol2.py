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
    vertices = getVertices(lines)
    ans = areaInside(vertices)
    return ans
"""
tested, works
"""
def getVertices(lines):
    n = len(lines)
    vertices = []
    r = [0,0]
    for line in lines:
        vertices.append(r)
        x = line.split()[-1][2:-1]
        d = toDistance(x[:-1])
        v = getVector(x[-1])
        r = [r[0] + d*v[0], r[1]+ d*v[1]]
    return vertices

def toDistance(s):
    print(s)
    hexa = list("0123456789abcdef")
    base = len(hexa)
    d = 0
    for i in range(5):
        d *= base
        d += hexa.index(s[i])
    return d

def getVector(c):
    if c == "0": return [0,1]
    if c == "1": return [1,0]
    if c == "2": return [0,-1]
    if c == "3": return [-1,0]


    return directions, distances, colors
"""
standard cross product method will undercount number of lattice points
by P/2 + 1, where P is the number of lattice points on the edge
"""
def areaInside(vertices):
    n = len(vertices)
    doubleArea = 0
    double_p = 0
    for i in range(n):
        v1 = vertices[i-1]
        v2 = vertices[i]
        diff = [v2[0] - v1[0], v2[1] - v1[1]]
        double_p += length(diff) # double count perimeter correction
        doubleArea += cross(v1,v2)

    print(doubleArea)
    return (abs(doubleArea) + double_p + 2)>>1
"""
assuming v has only one nonzero component
"""
def length(v):
    return abs(sum(v))
"""
[1,0] x [0,1] should give 1 by the RHR
"""
def cross(a,b):
    return a[0]*b[1] - b[0]*a[1]



t = time.time()
main() 
print("finished in", time.time() - t, "seconds")