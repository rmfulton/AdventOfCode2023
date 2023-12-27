

def main():
    fname = "./input.txt"
    f = open(fname)
    lines = f.readlines()
    f.close()
    print(answer(lines))

def answer(lines):
    s = 0
    for i in range(len(lines)):
        s += power(lines[i])
    return s

def power(line):
    rgb = [0, 0, 0]
    games = "".join(line.split()[2:]).split(';')
    for game in games:
        sample = [0,0,0]
        values = game.split(",")
        for val in values:
            if 'd' in val:
                rgb[0] = max(rgb[0], int(val[0:val.index('r')]))
            elif 'g' in val:
                rgb[1] = max(rgb[1], int(val[0:val.index('g')]))
            else:
                rgb[2] = max(rgb[2], int(val[0:val.index('b')]))
    power = rgb[0]*rgb[1]*rgb[2]
    print(power)
    return power



main()