
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
    s = 0
    for line in lines:
        nums = [int(x) for x in line.split()]
        s += predict(nums)
    return s

def predict(nums):
    current = nums
    lastStack = []
    diff = []
    while current != [0]*len(current):
        lastStack.append(current[-1])
        for i in range(len(current) - 1):
            diff.append(current[i+1] - current[i])
        current = diff
        diff = []
    return sum(lastStack)
    
   

main() 