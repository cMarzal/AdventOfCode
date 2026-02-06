data = [line for line in open('inp').read().split('\n')]
dict_change = {".": "a", "-": 0, "7": 1 - 1j, "|": 0, "F": 1 + 1j, "L": -1 + 1j, "J": -1 -1j, "S": "S"}
im_data = [[dict_change[let] for let in pipe] for pipe in data]

steps = 1
last = 1
start_pos = 0
for x1, n in enumerate(im_data):
    for x2, m in enumerate(n):
        if m == "S":
            start_pos = x1 + (x2 * 1j)
            break
pos = start_pos + last
pipe_list = {start_pos}
while True:
    pipe_list.add(pos)
    new_pos = pos + im_data[int(pos.real)][int(pos.imag)] + last
    last = new_pos - pos
    pos = new_pos
    steps += 1
    if pos == start_pos:
        break
    pipe_list.add(pos)

max_y = len(data)
max_x = len(data[0])
total_in = 0

for y in range(max_y):
    for x in range(max_x):
        if complex(y,x) not in pipe_list:
            this_sum = 0
            for yy in range(y+1):
                if complex(y-yy, x) in pipe_list:
                    this_sum += 1 if data[y-yy][x] in {"-","L","F"} else 0
            total_in += 1 if this_sum%2==1 else 0

print(total_in)
