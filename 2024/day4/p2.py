data = [line for line in open('inp').read().split('\n')]
tot_sum = 0
for x in range(1,len(data[0])-1):
    for y in range(1,len(data)-1):
        if data[y][x] == "A":
            check_1 = {"M","S"}
            check_2 = {"M","S"}
            try:
                check_1.remove(data[y-1][x-1])
                check_1.remove(data[y+1][x+1])
                check_2.remove(data[y-1][x+1])
                check_2.remove(data[y+1][x-1])
                tot_sum += 1
            except:
                a=1
print(tot_sum)