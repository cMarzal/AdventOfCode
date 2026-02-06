import networkx as nx

data = (group.split('-') for group in open('inp').read().split('\n'))
G = nx.Graph()
for a, b in data:
    G.add_edge(a, b)

cliques = list(nx.find_cliques(G))
max_size = max(len(c) for c in cliques)
largest_cliques = [c for c in cliques if len(c) == max_size]
print(','.join(sorted(largest_cliques[0])))
