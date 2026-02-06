data = open('inp').read().split(',')
final_sum = 0
for inp in data:
    this_sum = 0
    for char in inp:
        this_sum = ((this_sum + ord(char)) * 17) % 256
    final_sum += this_sum
print(final_sum)
