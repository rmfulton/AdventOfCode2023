

def main():
    fname = "./input.txt"
    f = open(fname)
    lines = f.readlines()
    f.close()
    print(answer(lines))

def answer(lines):
    s = 0
    for i in range(len(lines)):
        if possible(lines[i]):
            s += i + 1
            print(i+1)
    return s

def possible(line):
    rgb = [12, 13, 14]
    games = "".join(line.split()[2:]).split(';')
    for game in games:
        sample = [0,0,0]
        values = game.split(",")
        for val in values:
            if 'd' in val:
                sample[0] = int(val[0:val.index('r')])
            elif 'g' in val:
                sample[1] = int(val[0:val.index('g')])
            else:
                sample[2] = int(val[0:val.index('b')])
        if sample[0] > 12 or sample[1] > 13 or sample[2] > 14:
            return False
    return True



main()