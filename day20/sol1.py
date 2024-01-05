import time

class Broadcast:
    def pulse(self, bit, origin):
        return 0

class FlipFlop:
    def __init__(self):
        self.state = 0
    def pulse(self, bit, origin):
        if bit == 0:
            self.state = 1 - self.state
            return self.state
    
class Conjunction:
    def __init__(self, sources):
        self.state = {source: 0 for source in sources}
        self.numOnes = 0
        self.length = len(sources)
    def pulse(self, bit, origin):
        self.numOnes += bit - self.state[origin]
        self.state[origin] = bit
        return self.numOnes < self.length

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
    adj = get_adjacencies(lines)
    key2node = get_broadcast()
    flipflops = get_flip_flops(lines)
    conjunctions = get_conjunctions(lines, adj)
    for key in flipflops:
        key2node[key] = flipflops[key]
    for key in conjunctions:
        key2node[key] = conjunctions[key]
    lp = 0
    hp = 0
    for _ in range(1000):
        lp += 1
        nodeQ = [("button", 0, "broadcaster")]
        while len(nodeQ):
            front = nodeQ.pop(0)
            newSourceKey = front[2]
            oldPulseVal = front[1]
            newPulseVal = key2node[newSourceKey].pulse(oldPulseVal, front[0])
            if newPulseVal == None:
                continue
            for newDestKey in adj[newSourceKey]:
                if newDestKey in adj:
                    nodeQ.append((newSourceKey, newPulseVal, newDestKey))
                if newPulseVal: hp += 1
                else: lp += 1
    return lp*hp

def get_adjacencies(lines):
    d = {}
    for line in lines:
        x = line.split('->')
        left, right = x
        if "%" in left or "&" in left:
            start = left[1:-1]
        else:
            start = left[:-1]
        res = [s[1:] for s in right.split(',')]
        d[start] = res
    return d

def get_broadcast():
    return {"broadcaster": Broadcast()}

def get_flip_flops(lines):
    d = {}
    for line in lines:
        x = line.split('->')
        left, right = x
        if "%" in left:
            start = left[1:-1]
            res = FlipFlop()
            d[start] = res
    return d

def get_conjunctions(lines, adj):
    conjunctionKeys = {}
    for line in lines:
        x = line.split('->')
        left, right = x
        if "&" in left:
            start = left[1:-1]
            conjunctionKeys[start] = []
    for key in adj:
        for resKey in adj[key]:
            if resKey in conjunctionKeys:
                conjunctionKeys[resKey].append(key)
    for key in conjunctionKeys:
        val = conjunctionKeys[key]
        conjunctionKeys[key] = Conjunction(val)
    return conjunctionKeys




t = time.time()
main() 
print("finished in", time.time() - t, "seconds")