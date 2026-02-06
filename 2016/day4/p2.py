data = tuple((l.split("-")[:-1], int(l.split("-")[-1].split("[")[0])) for l in open('inp'))
for s, i in data:
    this_str = "".join(["".join(chr((ord(sss) - ord('a') + i) % 26 + ord('a'))) for ss in s for sss in ss])
    if "north" in this_str:
        print(this_str, i)
