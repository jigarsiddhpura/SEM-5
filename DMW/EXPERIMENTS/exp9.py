import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

graph_matrix = np.array([
[0, 0, 0, 1, 0, 0, 0, 0], # A -> D
[0, 0, 1, 0, 1, 0, 0, 0], # B -> E, C
[1, 0, 0, 0, 0, 0, 0, 0], # C -> A
[0, 0, 1, 0, 0, 0, 0, 0], # D -> C
[0, 1, 1, 1, 0, 1, 0, 0], # E -> B, C, D, F
[0, 0, 1, 0, 0, 0, 0, 1], # F -> C, H
[1, 0, 1, 0, 0, 0, 0, 0], # G -> A, C
[1, 0, 0, 0, 0, 0, 0, 0], # H -> A
])

G = nx.DiGraph()
labels = {}

for i in range(len(graph_matrix)):
    node_label = chr(ord('A') + i)
    labels[i] = node_label
    G.add_node(i, label=node_label)
    for j in range(len(graph_matrix[i])):
        if graph_matrix[i][j] == 1:
            G.add_edge(i, j)

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True, labels=labels)
hubs, authorities = nx.hits(G, max_iter=50, normalized=True)

print("Hub Scores:")
for key, value in hubs.items():
    print(f'{labels[key]}: {value}')
print()

print("Authority Scores:")
for key, value in authorities.items():
    print(f'{labels[key]}: {value}')
plt.show()
