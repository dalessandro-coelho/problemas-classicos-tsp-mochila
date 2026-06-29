ITENS = [
    (2, 10),
    (3, 5),
    (5, 15),
    (7, 7),
    (1, 6),
    (4, 18),
    (6, 12),
    (8, 25),
    (3, 9),
    (9, 16),
]

CAPACIDADE = 20


def resolver_mochila_pd(itens, capacidade):
    quantidade_itens = len(itens)

    dp = [
        [0 for _ in range(capacidade + 1)]
        for _ in range(quantidade_itens + 1)
    ]

    for i in range(1, quantidade_itens + 1):
        peso_item, valor_item = itens[i - 1]

        for capacidade_atual in range(capacidade + 1):
            if peso_item > capacidade_atual:
                dp[i][capacidade_atual] = dp[i - 1][capacidade_atual]
            else:
                nao_levar = dp[i - 1][capacidade_atual]
                levar = valor_item + dp[i - 1][capacidade_atual - peso_item]

                dp[i][capacidade_atual] = max(nao_levar, levar)

    return dp[quantidade_itens][capacidade]


resultado = resolver_mochila_pd(ITENS, CAPACIDADE)
print(resultado)