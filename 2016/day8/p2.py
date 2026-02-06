import re

data = tuple(re.findall(r"(rotate column|rotate row|rect).+?(\d+).+?(\d+)", line)[0] for line in open('inp').read().split('\n'))
l = set()
for what, x, y in data:
    x, y = int(x), int(y)
    match what:
        case "rect":
            l |= {complex(i, j) for i in range(x) for j in range(y)}
        case "rotate column":
            to_remove = {i for i in l if i.real == x}
            l -= to_remove
            l |= {complex(i.real, (i.imag + y) % 6) for i in to_remove}
        case "rotate row":
            to_remove = {i for i in l if i.imag == x}
            l -= to_remove
            l |= {complex((i.real + y) % 50, i.imag) for i in to_remove}

for y in range(6):
    row = ""
    for x in range(50):
        if complex(x, y) in l:
            row += "# "
        else:
            row += "  "
    print(row)