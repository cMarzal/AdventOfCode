data = [line.split() for line in open('inp')]
i = 0
values = {"a": 0, "b": 0}
while True:
    try:
        com = data[i]
        match com[0]:
            case "hlf": values[com[1]] = values[com[1]] // 2
            case "tpl" : values[com[1]] = values[com[1]] * 3
            case "inc": values[com[1]] += 1
            case "jmp": i += int(com[1]) - 1
            case "jie": i += int(com[2]) - 1 if values[com[1][:-1]]%2==0 else 0
            case "jio": i += int(com[2]) - 1 if values[com[1][:-1]]==1 else 0
        i+= 1
    except:
        print(values["b"])
        print(values["a"])
        exit()
