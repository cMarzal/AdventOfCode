import re
all_data = open('inp').read()
data = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", all_data)

active = 1
tot_sum = 0
for record in data:
    if active:
        if "mul" in record:
            tot_sum += int(record.split("(")[1].split(",")[0]) * int(record.split(",")[1].split(")")[0])
    if record == "do()":
        active = 1
    elif record == "don't()":
        active = 0
print(tot_sum)