data = [(line.split(" -> ")[0].replace("AND", "&").replace("OR","|").replace("LSHIFT","<<").replace("RSHIFT",">>").replace("NOT","65535 -").replace("as","asa").replace("if","ifa").replace("in","ina").replace("is","isa"), line.split(" -> ")[1].replace("as","asa").replace("if","ifa").replace("in","ina").replace("is","isa")) for line in open('inp').read().split('\n')]
b = 46065
while data:
    d1, d2 = data.pop(0)
    if d2 != "b":
        try:
            globals()[d2] = eval(d1)
            last = d2
        except:
            data.append((d1,d2))
print(a)