locks = [group.split('\n') for group in open('inp').read().split('\n\n') if group.startswith('#####')]
keys = [group.split('\n') for group in open('inp').read().split('\n\n') if not group.startswith('#####')]
nl = [[sum(1 if lock[x][c] == "#" else 0 for x in range(7)) for c in range(5)] for lock in locks]
kl = [[sum(1 if key[x][c] == "#" else 0 for x in range(7)) for c in range(5)] for key in keys]
tot_sum = sum(min(1 if ll + kk <= 7 else 0 for ll,kk in zip(l,k)) for l in nl for k in kl)
print(tot_sum)
