
def main():
    fname = "./input.txt"
    f = open(fname)
    lines = f.readlines()
    f.close()
    res = answer(lines)
    print(res)

def answer(lines):
    m = []
    for line in lines:
        m.append(getMatches(line))
    begottenCards = [0 for _ in m]
    for i in range(len(m) - 1, -1, -1):
        num_matches = m[i]
        begottenCards[i] = 1 + sum(begottenCards[i+1: i+1 + num_matches])
    return sum(begottenCards)


def getMatches(line):
    words = line.split()
    dividerIndex = words.index('|')
    winning = set([int(x) for x in words[2:dividerIndex]])
    have = [int(x) for x in words[dividerIndex+1:]]
    score = 0
    for number in have:
        if number in winning:
            score += 1
    return score

main() 
# testNumbers()