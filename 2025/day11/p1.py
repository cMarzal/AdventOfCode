from functools import cache

data = {line.split(":")[0]: set(line.split()[1:]) for line in open('inp')}

@cache
def find_path(rack):
    return rack == "out" or sum(find_path(next_rack) for next_rack in data[rack])

print(find_path("you"))
