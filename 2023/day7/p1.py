def hand_strength(hand):
    dd = dict()
    j_count = hand.count("J")
    for char in hand:
        dd[char] = hand.count(char)
    dd["J"] = 0
    srt = sorted(dd.values(), reverse=True)
    srt[0] += j_count
    return srt


char_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
def comp_hand(line_new, line_old):
    for k1, k2 in zip(line_new[2], line_old[2]):
        if k1 > k2:
            return 1
        elif k2 > k1:
            return 0
    for c1, c2 in zip(line_new[0], line_old[0]):
        if char_order.index(c1) < char_order.index(c2):
            return 1
        elif char_order.index(c2) < char_order.index(c1):
            return 0
    return 0


data = [[line.split(" ")[0], line.split(" ")[1], hand_strength(line.split(" ")[0])] for line in open('inp').read().split('\n')]
ordered_data = []
for x, line in enumerate(data):
    if x == 0:
        ordered_data.append(line)
    else:
        for order, this_line in enumerate(ordered_data):
            if comp_hand(line, this_line) == 0:
                ordered_data = ordered_data[:order] + [line] + ordered_data[order:]
                break
        else:
            ordered_data.append(line)

print(sum([int(line[1]) * (pos + 1) for pos, line in enumerate(ordered_data)]))