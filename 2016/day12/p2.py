import json
data = open('inp').read()
this_json = json.loads(data)

def get_tot_sum(j):
    if isinstance(j, list):
        return sum(get_tot_sum(j2) for j2 in j)
    elif isinstance(j, int):
        return j
    elif isinstance(j, dict):
        if "red" not in j.values():
            return sum(get_tot_sum(v) for v in j.values())
    return 0

print(get_tot_sum(this_json))
