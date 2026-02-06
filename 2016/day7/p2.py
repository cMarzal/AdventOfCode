from re import findall
data = tuple(findall("[a-z]+",l) for l in open('inp').read().split("\n"))
tot = 0
for line in data:
    ret_yes = 0
    for x in range((len(line) + 1) // 2):
        this_line = line[x*2]
        for y in range(len(this_line)-2):
            if this_line[y] == this_line[y+2] and this_line[y] != this_line[y+1]:
                this_string = this_line[y+1] + this_line[y] + this_line[y+1]
                for i in range((len(line) - 1) // 2):
                    new_line = line[i * 2 + 1]
                    if this_string in new_line:
                        tot += 1
                        ret_yes = 1
                        break
                if ret_yes: break
        if ret_yes: break

print(tot)
