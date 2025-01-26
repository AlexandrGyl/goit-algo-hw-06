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
("R1", "R2", {"bandwidth": 1000}),
("R1", "S1", {"bandwidth": 200}),
("R1", "S2", {"bandwidth": 150}),
("R2", "R3", {"bandwidth": 800}),
("R2", "S3", {"bandwidth": 300}),
("R3", "R4", {"bandwidth": 1000}),
("R3", "S4", {"bandwidth": 250}),
("R4", "R5", {"bandwidth": 2000}),
("R4", "S5", {"bandwidth": 400}),
("R5", "C1", {"bandwidth": 100}),
("R5", "C2", {"bandwidth": 100}),
("S1", "C3", {"bandwidth": 50}),
("S5", "C4", {"bandwidth": 70}),
("S2", "S3", {"bandwidth": 100}),
("S3", "S4", {"bandwidth": 150}),
("R1", "C4", {"bandwidth": 70}),
("R2", "C2", {"bandwidth": 100})

])

pos = nx.spring_layout(G, seed=42)

options = {
    "node_color": "green",
    "edge_color": "blue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}

nx.draw(G, pos, **options)
plt.title("Мережева топологія (пропускна здатність)")
plt.show()

dfs_tree = nx.dfs_tree(G, source='R1')
print (list(dfs_tree.edges()))
nx.draw(dfs_tree, pos, **options)
plt.show()

bfs_tree = nx.bfs_tree(G, source="R1")
print (list(bfs_tree.edges()))
nx.draw(bfs_tree,pos, **options)

plt.show()