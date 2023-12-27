from sol2 import Interval, Map, getSeeds, fillGaps

def testGetSeeds1():
    s = "seeds: 79 14 55 13"
    m = getSeeds(s)
    print(s)
    print([(x.sourceStart, x.destStart, x.length) for x in m.intervals])

def testGetSeeds2():
    s = "seeds: 364807853 408612163 302918330 20208251 1499552892 200291842 3284226943 16030044 2593569946 345762334 3692780593 17215731 1207118682 189983080 2231594291 72205975 3817565407 443061598 2313976854 203929368"
    m = getSeeds(s)
    print(s)
    for x in m.intervals:
        print((x.sourceStart, x.destStart, x.length))

def testCompose():
    interval1 = Interval(0,100,300)
    interval2 = Interval(304, 2, 50)
    m = Map(fillGaps([interval1, interval2]))
    m2 = Map([Interval(0,0, 1000)])
    m3 = m.compose(m2)
    m4 = m2.compose(m)
    print(m4)


testCompose()