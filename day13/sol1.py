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
        n = numArrangements(record, stats)
        total += n
    return total

main() 