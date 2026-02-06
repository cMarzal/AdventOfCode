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


def p1(inp, pMin, pMax, debug=False):
    hailstones = []
    for row in inp.strip().splitlines():
        hailstones.append(Hail(row, debug=debug))
    sm = 0
    for idx, H1 in enumerate(hailstones):
        for H2 in hailstones[idx + 1:]:
            p = H1.intersectXY(H2)
            if p is not None and p[0] >= pMin and p[0] <= pMax and p[1] >= pMin and p[1] <= pMax:
                if debug: print(f'YES {H1} x {H2} (@ {p})')
                sm += 1
    return sm

print(p1(d24s, 200000000000000, 400000000000000, debug=False))  # P1 answer

