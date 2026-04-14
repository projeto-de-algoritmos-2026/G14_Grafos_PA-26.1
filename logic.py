import heapq

def dijkstra(grafo, inicio, fim):
    distancias = {v: float("inf") for v in grafo}
    distancias[inicio] = 0

    predecessores = {v: None for v in grafo}

    fila = [(0, inicio)]

    while fila:
        d_atual, u = heapq.heappop(fila)

        if u == fim:
            break

        if d_atual > distancias[u]:
            continue

        for vizinho, peso in grafo[u]:
            custo = d_atual + peso

            if custo < distancias[vizinho]:
                distancias[vizinho] = custo
                predecessores[vizinho] = u
                heapq.heappush(fila, (custo, vizinho))

    if distancias[fim] == float("inf"):
        return [], float("inf")

    rota = []
    atual = fim
    while atual is not None:
        rota.insert(0, atual)
        atual = predecessores[atual]

    return rota, distancias[fim]