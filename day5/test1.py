from sol1 import getSeeds, getMaps

def testGetSeeds():
    s = "seeds: 1 3 4 9 12 7"
    x = getSeeds(s)
    expect = [1,3,4,9,12,7]
    return x == expect


print("testGetSeeds: " +  "passed" if testGetSeeds() else "failed")