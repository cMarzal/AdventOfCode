import re
all_data = open('inp').read()
data = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", all_data)

total_sum = sum([int(d[0])*int(d[1]) for d in data])
print(total_sum)