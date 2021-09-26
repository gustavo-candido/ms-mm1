def tipoDistribuicao(mapDist, nomeDist):
    distribuicoes = list(mapDist.keys())
    if nomeDist not in distribuicoes:
        print(f"Distribuição: '{nomeDist}' não suportada!\nInsira alguma das distribuições a seguir:")
        print(distribuicoes)
        raise SystemExit()
