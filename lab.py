import streamlit as st
import numpy as np
from logic import dijkstra

st.set_page_config(page_title="Dijkstra Lab - UnB", layout="wide")

st.title("Dijkstra Lab")
tab1, = st.tabs(["Labirinto Interativo"])

with tab1:
    st.header("Resolvendo Labirintos com Dijkstra")

    SIZE = 10
    START = (0, 0)
    END = (SIZE - 1, SIZE - 1)

    # Inicializa o labirinto
    if "maze" not in st.session_state:
        st.session_state.maze = np.zeros((SIZE, SIZE), dtype=int)

    # Botões de controle
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Resetar labirinto"):
            st.session_state.maze = np.zeros((SIZE, SIZE), dtype=int)
            st.rerun()

    with col2:
        if st.button("Criar paredes aleatórias"):
            maze = np.zeros((SIZE, SIZE), dtype=int)
            for r in range(SIZE):
                for c in range(SIZE):
                    if (r, c) not in [START, END]:
                        if np.random.rand() < 0.3:  # 30% de chance de parede
                            maze[r, c] = 1
            st.session_state.maze = maze
            st.rerun()

    # Garante que início e fim nunca sejam paredes
    st.session_state.maze[START] = 0
    st.session_state.maze[END] = 0

    # Monta o grafo com base nas células livres
    grid_grafo = {}
    for r in range(SIZE):
        for c in range(SIZE):
            if st.session_state.maze[r, c] == 0:
                vizinhos = []
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE:
                        if st.session_state.maze[nr, nc] == 0:
                            vizinhos.append(((nr, nc), 1))
                grid_grafo[(r, c)] = vizinhos

    st.subheader("Monte seu labirinto")
    cols = st.columns(SIZE)

    for r in range(SIZE):
        for c in range(SIZE):
            with cols[c]:
                if (r, c) == START:
                    label = "🏁"
                elif (r, c) == END:
                    label = "🎯"
                elif st.session_state.maze[r, c] == 1:
                    label = "⬛"
                else:
                    label = "⬜"

                # Impede clicar no início e no fim
                disabled = (r, c) == START or (r, c) == END

                if st.button(label, key=f"m-{r}-{c}", disabled=disabled):
                    st.session_state.maze[r, c] = 1 - st.session_state.maze[r, c]
                    st.rerun()

    # Executa Dijkstra
    path, cost = dijkstra(grid_grafo, START, END)

    st.subheader("Resultado")

    if path:
        st.success(f"Caminho encontrado com custo total = {cost}")
        for r in range(SIZE):
            row = ""
            for c in range(SIZE):
                pos = (r, c)
                if pos == START:
                    row += "🏁"
                elif pos == END:
                    row += "🎯"
                elif st.session_state.maze[r, c] == 1:
                    row += "⬛"
                elif pos in path:
                    row += "🟦"
                else:
                    row += "⬜"
            st.text(row)
    else:
        st.error("Não existe caminho possível entre a entrada e a saída.")
        for r in range(SIZE):
            row = ""
            for c in range(SIZE):
                pos = (r, c)
                if pos == START:
                    row += "🏁"
                elif pos == END:
                    row += "🎯"
                elif st.session_state.maze[r, c] == 1:
                    row += "⬛"
                else:
                    row += "⬜"
            st.text(row)