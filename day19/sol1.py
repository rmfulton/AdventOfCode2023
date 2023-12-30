import time

class Object:
    def __init__(self, s):
        elements = s.split(',')
        self.x = int(elements[0][3:])
        self.m = int(elements[1][2:])
        self.a = int(elements[2][2:])
        self.s = int(elements[3][2:-1])
    def ratingSum(self):
        return self.x + self.m + self.a + self.s
    def __repr__(self):
        return str(self.x) + " " + str(self.m) + " " + str(self.a) + " " + str(self.s)


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
    workflows = getWorkflows(lines) # map of name to function
    objects = getObjects(lines)
    res = 0
    for o in objects:
        accepted = getAcceptance(o, workflows)
        if accepted:
            ratingSum = o.ratingSum()
            res += ratingSum
    return res

def getAcceptance(o, workflows):
    res = "in"
    while res not in "RA":
        res = workflows[res](o)
    return True if res == "A" else False

def getObjects(lines):
    i = 0
    while len(lines[i]):
        i += 1
    i += 1
    objects = []
    while i < len(lines):
        o = Object(lines[i])
        objects.append(o)
        i += 1
    return objects

def getWorkflows(lines):
    i = 0
    workflows = {}
    while lines[i] != "":
        key, val = wf(lines[i])
        workflows[key] = val
        i += 1
    return workflows

"""
returns a key and a value
"""
def wf(line):
    name = line[:line.index("{")]
    sequence = line[line.index("{") + 1: line.index("}")]
    instructions = sequence.split(",")
    L = len(instructions)
    def res(o):
        for j in range(L-1):
            conditional, consequence = instructions[j].split(":")
            if eval("o." + conditional):
                return consequence
        return instructions[-1]
    return name, res





t = time.time()
main() 
print("finished in", time.time() - t, "seconds")