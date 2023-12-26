class Hand:
    def __init__(self, s, bid, ranking):
        self.ranking = ranking
        self.s = s
        self.bid = bid
    def __repr__(self):
        return self.s + f" {self.ranking}"+ f" {self.bid}"

    def rank_string(self, s):
        L = []
        for c in s:
            L.append(getRankOfChar(c))
        return [get_order(s)] + L

def main():
    fname = "./sample.txt"
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    f = open(fname)
    lines = [line[:-1] for line in f.readlines()]
    f.close()
    return lines

def answer(lines):
    a = getHands(lines)
    a.sort(key=lambda x: x.ranking)
    total = 0
    for i in range(len(a)):
        total += (i+1)*a[i].bid
    return total

def getHands(lines):
    hands = []
    for line in lines:
        handbid = line.split()
        ranking = getRanking(handbid[0])
        h = Hand(handbid[0], int(handbid[1]), ranking)
        hands.append(h)
    return hands

def getRanking(s):
    withoutJacksD = replaceJacksOptimally(s)
    ranking = []
    ranking.append(getKind(withoutJacksD))
    for c in s:
        ranking.append(getRankOfChar(c))
    return ranking

def replaceJacksOptimally(s):
    D = getCounts(s)
    num_jacks = numJacks(s)
    if num_jacks == 0:
        return D
    elif num_jacks == 5:
        return {'A':5}
    else:
        bestKey = findBestMode(D)
        D[bestKey] += num_jacks
        return D

def findBestMode(D):
    modes = []
    bestCount = 0
    for key in D:
        if D[key] == bestCount:
            modes.append(key)
        elif D[key] > bestCount:
            bestCount = D[key]
            modes = [key]
    modes.sort(key=getRankOfChar,reverse=True)
    return modes[0]
    

def getCounts(s):
    D = {}
    for c in s:
        if c != "J":
            if c not in D:
                D[c] = 0
            D[c] += 1
    return D

def numJacks(s):
    j = "J"
    count = 0
    for c in s:
        count += c == j
    return count

def getRankOfChar(c):
    rank = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    return rank.index(c)

def getKind(D):
    if len(D) == 1: # must be 5 of a kind
        return 7
    elif 4 in D.values(): # must be 4 of a kind
        return 6
    elif len(D) == 2: # must be full house
        return 5
    elif 3 in D.values(): # must be trips
        return 4
    elif len(D) == 3: # must be 2-pair
        return 3
    elif len(D) == 4: # must be pair
        return 2
    else: # must be high card
        return 1

main() 