
def main():
    fname = "./input.txt"
    f = open(fname)
    lines = f.readlines()
    f.close()
    res = answer(lines)
    print(res)

def answer(lines):
    totalWorth = 0
    for line in lines:
        totalWorth += getWorth(line)
    return totalWorth

def getWorth(line):
    words = line.split()
    dividerIndex = words.index('|')
    winning = set([int(x) for x in words[2:dividerIndex]])
    have = [int(x) for x in words[dividerIndex+1:]]
    score = 0
    for number in have:
        if number in winning:
            score = max(2*score, 1)
    return score

main() 
# testNumbers()