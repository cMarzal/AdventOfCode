inp = 29000000
def sum_divs(n):
    tot = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            tot += i + n//i if i != n//i else i
    return tot
for count in range(inp//100, inp, 10):
    if int(sum_divs(count))*10 >= inp:
        print(count)
        break
