from functools import reduce
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
    def __repr__(self):
        return self.key + " " + self.left + " " + self.right

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
    instructions = lines[0]
    print(len(instructions))
    keyToNodeMap = constructGraph(lines[2:])
    steps = traverse(instructions, keyToNodeMap)
    return steps

def constructGraph(nodeData):
    keyToNodeMap = {}
    for line in nodeData:
        split = line.split()
        key = split[0]
        left = split[2][1:4]
        right = split[3][:-1]
        n = Node(key, left, right)
        keyToNodeMap[key] = n
    return keyToNodeMap

def traverse(instructions, keyToNodeMap):
    initialNodes = getAllNodesThatEndWithA(keyToNodeMap)
    # data = [node.key: None for node in initialNodes]
    for node in initialNodes:
        printCycleInfo(node, instructions, keyToNodeMap)
        
def printCycleInfo(node, instructions, keyToNodeMap):
    numSteps = -1
    currentNode = node
    visited = {} # (instructions, key ending with Z) -> numSteps
    coords = None
    while coords == None:
        for i in range(len(instructions)):
            numSteps += 1
            if (i, currentNode.key) in visited:
                coords = (i,currentNode.key)
                break
            if currentNode.key[-1] == "Z":
                visited[(i,currentNode.key)] = numSteps
            choice = instructions[i]
            nextKey = currentNode.left if choice == "L" else currentNode.right
            currentNode = keyToNodeMap[nextKey]
    loopEntryPoint = visited[coords]
    period = numSteps - loopEntryPoint
    print(f"key: {node.key}, entryPoint: {loopEntryPoint}, period: {period}, coord: {coords}")

      
def getAllNodesThatEndWithA(keyToNodeMap):
    nodes = []
    for k in keyToNodeMap.keys():
        if k[-1] == "A":
            nodes.append(keyToNodeMap[k])
    print(len(nodes))
    return nodes

def lcm(arr):
    factorizations = [factorization(num) for num in arr]
    lcmFactors = {}
    allKeys = set(reduce(lambda x,y: x + y, [list(f.keys()) for f in factorizations]))
    for key in allKeys:
        lcmFactors[key] = 1
        for f in factorizations:
            if key in f:
                lcmFactors[key] = max(lcmFactors[key], f[key])
    multiple = 1
    for key in lcmFactors:
        val = lcmFactors[key]
        for _ in range(val):
            multiple *= key
    return multiple

def factorization(n):
    factors = {}
    x = n
    k = 1
    while x > k**2:
        k += 1
        while x % k == 0:
            if k not in factors:
                factors[k] = 0
            factors[k] += 1
            x = x//k
    if x > 1:
        factors[x] = 1
    return factors
main()

print(lcm([21883, 19667, 14681, 16897, 13019, 11911]))
# lcm = 10151663816849