import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

distancias = [[0, 24, 36, 0, 0, 0],
              [24, 0, 30, 12, 0, 0],
              [36, 30, 0, 17, 7, 17],
              [0, 12, 17, 0, 0, 36],
              [0, 0, 7, 0, 0, 9],
              [0, 0, 17, 36, 9, 0]]

no_inicial = int(input("Digite o ponto de origem (0 a 5): "))
no_final = int(input("Digite o ponto de destino (0 a 5): "))

G = nx.from_numpy_array(np.array(distancias))

caminho_minimo = nx.dijkstra_path(G, no_inicial, no_final)
arcos_caminho = [(caminho_minimo[i], caminho_minimo[i + 1]) for i in range(len(caminho_minimo)-1)]

soma_ponderacao = sum(distancias[u][v] for u, v in arcos_caminho)

posicoes_dos_nos = {0: [0, 1], 1:[1, 2], 2:[2, 0], 3:[3, 2], 4:[3, 0], 5:[5, 1]}

plt.figure(figsize = (8, 6))

nx.draw_networkx_nodes(G, pos = posicoes_dos_nos, node_color = 'white', edgecolors = 'black', node_size = 800)
nx.draw_networkx_labels(G, pos = posicoes_dos_nos, font_size = 10, font_color = 'black')

nx.draw_networkx_edges(G, pos = posicoes_dos_nos, edge_color = 'black', arrowsize = 20, width = 1)

for u, v in arcos_caminho:
    edge = plt.annotate("",
                        xy = posicoes_dos_nos[v], xycoords = 'data',
                        xytext = posicoes_dos_nos[u], textcoords = 'data',
                        arrowprops = dict(arrowstyle = "->", color = "red", linewidth = 2),
                        )

edge_labels = {(u, v): distancias[u][v] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos = posicoes_dos_nos, edge_labels = edge_labels, font_size = 8)

plt.axis('off')
plt.show()

print(f"Distância total: {soma_ponderacao}")
