import networkx as nx
import csv
# Importando o módulo csv para leitura e manipulação de arquivos CSV

def carregar_grafo(filename):
    grafo = nx.Graph()
    # Inicializa um grafo vazio usando a biblioteca NetworkX (um grafo não direcionado)
    
    # Leitura do arquivo CSV
    with open(filename, mode='r') as cvsfile:
        reader = csv.reader(cvsfile)
        # 'csv.reader' é usado para ler o arquivo CSV
        next(reader)
        # Pula a primeira linha do arquivo (normalmente cabeçalhos)
        
        for row in reader:
            origem, destino, distancia = row
            # Para cada linha do arquivo, extraímos a origem, destino e a distância (peso)
            grafo.add_edge(origem, destino, weight=int(distancia))
            # Adiciona uma aresta no grafo entre 'origem' e 'destino', com a distância como peso (convertida para int)
    
    return grafo
    # Retorna o grafo construído a partir do arquivo CSV

def listar_vizinhos(grafo):
    for cidade in grafo.nodes:
        # Para cada nó (cidade) no grafo
        print(cidade, list(grafo.neighbors(cidade)))
        # Exibe o nome da cidade e seus vizinhos (nós conectados)

# Carrega o grafo a partir de um arquivo CSV chamado "cidadesKM.csv"
grafo = carregar_grafo("cidadesKM.csv")

# A função listar_vizinhos foi comentada, mas quando chamada, ela listaria todos os nós e seus vizinhos
#listar_vizinhos(grafo)
