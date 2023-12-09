
def main():
    fname = "./input.txt"
    f = open(fname)
    lines = [line[:-1] for line in f.readlines()]
    f.close()
    res = answer(lines)
    print(res)

def answer(lines):
    numbers = getGoodNumbers(lines)

    return sum(numbers)

def getGoodNumbers(lines):
    n = len(lines)
    numbers = []
    for i in range(n):
        numbers += getGoodNumbersInLine(i, lines)
    return numbers

def getGoodNumbersInLine(i, lines):
    numbers = []
    m = len(lines[i])
    s = ""
    digits = "0123456789"
    for j in range(m):
        if lines[i][j] in digits:
            s = s + lines[i][j]
        elif len(s):
            row = i
            columns = [j - len(s), j-1]
            isPart = determineIfPart(row, columns, lines)
            if isPart:
                numbers.append(int(s))
            s = ""
    if len(s):
        row = i
        columns = [m - len(s), m-1]
        isPart = determineIfPart(row, columns, lines)
        if isPart:
            numbers.append(int(s))
        s = ""
    return numbers

def determineIfPart(row, columns, lines):
    n = len(lines)
    m = len(lines[0])
    p = getPerimeter(row, columns, n, m)
    for i, j in p:
        if lines[i][j] not in ".":
            return True
    return False

def getPerimeter(row, columns, n, m):
    over = [(row - 1, j) for j in range(columns[0] - 1, columns[1]+2)]
    under = [(row +1, j) for j in range(columns[0] - 1, columns[1]+2)]
    left = [(row, columns[0] - 1)]
    right = [(row, columns[1] + 1)]
    total = over + under + left + right

    return list(filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < m, total))





main() 
# testNumbers()