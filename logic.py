import heapq


def dijkstra(grafo, inicio, fim):
    """
    Encontra o menor caminho entre 'inicio' e 'fim' usando o algoritmo de Dijkstra.

    Parâmetros:
        grafo: dicionário no formato
               {no: [(vizinho, peso), ...]}
        inicio: nó inicial
        fim: nó final

    Retorna:
        (rota, custo_total)
        - rota: lista com os nós do caminho encontrado
        - custo_total: soma dos pesos do caminho
        Se não existir caminho, retorna ([], float('inf'))
    """

    # Inicializa todas as distâncias como infinito
    distancias = {v: float("inf") for v in grafo}
    distancias[inicio] = 0

    # Guarda o predecessor de cada nó para reconstruir a rota
    predecessores = {v: None for v in grafo}

    # Fila de prioridade: (distância acumulada, nó)
    fila = [(0, inicio)]

    while fila:
        d_atual, u = heapq.heappop(fila)

        # Se encontrou o destino, pode encerrar
        if u == fim:
            break

        # Ignora entradas antigas da fila
        if d_atual > distancias[u]:
            continue

        # Explora os vizinhos do nó atual
        for vizinho, peso in grafo[u]:
            custo = d_atual + peso

            # Se encontrou um caminho melhor para o vizinho
            if custo < distancias[vizinho]:
                distancias[vizinho] = custo
                predecessores[vizinho] = u
                heapq.heappush(fila, (custo, vizinho))

    # Se não há caminho até o destino
    if distancias[fim] == float("inf"):
        return [], float("inf")

    # Reconstrução do caminho do fim até o início
    rota = []
    atual = fim
    while atual is not None:
        rota.insert(0, atual)
        atual = predecessores[atual]

    return rota, distancias[fim]