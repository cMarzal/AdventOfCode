import math
data = [line for line in open('inp').read().split('\n\n')]
dirs = data[0]
routes = {input_string.split(" =")[0]: (input_string.split("(")[1].split(",")[0], input_string.split(", ")[1].split(")")[0]) for input_string in data[1].split('\n')}
this_paths = [path for path in routes.keys() if path.endswith("A")]

def lcm(a,b):
  return (a * b) // math.gcd(a,b)

def min_steps(inp):
    this_path = inp
    count = 0
    while True:
        this_dir = 0 if dirs[count % len(dirs)] == "L" else 1
        this_path = routes[this_path][this_dir]
        count += 1
        if this_path.endswith("Z"):
            break
    return count
lowest = 1
for start in this_paths:
    lowest = lcm(lowest, min_steps(start))

print(lowest)