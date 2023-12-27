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
    for i in range(N):
        line = lines[i]
        divide = line.split()
        record = divide[0]
        stats = [int(el) for el in divide[1].split(',')]
        numArrangements(record, stats)
    return total
"""
    O(N*2**Q) where N is length of record and Q is number of unknowns
"""
def numArrangements(record, stats):
    a = len(record)
    b = sum([c == "?" for c in record])
    print(a,b, 2**(3*b))

def choose(n,k):
    x = n
    res = 1
    for i in range(k):
        res *= n-i
    for i in range(1,k+1):
        res = res//i
    return res
print(choose(60,15))
main() 