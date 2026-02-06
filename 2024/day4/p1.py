data = [line for line in open('inp').read().split('\n')]
add_pos = (1,-1,1j,-1j,1+1j,1-1j,-1+1j,-1-1j)
tot_sum = 0
for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == "X":
            check_pos = complex(x, y)
            for new_pos in add_pos:
                this_pos = check_pos+new_pos
                if (0 <= this_pos.real < len(data[0])) and (0 <= this_pos.imag < len(data)) and data[int(this_pos.imag)][int(this_pos.real)] == "M":
                    this_pos = this_pos+new_pos
                    if (0 <= this_pos.real < len(data[0])) and (0 <= this_pos.imag < len(data)) and data[int(this_pos.imag)][int(this_pos.real)] == "A":
                        this_pos = this_pos + new_pos
                        if (0 <= this_pos.real < len(data[0])) and (0 <= this_pos.imag < len(data)) and data[int(this_pos.imag)][int(this_pos.real)] == "S":
                            tot_sum += 1
print(tot_sum)