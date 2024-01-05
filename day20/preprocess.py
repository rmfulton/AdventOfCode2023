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
    f = open("gv_input.txt", 'w')
    s = "digraph{ "
    for line in lines:
        s += line[1:] + ";"
    s += '}'
    f.writelines([s])
    f.close()

"""
111100100101 -> 3877
111010111001 -> 3769
111111011001 -> 4057
111100000111 -> 3847
answer: 228060006554227
"""




t = time.time()
main() 
print("finished in", time.time() - t, "seconds")