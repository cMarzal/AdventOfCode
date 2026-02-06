import numpy as np
from decimal import Decimal as D, getcontext

getcontext().prec = 50

import re

numParser = re.compile(r"(-?\d+)")
parseNums = lambda inp: [D(x) for x in numParser.findall(inp)]

with open('inp') as f:
    d24s = f.read()

class Hail:
    def __init__(self, inp, debug=False):
        self.debug = debug
        self.px, self.py, self.pz, self.vx, self.vy, self.vz = parseNums(inp)
        self.XYslope = D('inf') if self.vx == 0 else self.vy / self.vx
        self.ax, self.ay, self.az = 0, 0, 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.px}, {self.py}, {self.pz} @ {self.vx}, {self.vy}, {self.vz}>'

    def intersectXY(self, other):
        if self.XYslope == other.XYslope:
            return None
        if self.XYslope == float('inf'):  # self is vertical
            intX = self.px
            intY = other.XYslope * (intX - other.px) + other.py
        elif other.XYslope == float('inf'):  # other is vertical
            intX = other.px
            intY = self.XYslope * (intX - self.px) + self.py
        else:
            intX = (self.py - other.py - self.px * self.XYslope + other.px * other.XYslope) / (
                        other.XYslope - self.XYslope)
            intY = self.py + self.XYslope * (intX - self.px)
        intX, intY = intX.quantize(D(".1")), intY.quantize(D(".1"))

        selfFuture = np.sign(intX - self.px) == np.sign(self.vx)
        otherFuture = np.sign(intX - other.px) == np.sign(other.vx)
        if not (selfFuture and otherFuture):
            return None
        return (intX, intY)

    def adjust(self, ax, ay, az):
        self.vx -= ax - self.ax
        self.vy -= ay - self.ay
        self.vz -= az - self.az
        assert type(self.vx) is D
        self.XYslope = D('inf') if self.vx == 0 else self.vy / self.vx
        self.ax, self.ay, self.az = ax, ay, az

    def getT(self, p):
        if self.vx == 0:
            return (p[1] - self.py) / self.vy
        return (p[0] - self.px) / self.vx

    def getZ(self, other, inter):
        tS = self.getT(inter)
        tO = other.getT(inter)
        if tS == tO:
            assert self.pz + tS * self.vz == other.pz + tO * other.vz
            return None
        return (self.pz - other.pz + tS * self.vz - tO * other.vz) / (tS - tO)

def p2(inp, debug=False):
    hailstones = []
    for row in inp.strip().splitlines():
        hailstones.append(Hail(row, debug=debug))

    N = 0
    while True:
        for X in range(N + 1):
            Y = N - X
            for negX in (-1, 1):
                for negY in (-1, 1):
                    aX = X * negX
                    aY = Y * negY
                    H1 = hailstones[0]
                    H1.adjust(aX, aY, 0)
                    inter = None
                    for H2 in hailstones[1:]:
                        H2.adjust(aX, aY, 0)
                        p = H1.intersectXY(H2)
                        if p is None:
                            break
                        if inter is None:
                            inter = p
                            continue
                        if p != inter:
                            break
                    if p is None or p != inter:
                        continue
                    aZ = None
                    H1 = hailstones[0]
                    for H2 in hailstones[1:]:
                        nZ = H1.getZ(H2, inter)
                        if aZ is None:
                            aZ = nZ
                            continue
                        elif nZ != aZ:
                            return
                            break
                    if aZ == nZ:
                        H = hailstones[0]
                        Z = H.pz + H.getT(inter) * (H.vz - aZ)
                        print(int(Z + inter[0] + inter[1]))
                        return
        N += 1

p2(d24s, debug=False)  # P2 answer