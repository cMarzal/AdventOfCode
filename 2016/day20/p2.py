inp = 29000000
def all_divisors_sqrt(n):
    tot = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            tot += i if i >= n//50 else 0
            tot += n//i if i != n//i and n//i >= n//50 else 0
    return tot
for count in range(inp//100, inp, 2):
    if int(all_divisors_sqrt(count))*11 >= inp:
        print(count)
        break
