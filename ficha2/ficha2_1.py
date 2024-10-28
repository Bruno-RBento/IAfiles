import networkx as nx  # Importa a biblioteca NetworkX para manipulação de grafos
import exer8  # Módulo personalizado que contém a função para carregar o grafo
import ficha2  # Outro módulo personalizado, possivelmente com funções auxiliares

# Carrega o grafo a partir de um arquivo CSV com cidades e distâncias
G = exer8.carregar_grafo("cidadesKM.csv")
import csv  # Importa o módulo CSV (não utilizado diretamente no código aqui, mas pode ser necessário para manipular arquivos CSV)

# Função que calcula o comprimento (distância total) de um caminho dado no grafo G
def comprimento(G, caminho):
    total_weight = 0  # Inicializa a soma das distâncias como 0
    
    # Percorre cada par de cidades consecutivas no caminho (caminho[i] e caminho[i+1])
    for i in range(len(caminho) - 1):
        # Soma o peso (distância) da aresta entre caminho[i] e caminho[i+1]
        total_weight += G[caminho[i]][caminho[i + 1]]['weight']
    
    # Retorna a distância total para o caminho dado
    return total_weight

# Caminho de exemplo
caminho = ['Porto', 'Aveiro', 'Coimbra', 'Leiria', 'Lisboa']

# Função que encontra o caminho mais curto entre duas cidades usando BFS (Pesquisa em Largura)
def caminhoOrigemDestino(G, origem, destino):
    caminho = nx.shortest_path(G, origem, destino)  # Utiliza a BFS para encontrar o caminho mais curto
    return caminho  # Retorna a sequência de cidades que formam o caminho

# Função que encontra o caminho entre duas cidades usando BFS, com construção do caminho manualmente a partir das arestas
def caminhoOrigemPPL(G, origem, destino):
    # Executa BFS a partir da cidade de origem e coleta as arestas
    bfs_edges = list(nx.bfs_edges(G, origem, reverse=True))
    
    # Inicializa o caminho começando do destino
    path = [destino]
    current_node = destino
    
    # Mapeia cada nó para o nó anterior, formando uma árvore de pais
    parent = {v: u for u, v in bfs_edges}
    
    # Retrocede do destino até a origem, reconstruindo o caminho
    while current_node != origem:
        current_node = parent[current_node]
        path.append(current_node)
    
    # Reverte o caminho para que ele vá da origem até o destino
    path.reverse()
    return path

# Função que encontra o caminho mais curto usando o algoritmo A* (Pesquisa Informada)
def escolha_informada(G, origem, destino):
    caminho = nx.astar_path(G, origem, destino, weight='weight')  # Usa a heurística A* com pesos
    return caminho

# Função que encontra o caminho entre duas cidades usando DFS (Pesquisa em Profundidade)
def caminhoOrigemPPP(G, origem, destino):
    # Executa DFS e coleta as arestas
    edges = list(nx.dfs_edges(G, origem))
    
    # Inicializa o caminho começando do destino
    path = [destino]
    current_node = destino
    
    # Mapeia cada nó para o nó anterior
    parent = {v: u for u, v in edges}
    
    # Retrocede do destino até a origem
    while current_node != origem:
        current_node = parent[current_node]
        path.append(current_node)
    
    # Reverte o caminho para que ele vá da origem ao destino
    path.reverse()
    return path

# Função para criar uma tabela comparativa de resultados de diferentes algoritmos de busca
def criar_tabela(G, t):
    resultados = []
    total_ppl = 0
    total_a = 0
    total_ppp = 0
    
    # Cabeçalho da tabela
    print("Experiência\tPPL (BFS)\tA*\t\tPPP")
    
    # Para cada par de cidades (origem, destino) na lista t
    for i, (origem, destino) in enumerate(t):
        # Executa o algoritmo PPL (BFS) e calcula o comprimento do caminho
        caminho_ppl = caminhoOrigemPPL(G, origem, destino)
        comprimento_ppl = comprimento(G, caminho_ppl)
        
        # Executa o algoritmo A* e calcula o comprimento do caminho
        caminho_a = escolha_informada(G, origem, destino)
        comprimento_a = comprimento(G, caminho_a)
        
        # Executa o algoritmo PPP (DFS) e calcula o comprimento do caminho
        caminho_ppp = caminhoOrigemPPP(G, origem, destino)
        comprimento_ppp = comprimento(G, caminho_ppp)
        
        # Soma as distâncias para calcular médias depois
        total_ppl += comprimento_ppl
        total_a += comprimento_a
        total_ppp += comprimento_ppp
        
        # Adiciona os resultados à lista para gerar a tabela
        resultados.append([origem, destino, comprimento_ppl, comprimento_a, comprimento_ppp])
        
        # Exibe o resultado de cada experimento
        print(f"{i+1}\t\t{comprimento_ppl}\t\t{comprimento_a}\t\t{comprimento_ppp}")
    
    # Calcula as médias de distância para cada algoritmo
    media_ppl = total_ppl / len(t)
    media_a = total_a / len(t)
    media_ppp = total_ppp / len(t)
    
    # Exibe as médias de cada algoritmo
    print("Media")
    print(f"PPL: {media_ppl}")
    print(f"A*: {media_a}")
    print(f"PPP: {media_ppp}")

# Lista de pares de cidades (origem, destino) para os experimentos
data = [
    ('Faro', 'Braganca'),
    ('Beja', 'Lisboa'),
    ('Porto', 'Viseu'),
    ('Coimbra', 'Faro'),
    ('Lisboa', 'Porto'),
    ('Leiria', 'Aveiro'),
    ('Setubal', 'Vila Real'),
    ('Guarda', 'Evora'),
    ('Viseu', 'Faro'),
    ('Santarem', 'Coimbra')
]

# Executa a função para criar a tabela comparativa dos algoritmos
criar_tabela(G, data)

# Explicação:
# - PPL (BFS): Tende a encontrar o caminho mais curto em termos de número de nós percorridos, mas nem sempre o menor caminho em termos de distância total.
# - PPP (DFS): Explora profundamente antes de tentar caminhos alternativos, portanto, pode não encontrar o caminho mais curto.
# - A*: Geralmente encontra o caminho mais curto em termos de distância total, pois utiliza uma heurística baseada no peso das arestas.

#ler do teclado
def ler_teclado():
    nome = input("Digite o texto: ")
    print("O texto %s" % nome)
    return nome
