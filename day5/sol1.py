def main():
    fname = "./test1.txt"
    f = open(fname)
    lines = [line[:-1] for line in f.readlines()]
    f.close()
    res = answer(lines)
    print(res)

def answer(lines):
    seeds = getSeeds(lines[0])
    maps = getMaps(lines[2:])
    smallest_location = 9999999999999999999999999
    for seed in seeds:
        source = seed
        for m in maps:
            dest = m(source)
            source = dest
        # print(source)
        if source < smallest_location:
            smallest_location = source
            # print(seed)
    return smallest_location
        


def getSeeds(line):
    numbers = line.split()[1:]
    return [int(x) for x in numbers]

def getMaps(lines):
    N = len(lines)
    maps = []
    el = []
    for i in range(N):
        s = lines[i]
        if s == "":
            m = makeMap(el)
            maps.append(m)
            el = []
        elif s.split()[-1] == "map:":
            continue
        else:
            el.append(s)
    m = makeMap(el)
    maps.append(m)
    return maps

def makeMap(numbers):
    numbers = [[int(x) for x in el.split()] for el in numbers]
    def retFunction(k):
        for el in numbers:
            sourceStart = el[1]
            destStart = el[0]
            d = el[2]
            if sourceStart <= k < sourceStart + d:
                return destStart + k - sourceStart
        return k
    return retFunction

main() 