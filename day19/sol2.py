import time

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
    functions = getFunctions(lines)
    q = [('in', [(1, 4001) for _ in range(4)])]
    s = 0
    while len(q):
        key, r = q.pop(0)
        if value(r) == 0:
            continue
        if key == 'A':
            s += value(r)
            continue
        if key == 'R':
            continue
        f = functions[key]
        orders = getOrders(f,r)
        q += orders
    return s

def value(r):
    v = 1
    for span in r:
        v *= max(0, span[1] - span[0])
    return v

def getOrders(f,r):
    xmas = list('xmas')
    orders = []
    for branch in f:
        if ':' not in branch:
            orders.append((branch, r))
            return orders
        dim = xmas.index(branch[0])
        key = branch[branch.index(':') + 1:]
        num = branch[2:branch.index(':')]
        num = int(num)
        lower = r[dim][0]
        upper = r[dim][1]
        if branch[1] == '<':
            inrange = [lower, num]
            outrange = [num, upper]
        else:
            outrange = [lower, num+1]
            inrange = [num+1, upper]
        cut = [inrange if i == dim else r[i] for i in range(4)]
        orders.append((key, cut))
        r = [outrange if i == dim else r[i] for i in range(4)]
    return orders

def getFunctions(lines):
    d = {}
    for line in lines:
        if line == "": break
        k = line[:line.index('{')]
        rest = line[line.index('{')+1:-1]
        d[k] = rest.split(',')
    return d




t = time.time()
main() 
print("finished in", time.time() - t, "seconds")