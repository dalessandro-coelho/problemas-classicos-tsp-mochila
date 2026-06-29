ITENS = [
    {"id": 1, "peso": 2, "valor": 10},
    {"id": 2, "peso": 3, "valor": 5},
    {"id": 3, "peso": 5, "valor": 15},
    {"id": 4, "peso": 7, "valor": 7},
    {"id": 5, "peso": 1, "valor": 6},
    {"id": 6, "peso": 4, "valor": 18},
    {"id": 7, "peso": 6, "valor": 12},
    {"id": 8, "peso": 8, "valor": 25},
    {"id": 9, "peso": 3, "valor": 9},
    {"id": 10, "peso": 9, "valor": 16},
]

CAPACIDADE = 20

def preencher_espaco_residual(
    selecionados,
    nao_selecionados,
    capacidade,
    peso_atual,
    valor_atual,
):

    for item in list(nao_selecionados):
        if peso_atual + item["peso"] <= capacidade:
            selecionados.append(item)
            nao_selecionados.remove(item)

            peso_atual += item["peso"]
            valor_atual += item["valor"]
    return peso_atual, valor_atual

def resolver_hder(itens, capacidade):
    itens_ordenados = sorted(
        itens,
        key=lambda item: item["valor"] / item["peso"],
        reverse=True,
    )

    selecionados = []
    nao_selecionados = []
    peso_atual = 0
    valor_atual = 0

    for item in itens_ordenados:
        if peso_atual + item["peso"] <= capacidade:
            selecionados.append(item)
            peso_atual += item["peso"]
            valor_atual += item["valor"]
        else:
            nao_selecionados.append(item)

    peso_atual, valor_atual = preencher_espaco_residual(
        selecionados,
        nao_selecionados,
        capacidade,
        peso_atual,
        valor_atual,
    )

    houve_melhoria = True
    while houve_melhoria:
        houve_melhoria = False
        for item_dentro in list(selecionados):
            for item_fora in list(nao_selecionados):
                novo_peso = (
                    peso_atual
                    - item_dentro["peso"]
                    + item_fora["peso"]
                )

                troca_vantajosa = (
                    novo_peso <= capacidade
                    and item_fora["valor"] > item_dentro["valor"]
                )

                if troca_vantajosa:
                    selecionados.remove(item_dentro)
                    nao_selecionados.remove(item_fora)

                    selecionados.append(item_fora)
                    nao_selecionados.append(item_dentro)

                    peso_atual = novo_peso
                    valor_atual = (
                        valor_atual
                        - item_dentro["valor"]
                        + item_fora["valor"]
                    )

                    peso_atual, valor_atual = preencher_espaco_residual(
                        selecionados,
                        nao_selecionados,
                        capacidade,
                        peso_atual,
                        valor_atual,
                    )

                    houve_melhoria = True
                    break

            if houve_melhoria:
                break

    return valor_atual

resultado = resolver_hder(ITENS, CAPACIDADE)
print(resultado)