#! /usr/bune/env python

import networkx as nx
import matplotlib.pyplot as plt

G=nx.random_geometric_graph(400,0.085)
# position is stored as node attribute data for random_geometric_graph
pos=nx.get_node_attributes(G,'pos')

# find node near center (1.0,1.0)
dmin=1
ncenter=0
for n in pos:
    x,y=pos[n]
    d=(x-0.5)**2+(y-0.5)**2
    if d<dmin:
        ncenter=n
        dmin=d

# color by path length from node near center
p=nx.single_source_shortest_path_length(G,ncenter)

plt.figure(figsize=(30,30))
nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
                       node_size=10,
                       node_color=p.values(),
                       cmap=plt.cm.ocean)

plt.xlim(0.0,1.0)
plt.ylim(0.0,1.0)
plt.axis('off')
plt.savefig('resources/bg.png', transparent=True)
