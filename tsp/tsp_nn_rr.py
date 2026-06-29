import math
import networkx as nx

CIDADES = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (3, 1),
    "D": (5, 3),
    "E": (6, 6),
    "F": (8, 2),
    "G": (9, 5),
    "H": (1, 7),
    "I": (4, 8),
    "J": (7, 9),
}

nomes_cidades = list(CIDADES.keys())

grafo = nx.Graph()
grafo.add_nodes_from(nomes_cidades)

for i in range(len(nomes_cidades)):
    for j in range(i + 1, len(nomes_cidades)):
        origem = nomes_cidades[i]
        destino = nomes_cidades[j]

        distancia = math.dist(CIDADES[origem], CIDADES[destino])

        grafo.add_edge(
            origem,
            destino,
            weight=distancia
        )

ciclo = nx.approximation.christofides(
    grafo,
    weight="weight"
)

distancia_total = 0

for i in range(len(ciclo) - 1):
    origem = ciclo[i]
    destino = ciclo[i + 1]

    distancia_total += grafo[origem][destino]["weight"]

print(f"{distancia_total:.2f}")