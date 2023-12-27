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
"""
    O(N*2**Q) where N is length of record and Q is number of unknowns
"""
def numArrangements(record, stats):
    numQs = 0
    qindices = []
    ans = 0
    for i in range(len(record)):
        c = record[i]
        if c == "?":
            numQs += 1
            qindices.append(i)
    for v in range(1<<numQs):
        rec = ""
        qshit = 0
        for c in record:
            if c == "?":
                rec += "#" if (v>>qshit)%2 else "."
                qshit += 1
            else:
                rec += c
        ans += satisfies(rec, stats)
    # print(1<<numQs)
    return ans


"""
O(N) where N is length of record
"""
def satisfies(record, stats):
    N = len(record)
    observed = []
    l = 0
    for i in range(N):
        if record[i] == "#":
            l += 1
        elif l:
            observed.append(l)
            l = 0
    if l:
        observed.append(l)
    return observed == stats


main() 