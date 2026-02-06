from functools import cache
data = [[line.split(" ")[0],tuple(map(int,line.split(" ")[1].split(",")))] for line in open('inp').read().split('\n')]

@cache
def check_sols(hotsprings, sizes, num_done_in_group=0):
    if not hotsprings:
        return not sizes and not num_done_in_group
    num_sols = 0
    possible = [".", "#"] if hotsprings[0] == "?" else hotsprings[0]
    for c in possible:
        if c == "#":
            num_sols += check_sols(hotsprings[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += check_sols(hotsprings[1:], sizes[1:])
            else:
                num_sols += check_sols(hotsprings[1:], sizes)
    return num_sols

print(sum(check_sols(group + ".", sizes) for group, sizes in data))