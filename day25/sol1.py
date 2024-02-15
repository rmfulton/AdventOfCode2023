import time
import numpy as np

class Node:
    def __init__(self, name):
        self.name = name
        self.adj = set()

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def addNode(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        
    def addEdge(self, name1, name2):
        self.addNode(name1)
        self.addNode(name2)
        self.nodes[name1].adj.add(name2)
        self.nodes[name2].adj.add(name1)
        self.edges.append((name1, name2))
    
    def cutEdge(self, name1, name2):
        self.nodes[name1].adj.remove(name2)
        self.nodes[name2].adj.remove(name1)
    
    def restoreEdge(self, name1, name2):
        self.nodes[name1].adj.add(name2)
        self.nodes[name2].adj.add(name1)

    def cutEdges(self, edges):
        for e in edges:
            self.cutEdge(e[0], e[1])
    
    def restoreEdges(self, edges):
        for e in edges:
            self.restoreEdge(e[0], e[1])

    def componentSize(self):
        init = list(self.nodes.values())[0]
        visited = set([init.name])
        stack = [init]
        while len(stack):
            top = stack.pop(0)
            for k in top.adj:
                if k in visited:
                    continue
                else:
                    visited.add(k)
                    stack.append(self.nodes[k])
        return len(self.nodes) - len(visited)

    def shortestPath(self, a, b):
        init = self.nodes[a]
        visited = {}
        queue = [init]
        while len(queue):
            top = queue.pop(0)
            for k in top.adj:
                if k in visited:
                    continue
                else:
                    visited[k] = top.name
                    queue.append(self.nodes[k])
        if b not in visited:
            return -1
        else:
            edges = []
            v = b
            while v != a:
                edges.append( (v,visited[v]) )
                v = visited[v]
            return edges

    def tightlyConnected(self, a, b):
        edgesRemoved = []
        for i in range(4):
            p = self.shortestPath(a,b)
            if p == -1:
                self.restoreEdges(edgesRemoved)
                return False
            edgesRemoved += p
            self.cutEdges(p)
        self.restoreEdges(edgesRemoved)
        return True

    def __repr__(self):
        s = ""
        for n in self.nodes:
            for m in self.nodes:
                if n == m:
                    s += '1'
                elif (n,m) in self.edges:
                    s += '1'
                else:
                    s += '0'
            s += '\n'
        return s

def main():
    fname = "./input.txt"
    # fname = './sample.txt'
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    with open(fname) as f:
        lines = [line[:-1] for line in f.readlines()]
    return lines

def answer(lines):
    g, k = makeGraph(lines)
    ans = findComponent(g,k)
    # ans = brute_force(g)
    return ans

def makeGraph(lines):
    g = Graph()
    for line in lines:
        left, right = line.split(':')
        right = right.split()
        for r in right:
            g.addEdge(left, r)
    return g, left


"""
There are 15 nodes and 33 edges in the sample input, and 
1_568 nodes and 3_503 edges in the actual input.

There are 5_456 ways to choose 3 edges in the sample input, and 
7_158_089_751 ways to choose 3 edges in the actual input. That's too big.

IDEAS:
- for arbitrary nodes a,b in the graph,
- attempt to find 4 mutually edge-disjoint paths between them.
- If successful, then these two nodes MUST be part of the same component
- in any tri-cut graph.
    - Pf: If each of the four independent paths are severed, then
    - there must have been at least four cuts

- conjecture: If unsuccessful, then there must exist a tri-cut which
- separates these two nodes.
    - Pf: ...

- Regardless, if we find that there are only two cliques
- then our answer must be the product of the sizes, without relying
- on the conjecture, but rather only upon assumptions about the input.

RUNTIME: O( N*4(N+E) )
"""
def brute_force(g):
    t = time.time()
    for i in range(len(g.edges)):
        for j in range(i+1, len(g.edges)):
            for k in range(j+1, len(g.edges)):
                for l in [i,j,k]:
                    n1 = g.edges[l][0]
                    n2 = g.edges[l][1]
                    g.cutEdge(n1, n2)
                s = g.componentSize()
                if s != 0:
                    return s*( len(g.nodes) - s )
                else:
                    for l in [i,j,k]:
                        n1 = g.edges[l][0]
                        n2 = g.edges[l][1]
                        g.restoreEdge(n1, n2)
    return "Error"

def findComponent(g, name):
    inGroupA = [name]
    x = None
    for key in g.nodes:
        if key == name:
            continue
        if g.tightlyConnected(name, key):
            inGroupA.append(key)
        else:
            x = key
    inGroupB = [x]
    overlap = []
    outGroup = []
    for key in g.nodes:
        if key == x:
            continue
        if g.tightlyConnected(x,key):
            inGroupB.append(key)
            if key in inGroupA:
                overlap.append(key)
        elif key not in inGroupA:
            outGroup.append(key)

    print(f"intersection: {len(overlap)}, cliqueA size: {len(inGroupA)}, cliqueB size: {len(inGroupB)}, leftover: {len(outGroup)}, total: {len(g.nodes)}")

    print(len(inGroupA))
    return len(inGroupA)*len(inGroupB)

"""
Pf of conjecture for one cut:
If we cannot find two independent paths, 
then any two paths must merge at a single edge. 
Suppose every two paths merge at at least one single edge. 
Let p1, p2 merge at only one edge e.
Then we could cut this edge to separate the points, unless
There were a third path p3 which did not traverse this edge,
but rather intersects... Never mind, I solved the problem, didn't I?

"""






t = time.time()
main() 
print("finished in", time.time() - t, "seconds")
