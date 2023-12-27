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
    T = int("".join(lines[0].split()[1:]))
    D = int("".join(lines[1].split()[1:]))
    return numWays(T,D)
"""
If I wait w milliseconds, and then travel at w millimeters / ms for t milliseconds,
then I will travel w*t. 
"""
def numWays(t, d):
    count = 0
    print(t)
    for i in range(t+1):
        if i % 10000000 == 0:
            print(i)
        if (t-i)*i > d:
            count += 1
        # else:
        #     if count:
        #         break
    return count

main() 