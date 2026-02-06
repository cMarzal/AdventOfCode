from itertools import combinations
from shapely.geometry import Polygon

data = [(int(line.split(",")[0]),int(line.split(",")[1])) for line in open('inp').read().split('\n')]
main_poly = Polygon(data)
pairs = combinations(data, 2)
distances = sorted([(abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1) for p1, p2 in pairs if main_poly.contains(Polygon([p1,(p1[0],p2[1]),p2,(p2[0],p1[1])]))])
print(distances[-1])
