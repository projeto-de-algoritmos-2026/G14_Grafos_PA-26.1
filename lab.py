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

    TERRAIN = {
        0: {"emoji": "⬜", "cost": 1},   
        1: {"emoji": "⬛", "cost": None},
        2: {"emoji": "🌿", "cost": 2},   
        3: {"emoji": "🟨", "cost": 3},   
        4: {"emoji": "💧", "cost": 5},   
    }

    if "maze" not in st.session_state:
        st.session_state.maze = np.zeros((SIZE, SIZE), dtype=int)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Resetar labirinto"):
            st.session_state.maze = np.zeros((SIZE, SIZE), dtype=int)
            st.rerun()

    with col2:
        if st.button("Criar mapa aleatório"):
            maze = np.zeros((SIZE, SIZE), dtype=int)
            for r in range(SIZE):
                for c in range(SIZE):
                    if (r, c) not in [START, END]:
                        if np.random.rand() < 0.3:
                            maze[r, c] = np.random.choice([1, 2, 3, 4])
            st.session_state.maze = maze
            st.rerun()

    st.session_state.maze[START] = 0
    st.session_state.maze[END] = 0

    grid_grafo = {}
    for r in range(SIZE):
        for c in range(SIZE):
            tipo = st.session_state.maze[r, c]

            if tipo != 1:  
                vizinhos = []
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < SIZE and 0 <= nc < SIZE:
                        tipo_vizinho = st.session_state.maze[nr, nc]

                        if tipo_vizinho != 1:
                            custo = TERRAIN[tipo_vizinho]["cost"]
                            vizinhos.append(((nr, nc), custo))

                grid_grafo[(r, c)] = vizinhos

    st.subheader("Monte seu labirinto (clique para mudar o terreno)")
    cols = st.columns(SIZE)

    for r in range(SIZE):
        for c in range(SIZE):
            with cols[c]:
                if (r, c) == START:
                    label = "🏁"
                elif (r, c) == END:
                    label = "🎯"
                else:
                    tipo = st.session_state.maze[r, c]
                    label = TERRAIN[tipo]["emoji"]

                disabled = (r, c) == START or (r, c) == END

                if st.button(label, key=f"m-{r}-{c}", disabled=disabled):
                    st.session_state.maze[r, c] = (st.session_state.maze[r, c] + 1) % 5
                    st.rerun()

    path, cost = dijkstra(grid_grafo, START, END)

    st.subheader("Resultado")

    st.markdown("""         
    **Legenda:**
                
    ⬜ Livre (1)  
    🌿 Grama (2)  
    🟨 Areia (3)  
    💧 Água (5)  
    ⬛ Parede  
    """)

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
                    tipo = st.session_state.maze[r, c]
                    row += TERRAIN[tipo]["emoji"]

            st.text(row)
    else:
        st.error("Não existe caminho possível.")

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
                    tipo = st.session_state.maze[r, c]
                    row += TERRAIN[tipo]["emoji"]

            st.text(row)