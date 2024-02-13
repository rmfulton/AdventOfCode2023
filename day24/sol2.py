import time


def main():
    fname = "./input.txt"
    # fname = './sample.txt'
    lines = getLines(fname)
    res = answer(lines)
    print(res)

def getLines(fname):
    with open(fname) as f:
        lines = [line[:-1] for line in f.readlines()]
    return lines
"""
with algebraic manipulations, you can reduce it to the following equations:
      [ (vzi - vzk)B - (vzj - vzk)A ][ (xj-xk)A - (xi-xk)B + (vxj-vxi)AB ] 
    = [ (vxi - vxk)B - (vxj - vxk)A ][ (zj-zk)A - (zi-zk)B + (vzj-vzi)AB ],
      [ (vzi - vzk)B - (vzj - vzk)A ][ (yj-yk)A - (yi-yk)B + (vyj-vyi)AB ] 
    = [ (vyi - vyk)B - (vyj - vyk)A ][ (zj-zk)A - (zi-zk)B + (vzj-vzi)AB ],

"""
def answer(lines):
    positions = []
    velocities = []
    for line in lines:
        pv = line.split('@')
        p = pv[0].split(',')
        p = [int(x) for x in p]
        v = pv[1].split(',')
        v = [int(x) for x in v]
        positions.append(p)
        velocities.append(v)
    # printEquations(positions, velocities)
    # From these equations, Wolfram Alpha gives us 
    # A = -264154475682, B = -717113827110
    # as the only integer solutions aside from (0,0). 
    t1, t2, t3 = getTimes(-264154475682, -717113827110, positions, velocities)
    return getAnswer(int(t1), int(t2), positions, velocities)

def printEquations(positions, velocities):
    x = [p[0] for p in positions]
    y = [p[1] for p in positions]
    z = [p[2] for p in positions]
    vx = [v[0] for v in velocities]
    vy = [v[1] for v in velocities]
    vz = [v[2] for v in velocities]
    eq1 = f"[ ({vz[0] - vz[2]})y - ({vz[1] - vz[2]})x ]"
    eq1 += f"[ ({x[1]-x[2]})x - ({x[0]-x[2]})y + ({vx[1]-vx[0]})xy ]"
    eq1 += f" = "
    eq1 += f"[ ({vx[0] - vx[2]})y - ({vx[1] - vx[2]})x ]"
    eq1 += f"[ ({z[1]-z[2]})x - ({z[0]-z[2]})y + ({vz[1]-vz[0]})xy ]"

    eq2 = f"[ ({vz[0] - vz[2]})y - ({vz[1] - vz[2]})x ]"
    eq2 += f"[ ({y[1]-y[2]})x - ({y[0]-y[2]})y + ({vy[1]-vy[0]})xy ]"
    eq2 += f" = "
    eq2 += f"[ ({vy[0] - vy[2]})y - ({vy[1] - vy[2]})x ]"
    eq2 += f"[ ({z[1]-z[2]})x - ({z[0]-z[2]})y + ({vz[1]-vz[0]})xy ]"

    print(eq1)
    print()
    print(eq2)
    print()

def getTimes(A, B, p, v):
    x = [r[0] for r in p]
    vx = [rdot[0] for rdot in v]
    numer = (x[1] - x[2])*A - (x[0]-x[2])*B + (vx[1] - vx[0])*A*B
    denom = (vx[0] - vx[2])*B - (vx[1] - vx[2])*A
    C = numer/denom
    t1 = A + C
    t2 = B + C
    t3 = C
    print(t1,t2,t3)
    return t1,t2,t3

def getAnswer(t1, t2, p, v):
    p1 = p[0]
    p2 = p[1]
    v1 = v[0]
    v2 = v[1]
    dp = [ p2[i] + v2[i]*t2 - p1[i] - v1[i]*t1 for i in range(3)]
    dt = t2 - t1
    vel = [dp[i]/dt for i in range(3)]
    p0 = [ p1[i] + v1[i]*t1 - dp[i]* t1/dt for i in range(3)]
    print(p0)
    return sum(p0)


t = time.time()
main() 
print("finished in", time.time() - t, "seconds")
