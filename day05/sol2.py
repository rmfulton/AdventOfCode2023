class Interval:
    def __init__(self, sourceStart, destStart, length):
        self.sourceStart = sourceStart
        self.destStart = destStart
        self.length = length
    def __repr__(self):
        return f"({self.sourceStart} {self.destStart} {self.length})"

class Map:
    def __init__(self, intervals):
        self.intervals = sorted(intervals, key=lambda x: x.sourceStart)

    def compose(self, other):
        intervals = []
        for chunk in self.intervals:
            domainStart = chunk.sourceStart
            intermediate = chunk.destStart
            L = chunk.length
            for afterchunk in other.intervals:
                if intermediate < afterchunk.sourceStart:
                    d = afterchunk.sourceStart - intermediate
                    if d < L:
                        ni = Interval(domainStart, intermediate, d)
                        intervals.append(ni)
                        domainStart += d
                        intermediate += d
                        L -= d
                    else:
                        intervals.append(Interval(domainStart, intermediate, L))
                        L = 0
                        break
                if intermediate >= afterchunk.sourceStart + afterchunk.length:
                    continue
                else:
                    x = intermediate - afterchunk.sourceStart
                    y = afterchunk.length - x
                    if y < L:
                        ni = Interval(domainStart, afterchunk.destStart + x, y)
                        intervals.append(ni)
                        domainStart += y
                        intermediate += y
                        L -= y
                    else:
                        intervals.append(Interval(domainStart, afterchunk.destStart + x, L))
                        L = 0
                        break
            if L:
                ni = Interval(domainStart, intermediate, L)
                intervals.append(ni)

        return Map(intervals)

    def __repr__(self):
        return "".join([str(interval) + "\n" for interval in self.intervals])

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
    seeds = getSeeds(lines[0])
    maps = getMaps(lines[2:])
    for m in maps:
        seeds = seeds.compose(m)
    return min([interv.destStart for interv in seeds.intervals])


def getSeeds(line):
    numbersAsStrings = line.split()[1:]
    numbers = [int(x) for x in numbersAsStrings] 
    intervals = []
    for i in range(0,len(numbers), 2):
        I = Interval(numbers[i], numbers[i], numbers[i+1])
        intervals.append(I)
    return Map(intervals)


def getMaps(lines):
    N = len(lines)
    maps = []
    intervals = []
    for i in range(N):
        s = lines[i]
        if s == "":
            m = Map(fillGaps(intervals))
            maps.append(m)
            intervals = []
        elif s.split()[-1] == "map:":
            continue
        else:
            asNums = [int(x) for x in s.split()]
            newInt = Interval(asNums[1], asNums[0], asNums[2])
            intervals.append(newInt)
    return maps

def fillGaps(intervals):
    keyFunction = lambda interval: interval.sourceStart
    intervals = sorted(intervals, key=keyFunction)
    fillers = []
    for i in range(len(intervals) - 1):
        left = intervals[i]
        right = intervals[i+1]
        fillers.append(left)
        leftEnd = left.sourceStart + left.length
        if leftEnd < right.sourceStart:
            newInt = Interval(leftEnd, leftEnd, right.sourceStart - leftEnd)
            fillers.append(newInt)
    fillers.append(intervals[-1])
    return fillers

main() 