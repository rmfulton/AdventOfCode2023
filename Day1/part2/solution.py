

def main():
    fname = "../input.txt"
    f = open(fname)
    lines = f.readlines()
    f.close()
    return getSum(lines)

def getSum(lines):
    s = 0
    for line in lines:
        first = getFirst(line)
        last = getLast(line)
        s += 10*first + last
    print(s)


def getFirst(line):
    numbers = "0123456789"
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for i in range(len(line)):
        for j in range(10):
            if line[i] == numbers[j]:
                return j
            L = len(words[j])
            if i + L <= len(line) and line[i:i+L] == words[j]:
                return j
    return -1

def getLast(line):
    numbers = "0123456789"
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for i in range(len(line)-1,-1,-1):
        for j in range(10):
            if line[i] == numbers[j]:
                return j
            L = len(words[j])
            if i + L <= len(line) and line[i:i+L] == words[j]:
                return j
    return -1


main()