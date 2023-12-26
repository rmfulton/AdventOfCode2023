class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
    def __repr__(self):
        return self.s + f" {self.left}"+ f" {self.right}"

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
    numSteps = -1
    currentNode = keyToNodeMap["AAA"]
    while True:
        for choice in instructions:
            numSteps += 1
            if currentNode.key == "ZZZ":
                return numSteps
            if choice == "L":
                nextKey = currentNode.left
            else:
                nextKey = currentNode.right
            currentNode = keyToNodeMap[nextKey]
            

main() 