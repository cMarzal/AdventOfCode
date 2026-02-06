data = [1 if l == "(" else -1 for l in open('inp').read()]
floor = 0
for x, d in enumerate(data):
    floor += d
    if floor == -1:
        print(x+1)
        break
