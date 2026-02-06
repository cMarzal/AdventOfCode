import re
data = open('inp').read()
print(sum((map(int, re.findall(r'-?\d+', data)))))
