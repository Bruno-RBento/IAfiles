import networkx as nx

import exer8  # Importa o módulo 'exer8', que deve conter a função 'carregar_grafo'
import ex1    # Importa o módulo 'ex1', que provavelmente contém a função 'ler_teclado'

# Carrega o grafo a partir do arquivo "cidadesKM.csv" usando a função 'carregar_grafo' do módulo 'exer8'
grafo = exer8.carregar_grafo("cidadesKM.csv")

# Função que calcula o comprimento (distância total) do caminho mais curto entre dois nós do grafo
def caminho(g):
    origem = ex1.ler_teclado()  # Lê o nó de origem a partir de uma entrada do usuário, usando 'ler_teclado' do módulo 'ex1'
    destino = ex1.ler_teclado() # Lê o nó de destino a partir de uma entrada do usuário, usando 'ler_teclado' do módulo 'ex1'
    return nx.shortest_path_length(g, origem, destino, weight='weight')
    # Usa a função 'shortest_path_length' da biblioteca NetworkX para calcular a menor distância (caminho) entre 'origem' e 'destino'.
    # O argumento 'weight='weight'' especifica que o peso (distância) das arestas deve ser considerado no cálculo.

# A linha abaixo está comentada, mas poderia ser usada para imprimir o resultado da função 'caminho' para o grafo carregado
# print(caminho(grafo))

# Função alternativa que calcula o comprimento do caminho mais curto entre dois nós, mas recebe a origem e destino como parâmetros
def caminhoNoInput(g, origem, destino):
    return nx.shortest_path_length(g, origem, destino, weight='weight')
    # A mesma função que acima, mas sem necessidade de ler entradas do usuário diretamente.
    # Em vez disso, as cidades de 'origem' e 'destino' são passadas como argumentos diretamente.
