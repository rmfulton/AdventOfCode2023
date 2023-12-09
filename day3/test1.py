from sol1 import getPerimeter

def testGetPerimeter():
    row = 1
    cols = [1,1]
    actual = [tuple(el) for el in getPerimeter(row,cols,3,3)]
    expected = [ (i,j) for i in range(3) for j in range(3)]
    expected.remove((1,1))
    print(set(expected) == set(actual))

testGetPerimeter()