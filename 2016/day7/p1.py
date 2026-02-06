from re import findall
data = tuple(findall("[a-z]+",l) for l in open('inp').read().split("\n"))
tot = 0
for line in data:
    ret_no = 0
    ret_yes = 0
    for x in range((len(line)-1)//2):
        this_line = line[x*2+1]
        for y in range(len(this_line)- 3):
            if this_line[y] == this_line[y+3] and this_line[y+1] == this_line[y+2] and this_line[y] != this_line[y+1]:
                ret_no = 1
                break
        if ret_no: break
    if not ret_no:
        for x in range((len(line)+1) // 2):
            this_line = line[x * 2]
            for y in range(len(this_line) - 3):
                if this_line[y] == this_line[y + 3] and this_line[y + 1] == this_line[y + 2] and this_line[y] != this_line[y+1]:
                    tot += 1
                    ret_yes = 1
                    break
            if ret_yes: break
print(tot)
