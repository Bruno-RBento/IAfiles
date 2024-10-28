# Função que calcula a probabilidade condicional de haver um poço na posição [1,3]
# baseado na probabilidade a priori fornecida (prob_inicial)
def calcular_probabilidade_1_3(prob_inicial):
    numero_de_vizinhos = 4  # Define o número de vizinhos ao redor de uma posição (no Wumpus World há 4 vizinhos)
    
    # Calcula a probabilidade de sentir brisa, levando em consideração os vizinhos
    # Se não houver um poço em nenhum dos vizinhos, não haverá brisa. Portanto, a
    # probabilidade de sentir brisa é 1 menos a probabilidade de não sentir brisa em todos os vizinhos.
    prob_sentir_brisa = 1 - (1 - float(prob_inicial)) ** numero_de_vizinhos
    
    # Calcula a probabilidade condicional de haver um poço na posição [1,3] dado que existe brisa.
    # Aqui é aplicado o teorema de Bayes, onde se divide a probabilidade de haver poço pela probabilidade de sentir brisa.
    prob = (1 * float(prob_inicial)) / prob_sentir_brisa
    
    return prob  # Retorna a probabilidade condicional calculada

# Solicita ao usuário que insira a probabilidade a priori de haver um poço
prob_inicial = input("Digite a probabilidade a priori: ")

# Chama a função calcular_probabilidade_1_3 com a probabilidade fornecida pelo usuário
probabilidade_1_3 = calcular_probabilidade_1_3(prob_inicial)

# Exibe a probabilidade condicional calculada formatada com 3 casas decimais
print(f"Probabilidade: {probabilidade_1_3:.3f}")
