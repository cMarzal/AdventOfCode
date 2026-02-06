data = [l for l in open('inp').read().split("\n")]
d1 = {"U": -1j, "L": -1, "R": 1, "D": 1j}
d2 = {"(2+0j)": "1", "(1+1j)": "2", "(2+1j)": "3", "(3+1j)": "4", "2j": "5", "(1+2j)": "6", "(2+2j)": "7", "(3+2j)": "8", "(4+2j)": "9", "(1+3j)": "A", "(2+3j)": "B", "(3+3j)": "C", "(2+4j)": "D"}
this_pos = 2j
fs = ""
for d in data:
    for c in d:
        this_pos += d1[c] if str(this_pos+d1[c]) in d2 else 0
    fs += d2[str(this_pos)]
print(fs)
