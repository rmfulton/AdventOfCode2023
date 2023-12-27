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
    T = [int(time) for time in lines[0].split()[1:]]
    D = [int(d) for d in lines[1].split()[1:]]
    prod = 1
    for i in range(len(T)):
        prod *= numWays(T[i], D[i])
    return prod
"""
If I wait w milliseconds, and then travel at w millimeters / ms for t milliseconds,
then I will travel w*t. 
"""
def numWays(t, d):
    count = 0
    for i in range(t+1):
        if (t-i)*i > d:
            count += 1
    return count

main() 