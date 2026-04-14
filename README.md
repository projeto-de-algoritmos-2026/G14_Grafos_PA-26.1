# G14_Grafos_PA-26.1 

Número da Dupla: 14<br>
Conteúdo da Disciplina: Grafo<br>
Vídeo da Apresentação: (https://youtu.be/De6rwbIhTv8)

## Alunas
|Matrícula | Aluna |
| -- | -- |
| 231026840 |  Laryssa Félix |
| 231027005  |  Maria Samara |

---

## Sobre 
Este projeto tem como objetivo demonstrar a aplicação prática de algoritmos de grafos, utilizando como exemplo a resolução de um labirinto interativo.<br>

O sistema criado permite ao usuário montar o próprio labirinto de forma interativa e visualizar o caminho encontrado pelo algoritmo, além de informar quando não existe solução possível.

### Modelagem do Problema

O labirinto é modelado como um **grafo**, no qual:

- Cada célula livre representa um **vértice**
- As conexões entre células adjacentes (cima, baixo, esquerda e direita) representam **arestas**
- Cada aresta possui um **peso**, que neste projeto é representado por:

<div align="center">
    
| Terreno | Representação | Peso |
|--------|-------------|------|
| Parede | ⬛ | 0 |
| Livre  | ⬜ | 1 |
| Grama  | 🌿 | 2 |
| Areia  | 🟨 | 3 |
| Água   | 💧 | 5 |

</div>

Essa modelagem transforma o labirinto em um problema clássico de busca em grafos, permitindo aplicar algoritmos para encontrar um caminho mais barato entre a entrada e a saída do labirinto.<br>

Além da representação em grafo, o problema também pode ser interpretado como uma busca em árvore implícita. Cada posição no labirinto corresponde a um estado, e os movimentos possíveis geram novos estados, formando uma árvore de exploração. O algoritmo percorre esses estados até encontrar a solução. <br>

### Algoritmo Utilizado: Dijkstra

Para resolver o problema, foi utilizado o **algoritmo de Dijkstra**, amplamente utilizado para encontrar o caminho de menor custo em grafos com pesos não negativos.

O funcionamento do algoritmo pode ser resumido em:

- Inicializa todas as distâncias como infinito
- Define a distância do ponto inicial como 0
- Utiliza uma **fila de prioridade (heap)** para sempre explorar o nó com menor custo acumulado
- Atualiza as distâncias dos vizinhos sempre que encontra um caminho de menor custo
- Continua o processo até alcançar o destino

No contexto do labirinto:

- O algoritmo percorre as células livres, modeladas como vértices de um grafo ponderado
- Cada movimento entre células possui um custo associado, de acordo com o tipo de terreno
- O algoritmo calcula o menor custo acumulado até cada posição
- Garante que o caminho encontrado até a saída seja o mais eficiente possível e que o caminho encontrado até a saída seja o de menor custo total, mesmo que não seja o mais curto em número de passos


### Funcionamento do Sistema

O sistema desenvolvido permite:

- Criar um labirinto de forma interativa
- Adicionar e remover obstáculos
- Visualizar o caminho encontrado pelo algoritmo
- Exibir o custo total do caminho
- Identificar quando não existe solução possível

---

## Screenshots

### Labirinto Inicial vazio

Representa o estado inicial do sistema, onde todas as células estão livres. Neste momento, o algoritmo encontra automaticamente o caminho mínimo direto entre o ponto inicial (🏁) e o final (🎯).

![Labirinto vazio](images/lab_inicial.png)

### Labirinto com Obstáculos Criados pelo Usuário

Mostra o labirinto após a interação do usuário, onde algumas células foram transformadas em obstáculos (⬛, ⬜, 🌿, 🟨, 💧). Isso altera o grafo e força o algoritmo a buscar caminhos alternativos.

![Labirinto com obstáculos](images/caminho_usuario.png) 

### Resultado com Caminho Encontrado

Exibe o resultado da execução do algoritmo de Dijkstra, destacando o caminho encontrado (🟦) entre o início e o fim, além do custo total da rota.

![Caminho encontrado](images/caminho_encontrado.png)

### Caso sem Solução

Demonstra um cenário onde não existe caminho possível entre o ponto inicial e o final devido aos obstáculos. O sistema identifica essa condição e informa ao usuário.

![Sem solução](images/sem_caminho.png)

---

## Instalação 
Linguagem: python 3.10+<br>
Framework: Streamlit<br>

### Pré-requisitos:
- Python 3 instalado
- pip instalado

### Passos:

Clone o repositório:
```bash
git clone https://github.com/projeto-de-algoritmos-2026/G14_Grafos_PA-26.1
cd G28-Busca-EDA2-26.1
```

Instale as dependências:
```
pip install -r requirements.txt
```

## Uso 

Para executar o projeto, utilize o seguinte comando:
```
streamlit run lab.py
```

### Após executar:

1. O navegador abrirá automaticamente com a interface do projeto.
2. Clique nas células do grid para criar ou remover paredes.
3. O ponto inicial é representado por 🏁 e a saída por 🎯.
4. O algoritmo irá automaticamente calcular o melhor caminho.
5. O caminho encontrado será destacado em azul 🟦.

Observação:
Caso não exista solução, o sistema exibirá uma mensagem de erro.

### Regras do labirinto

- O jogador deve sair do ponto 🏁 e chegar ao ponto 🎯.

- Movimentos permitidos:

    -cima<br>
    -baixo<br>
    -esquerda<br>
    -direita<br>
    
Tipos de células:
| Terreno | Representação | Peso |
|--------|-------------|------|
| Parede | ⬛ | 0 |
| Livre  | ⬜ | 1 |
| Grama  | 🌿 | 2 |
| Areia  | 🟨 | 3 |
| Água   | 💧 | 5 |


### Como montar o labirinto

Para editar o labirinto, basta clicar nos quadradinhos (vértices).
Cada clique muda o tipo de terreno na seguinte ordem:

- 1 clique → ⬛ Parede (bloqueia o caminho)<br>
- 2 cliques → 🌿 Grama (custo 2)<br>
- 3 cliques → 🟨 Areia (custo 3)<br>
- 4 cliques → 💧 Água (custo 5)<br>
- 5 cliques → ⬜ Livre (volta ao normal)<br>

Ou seja: é só ir clicando na célula que ela vai alternando entre os tipos.

### Gerar mapa automaticamente

Se você não quiser montar manualmente, pode clicar no botão:

- "Criar mapa aleatório"

Isso gera automaticamente um labirinto com:

- paredes
- diferentes tipos de terreno

Perfeito para testar rapidamente o algoritmo em diferentes cenários.

### Resetar o labirinto

Para limpar tudo e começar do zero, basta clicar no botão:

- "Resetar labirinto"

Isso remove todos os obstáculos e terrenos especiais, deixando apenas células livres.

### Observações importantes
🏁 Início e 🎯 destino não podem ser alterados<br>
⬛ Paredes bloqueiam o caminho<br>
🌿🟨💧 aumentam o custo do percurso<br>
<br>
O algoritmo busca o menor custo, não necessariamente o menor caminho em número de passos.<br>
Cada movimento possui um custo associado, dependendo do terreno da célula de destino.

## Justificativa do algoritmo

O algoritmo de Dijkstra foi escolhido por ser adequado para encontrar caminhos mínimos em grafos com pesos não negativos. Mesmo em um cenário simples, como o labirinto, ele garante que o caminho encontrado seja o de menor custo. Embora a implementação utilize grafos, o problema também pode ser interpretado como uma busca em árvore. Cada posição no labirinto representa um estado, e cada movimento gera novos estados possíveis. Assim, a exploração do labirinto corresponde à expansão de nós em uma árvore de busca.

## Estrutura do Projeto

```bash
G14_Grafos_PA-26.1 /
├── lab.py         # Interface interativa do projeto  
├── logic.py       # Implementação do algoritmo de Dijkstra.
                   # Contém a lógica de busca no grafo, cálculo das distâncias mínimas
                   # e reconstrução do caminho entre o ponto inicial e o final.
