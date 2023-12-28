import time
class Lens:
    def __init__(self, label, fl):
        self.label = label
        self.fl = fl
class Box:
    def __init__(self, boxNumber):
        self.lensQ = []
        self.qsize = 0
        self.boxNumber = boxNumber
        self.labels = set()
    
    def add(self, newLens):
        if newLens.label in self.labels:
            for i in range(self.qsize):
                if self.lensQ[i].label == newLens.label:
                    self.lensQ[i] = newLens
        else:
            self.lensQ.append(newLens)
            self.qsize += 1
            self.labels.add(newLens.label)
    
    def remove(self, label):
        if label in self.labels:
            for i in range(self.qsize):
                if self.lensQ[i].label == label:
                    self.lensQ.pop(i)
                    break
            self.qsize -= 1
            self.labels.remove(label)


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
    line = lines[0]
    boxes = [Box(i) for i in range(256)]
    # O(N^2) operation, could probably be made into linear
    for instruction in line.split(","):
        if "=" in instruction:
            label = instruction[:-2]
            fl = int(instruction[-1])
            L = Lens(label, fl)
            h = HASH(label)
            boxes[h].add(L)
        else:
            label = instruction[:-1]
            h = HASH(label)
            boxes[h].remove(label)
    power = getPower(boxes)
    return power

def HASH(s):
    val = 0
    for c in s:
        val = ((val + ord(c))*17) % 256
    return val

def getPower(boxes):
    p = 0
    for box in boxes:
        for i in range(box.qsize):
            lens = box.lensQ[i]
            fp = (box.boxNumber + 1)*(i+1)*lens.fl
            p += fp
            print(lens.label, box.boxNumber, i, lens.fl, fp)
    return p

t = time.time()
main() 
print(time.time() - t)