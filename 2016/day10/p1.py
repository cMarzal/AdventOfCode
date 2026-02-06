inf_vals = {(line.split()[1], line.split()[5]) for line in open('inp') if line.startswith("value")}
inf_bots = {line.split(" gives")[0]: (line.split("to ")[1][:-10],line.split("to ")[2]) for line in open('inp').read().split("\n") if line.startswith("bot")}
bot_val = {k: set() for k in inf_bots.keys()}
for x in range(21):
    bot_val[f"output {x}"] = set()
for v1, v2 in inf_vals:
    bot_val[f"bot {v2}"].add(int(v1))
while inf_bots:
    ni = inf_bots.copy()
    for k, (v1, v2) in inf_bots.items():
        if len(bot_val[k]) == 2:
            bot_val[v1].add(min(bot_val[k]))
            bot_val[v2].add(max(bot_val[k]))
            del ni[k]
    inf_bots = ni
for k, v in bot_val.items():
    if 61 in v and 17 in v:
        print(k)
        break
