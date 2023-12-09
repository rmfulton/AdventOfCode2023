class Number:
    def __init__(self, val, row, columns):
        self.val = val
        self.row = row
        self.columns = columns
    
    def __eq__(self, other):
        return type(other) == Number and self.val == other.val and self.row == other.row and self.columns == other.columns
 

def main():
    fname = "./input.txt"
    f = open(fname)
    lines = [[element for element in line[:-1]] for line in f.readlines()]
    f.close()
    res = answer(lines)
    print(res)

def answer(lines):
    numbers = getNumbers(lines)
    ratios = getGearRatios(lines)
    return sum(ratios)
        

def getNumbers(lines):
    n = len(lines)
    numbers = []
    for i in range(n):
        numbers += getNumbersInLine(i, lines)
    return numbers

def getNumbersInLine(i, lines):
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
            number = Number(int(s), row, columns)
            numbers.append(number)
            for k in range(columns[0], columns[1]+1):
                lines[i][k] = number
            s = ""
    if len(s):
        row = i
        columns = [m - len(s), m-1]
        number = Number(int(s), row, columns)
        numbers.append(number)
        for k in range(columns[0], columns[1] + 1):
            lines[i][k] = number
        s = ""
    return numbers

def getGearRatios(lines):
    n = len(lines)
    ratios = []
    for i in range(n):
        m = len(lines[i])
        for j in range(m):
            isStar = lines[i][j] == "*"
            if isStar:
                isGear = adjacentToTwoNumbers(lines,i,j)
                if isGear:
                    ratios.append(isGear[0]*isGear[1])
    return ratios

def adjacentToTwoNumbers(lines,i,j):
    p = getPerimeter(i,[j,j], len(lines), len(lines[i]))
    numbers = []
    for a,b in p:
        if type(lines[a][b]) == Number:
            if lines[a][b] not in numbers:
                numbers.append(lines[a][b])
    if len(numbers) == 2:
        return list(map(lambda x: x.val, numbers))
    else:
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