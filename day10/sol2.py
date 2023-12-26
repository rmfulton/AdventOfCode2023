
def main():
    fname = "./output.txt"
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    f = open(fname)
    lines = [line[:-1] for line in f.readlines()]
    f.close()
    return lines

def answer(lines):
    numEnclosed = 0
    for line in lines:
        isInside = 0
        direction = 0
        for char in line:
            if char == "." and isInside == 1:
                numEnclosed += 1
            elif char == "|":
                isInside = 1 - isInside
            elif char == "-":
                continue
            elif char == "F":
                direction = 1
            elif char == "L":
                direction = -1
            elif char == "7":
                if direction == -1:
                    isInside = 1 - isInside
                direction = 0
            elif char == "J":
                if direction == 1:
                    isInside = 1 - isInside
                direction = 0
    return numEnclosed

main() 