data = [line for line in open('inp').read().split('\n')]
dict_change = {".": "a", "-": 0, "7": 1 - 1j, "|": 0, "F": 1 + 1j, "L": -1 + 1j, "J": -1 -1j, "S": "S" }
im_data = [[dict_change[let] for let in pipe] for pipe in data]
steps = 1
last = 1  # since I manually see that there's pipes connected up and down, -1 is up
start_pos = 0
for x1, n in enumerate(im_data):
    for x2, m in enumerate(n):
        if m == "S":
            start_pos = x1 + (x2 * 1j)
            break
pos = start_pos + last
while True:
    new_pos = pos + im_data[int(pos.real)][int(pos.imag)] + last
    last = new_pos - pos
    pos = new_pos
    steps += 1
    if pos == start_pos:
        break
print(int(steps/2))
