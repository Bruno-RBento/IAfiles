import random  # Importa o módulo random para gerar números aleatórios

# Função para criar um "mundo" no Wumpus World com base na probabilidade de ter um poço
def mundo_wumpus(prob_poco):
    mundo = [False, False, False]  # Inicia um mundo com 3 posições, todas sem poço (False)
    
    for i in range(len(mundo)):  # Itera sobre as 3 posições no mundo
        prob = random.random()  # Gera um número aleatório entre 0 e 1
        if prob < prob_poco:  # Se o número gerado for menor que a probabilidade de poço...
            mundo[i] = True  # Coloca um poço (True) naquela posição
                
    return mundo  # Retorna o "mundo", ou seja, uma lista indicando onde há poços

# Função para verificar se há brisa no mundo, com base na localização dos poços
def verificar_brisa(mundo):
    if (mundo[0] and mundo[2]):  # Se houver poços nas posições 1 e 3...
        return True  # Há brisa
    elif (mundo[1]):  # Ou, se houver poço na posição 2...
        return True  # Há brisa
    else:
        return False  # Caso contrário, não há brisa

# Função que realiza a simulação para estimar probabilidades de poços nas posições [1,3], [2,2], [3,1]
def simular(prob_poco=0.2):
    count_1_3 = 0  # Conta quantas vezes a posição [1,3] tem um poço
    count_2_2 = 0  # Conta quantas vezes a posição [2,2] tem um poço
    count_3_1 = 0  # Conta quantas vezes a posição [3,1] tem um poço
    mundos_validos = 0  # Conta quantos mundos com brisa foram gerados
    
    # Continua simulando mundos até que 10.000 mundos válidos (com brisa) sejam gerados
    while mundos_validos < 10000:
        mundo = mundo_wumpus(prob_poco)  # Gera um novo mundo com base na probabilidade de poço
        
        if verificar_brisa(mundo):  # Verifica se o mundo tem brisa
            mundos_validos += 1  # Incrementa o contador de mundos válidos (com brisa)
            if mundo[0]:  # Se a posição [1,3] tiver poço, incrementa o contador correspondente
                count_1_3 += 1
            if mundo[1]:  # Se a posição [2,2] tiver poço, incrementa o contador correspondente
                count_2_2 += 1
            if mundo[2]:  # Se a posição [3,1] tiver poço, incrementa o contador correspondente
                count_3_1 += 1

    # Calcula as probabilidades de poço em cada posição como o número de poços dividido pelo total de mundos válidos
    prob_1_3 = count_1_3 / mundos_validos  # Probabilidade de [1,3] ter um poço
    prob_2_2 = count_2_2 / mundos_validos  # Probabilidade de [2,2] ter um poço
    prob_3_1 = count_3_1 / mundos_validos  # Probabilidade de [3,1] ter um poço
    
    return prob_1_3, prob_2_2, prob_3_1  # Retorna as três probabilidades calculadas
# Executa a simulação com a probabilidade de poço padrão (0.2 ou 20%) e armazena as probabilidades
prob_1_3, prob_2_2, prob_3_1 = simular()
# Exibe as probabilidades formatadas com 3 casas decimais
print(f"Probabilidade de [1,3] ter um poço: {prob_1_3:.3f}")
print(f"Probabilidade de [2,2] ter um poço: {prob_2_2:.3f}")
print(f"Probabilidade de [3,1] ter um poço: {prob_3_1:.3f}")