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
    return totalLoad(lines)

def totalLoad(lines):
    N = len(lines)
    M = len(lines[0])
    total = 0
    for i in range(M):
        load = M + 1
        for j in range(N):
            if lines[j][i] == "#":
                load = M - j
            elif lines[j][i] == "O":
                load -= 1
                total += load
    return total


main() 