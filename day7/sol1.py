class Hand:
    def __init__(self, s, bid):
        self.order = self.rank_string(s)
        self.s = s
        self.bid = bid
    def __repr__(self):
        return self.s + f" {self.order}"+ f" {self.bid}"
    
    def get_order(self, s):
        D = {}
        for char in s:
            if char not in D:
                D[char] = 0
            D[char] += 1
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

    def rank_string(self, s):
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        L = []
        for char in s:
            L.append(rank.index(char))
        return [self.get_order(s)] + L


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
    a = getHands(lines)
    a.sort(key=lambda x: x.order)
    total = 0
    for i in range(len(a)):
        total += (i+1)*a[i].bid
    return total


def getHands(lines):
    a = []
    for line in lines:
        arr = line.split()
        h = Hand(arr[0], int(arr[1]))
        a.append(h)
    return a


main() 