data = [l for l in open('inp').read().split("\n")]
d1 = {"U": -1j, "L": -1, "R": 1, "D": 1j}
d2 = {"0j": 1, "(1+0j)": 2, "(2+0j)": 3, "1j": 4, "(1+1j)": 5, "(2+1j)": 6, "2j": 7, "(1+2j)": 8, "(2+2j)": 9}
this_pos = 1+1j
fs = ""
for d in data:
    for c in d:
        this_pos += d1[c] if str(this_pos+d1[c]) in d2 else 0
    fs += str(d2[str(this_pos)])
print(fs)
