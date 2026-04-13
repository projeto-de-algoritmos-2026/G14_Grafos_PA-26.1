import streamlit as st
import numpy as np
from logic import dijkstra


st.set_page_config(page_title="Dijkstra Lab - UnB", layout="wide")


st.title(" Dijkstra Lab")


tab1, = st.tabs([" Labirinto Interativo"])


with tab1:
    st.header("Resolvendo Labirintos")
    SIZE = 10
    if 'maze' not in st.session_state:
        st.session_state.maze = np.zeros((SIZE, SIZE))
    grid_grafo = {}
    for r in range(SIZE):
        for c in range(SIZE):
            if st.session_state.maze[r, c] == 0:
                vizinhos = []
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE and st.session_state.maze[nr, nc] == 0:
                        vizinhos.append(((nr, nc), 1))
                grid_grafo[(r, c)] = vizinhos


    cols = st.columns(SIZE)
    for r in range(SIZE):
        for c in range(SIZE):
            with cols[c]:
                label = "⬛" if st.session_state.maze[r,c] == 1 else "⬜"
                if (r,c) == (0,0): label = "🏁"
                if (r,c) == (SIZE-1, SIZE-1): label = "🎯"
                if st.button(label, key=f"m-{r}-{c}"):
                    st.session_state.maze[r,c] = 1 - st.session_state.maze[r,c]
                    st.rerun()


    path, _ = dijkstra(grid_grafo, (0,0), (SIZE-1, SIZE-1))
   
    if path:
        st.success("Caminho encontrado!")
        res = ""
        for r in range(SIZE):
            row = ""
            for c in range(SIZE):
                if (r,c) in path: row += "🟦"
                elif st.session_state.maze[r,c] == 1: row += "⬛"
                else: row += "⬜"
            st.text(row)


