import math
import random

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
TENTATIVAS = 100

random.seed(42)


def calcular_distancia(cidade_a, cidade_b):
    return math.dist(CIDADES[cidade_a], CIDADES[cidade_b])


def executar_vizinho_mais_proximo(cidade_inicial):
    rota = [cidade_inicial]
    visitadas = {cidade_inicial}
    cidade_atual = cidade_inicial

    while len(visitadas) < len(nomes_cidades):
        cidades_disponiveis = [
            cidade
            for cidade in nomes_cidades
            if cidade not in visitadas
        ]

        proxima_cidade = min(
            cidades_disponiveis,
            key=lambda cidade: calcular_distancia(
                cidade_atual,
                cidade
            )
        )

        rota.append(proxima_cidade)
        visitadas.add(proxima_cidade)
        cidade_atual = proxima_cidade

    rota.append(cidade_inicial)

    distancia_total = 0

    for i in range(len(rota) - 1):
        distancia_total += calcular_distancia(
            rota[i],
            rota[i + 1]
        )

    return rota, distancia_total


melhor_rota = None
melhor_distancia = float("inf")

for _ in range(TENTATIVAS):
    cidade_inicial = random.choice(nomes_cidades)

    rota, distancia_total = executar_vizinho_mais_proximo(
        cidade_inicial
    )

    if distancia_total < melhor_distancia:
        melhor_distancia = distancia_total
        melhor_rota = rota

print(f"{melhor_distancia:.2f}")