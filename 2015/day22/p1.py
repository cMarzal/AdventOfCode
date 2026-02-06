info_him = [int(line.split(": ")[1]) for line in open('inp')]
attacks = [(53,4,0,0,0,0),(73,2,2,0,0,0),(113,0,0,6,0,1),(173,6,0,0,0,1),(229,0,0,0,5,1)] # cost, damage, heal, armor, mana, turns
min_mana = 10000
def sim_turn(me_health, total_mana, him_health, effect, mana_used):
    global min_mana
    stacks = (3,7,101)
    him_damage = 9
    pos_attacks = {att for att in attacks if att[0] <= total_mana}
    if effect [0] > 1:
        pos_attacks.discard((173,6,0,0,0,1))
    if effect [1] > 1:
        pos_attacks.discard((113,0,0,5,0,1))
    if effect [2] > 1:
        pos_attacks.discard((229,0,0,0,5,1))
    min_mana_used = 10000
    for cost, damage, heal, armor, mana, turns in pos_attacks:
        new_mana_tot = total_mana-cost
        new_mana_used = mana_used+cost
        if new_mana_used < min_mana:
            new_health_me = me_health
            new_health_him = him_health
            this_effect = effect.copy()
            # our turn is 0, his is 1
            for x in range(2):
                new_health_him -= stacks[0] if this_effect[0] > 0 else 0
                new_mana_tot += stacks[2] if this_effect[2] > 0 else 0
                this_effect = [max(0,s-1) for s in this_effect]
                if x == 0:
                    if turns:
                        this_effect[0] += damage
                        this_effect[1] += armor
                        this_effect[2] += mana
                    else:
                        new_health_him -= damage
                        new_health_me += heal
                if new_health_him <= 0:
                    min_mana_used = min(min_mana_used, new_mana_used)
                    break
                if x == 1:
                    new_health_me -= him_damage - stacks[1] if this_effect[1] != 0 else him_damage
                    if new_health_me > 0:
                        min_mana_used = min(min_mana_used, sim_turn(new_health_me, new_mana_tot, new_health_him, this_effect, new_mana_used))
    min_mana = min(min_mana, min_mana_used)
    return min_mana_used

print(sim_turn(50, 500, 58, [0,0,0], 0))
