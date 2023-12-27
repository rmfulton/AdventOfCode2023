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
        record, stats = unfoldLine(line)
        n = recursive(record, stats)
        print(n)
        total += n
    return total

def unfoldLine(line):
    MULTIPLIER = 5
    divide = line.split()
    foldedRecord = divide[0]
    record = (foldedRecord + '?')*MULTIPLIER
    record = record[:-1]

    stats = [int(el) for el in divide[1].split(',')]*MULTIPLIER
    return record, stats
"""
    naively assume that we're working with all ? marks until we
    run into a wall.
"""
memo = {}
def recursive(record, stats):
    if (record, tuple(stats)) in memo:
        return memo[(record, tuple(stats))]
    if stats == []:
        res = int( "#" not in record )
        memo[(record, tuple(stats))] = res
        return res
    firstStatSize = stats[0]
    naiveLastStart = len(record) - sum(stats) - len(stats) + 1 # Assumes all ?
    totalNumber = 0
    for start in range(naiveLastStart+1):
        if "." not in record[start:start+stats[0]]:
            if len(stats) == 1:
                remainingRecord = record[start+stats[0]:]
                remainingStats = stats[1:] 
                totalNumber += recursive(remainingRecord, remainingStats)
            elif record[start + stats[0]] in ".?":
                remainingRecord = record[start+stats[0]+1:]
                remainingStats = stats[1:]
                totalNumber += recursive(remainingRecord, remainingStats)

        if record[start] == "#":
            break
    memo[(record, tuple(stats))] = totalNumber
    return totalNumber

main() 