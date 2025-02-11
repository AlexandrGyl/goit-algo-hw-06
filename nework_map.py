'''
Маршрутизатори: R1, R2, R3, R4, R5  
Сервери: S1, S2, S3, S4, S5  
Клієнти: C1, C2, C3, C4

Вершина 1   Вершина 2   Пропускна здатність
R1	        R2	        1000
R1	        S1	        200
R1	        S2	        150
R2	        R3	        800
R2	        S3	        300
R3	        R4	        1000
R3	        S4	        250
R4	        R5	        2000
R4	        S5	        400
R5	        C1	        100
R5	        C2	        100
S1	        C3	        50
S5	        C4	        70
S2	        S3	        100
S3	        S4	        150
R1          C4          70
R2          C2          100
'''


import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_nodes_from(["R1", "R2", "R3", "R4", "R5", "S1", "S2", "S3", "S4", "S5", "C1", "C2", "C3", "C4"])

G.add_edges_from([
("R1", "R2", {"bandwidth": 1000, "weight": 1/1000}),
("R1", "S1", {"bandwidth": 200, "weight": 1/200}),
("R1", "S2", {"bandwidth": 150, "weight": 1/150}),
("R2", "R3", {"bandwidth": 800, "weight": 1/800}),
("R2", "S3", {"bandwidth": 300, "weight": 1/300}),
("R3", "R4", {"bandwidth": 1000, "weight": 1/1000}),
("R3", "S4", {"bandwidth": 250, "weight": 1/250}),
("R4", "R5", {"bandwidth": 2000, "weight": 1/2000}),
("R4", "S5", {"bandwidth": 400, "weight": 1/400}),
("R5", "C1", {"bandwidth": 100, "weight": 1/100}),
("R5", "C2", {"bandwidth": 100, "weight": 1/100}),
("S1", "C3", {"bandwidth": 50, "weight": 1/50}),
("S5", "C4", {"bandwidth": 70, "weight": 1/70}),
("S2", "S3", {"bandwidth": 100, "weight": 1/100}),
("S3", "S4", {"bandwidth": 150, "weight": 1/150}),
("R1", "C4", {"bandwidth": 70, "weight": 1/70}),
("R2", "C2", {"bandwidth": 100, "weight": 1/100})
])

pos = nx.spring_layout(G, seed=42)

options = {
    "node_color": "green",
    "edge_color": "blue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
options_1 = {
    "node_color": "red",
    "edge_color": "green",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}

options_2 = {
    "node_color": "yellow",
    "edge_color": "green",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}

nx.draw(G, pos, **options)
plt.title("Мережева топологія (пропускна здатність)")
plt.show()

dfs_tree = nx.dfs_tree(G, source='R1')
print (list(dfs_tree.edges()))
nx.draw(dfs_tree, pos, **options_2)
plt.show()

bfs_tree = nx.bfs_tree(G, source="R1")
print (list(bfs_tree.edges()))
nx.draw(bfs_tree,pos, **options_1)

plt.show()

short_parts = nx.single_source_dijkstra_path_length(G, source="R1", weight='weight')
print (short_parts)

nx.draw(G, pos, **options)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d:.2f}" for (u, v), d in nx.get_edge_attributes(G, 'weight').items()})
plt.title("Довжини шляхів за алгоритмом Дейкстри")
plt.show()