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
    line = lines[0]
    total = 0
    for s in line.split(","):
        total += HASH(s)
    return total

def HASH(s):
    val = 0
    for c in s:
        val = ((val + ord(c))*17) % 256
    return val

t = time.time()
main() 
print(time.time() - t)