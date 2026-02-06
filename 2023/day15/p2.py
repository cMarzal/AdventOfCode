data = open('inp').read().split(',')
boxes = [[] for x in range(256)]
lenses = [[] for x in range(256)]

for inp in data:
    this_sum = 0
    if "=" in inp:
        box = inp.split("=")[0]
        lens = int(inp.split("=")[1])
        for char in box:
            this_sum = ((this_sum + ord(char)) * 17) % 256
        if box in boxes[this_sum]:
            lenses[this_sum][boxes[this_sum].index(box)] = lens
        else:
            boxes[this_sum].append(box)
            lenses[this_sum].append(lens)
    else:
        box = inp.split("-")[0]
        for char in box:
            this_sum = ((this_sum + ord(char)) * 17) % 256
        if box in boxes[this_sum]:
            pos = boxes[this_sum].index(box)
            lenses[this_sum].pop(pos)
            boxes[this_sum].pop(pos)
total_sum = 0
for x, box in enumerate(boxes):
    for y, inp in enumerate(box):
        total_sum += (x+1) * (y+1) * lenses[x][y]
print(total_sum)