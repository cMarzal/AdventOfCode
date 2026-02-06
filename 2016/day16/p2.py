data = {line.split(":")[0]: {line.split()[2][:-1]: int(line.split()[3][:-1]),line.split()[4][:-1]: int(line.split()[5][:-1]),line.split()[6][:-1]: int(line.split()[7])} for line in open('inp')}
this_d = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
for k, v in data.items():
    this_sum = 0
    for k2, v2 in v.items():
        if k2 == "cat" or k2 == "trees":
            if this_d[k2] < v2: this_sum += 1
        elif k2 == "pomeranians" or k2 == "goldfish":
            if this_d[k2] > v2: this_sum += 1
        else:
            if this_d[k2] == v2: this_sum += 1
    if this_sum == 3:
        print(k)
        break
