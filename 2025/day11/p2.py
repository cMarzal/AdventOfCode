from functools import cache

data = {line.split(":")[0]: set(line.split()[1:]) for line in open('inp')}

@cache
def find_path(rack, out_rack):
    return rack == out_rack or sum(find_path(next_rack, out_rack) for next_rack in data[rack])

data["out"] = set()
print(find_path("dac", "out")*find_path("fft", "dac")*find_path("svr", "fft"))
