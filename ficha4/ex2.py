import random  # Importa o módulo random para gerar números aleatórios
import time  # Importa o módulo time para medir o tempo de execução

# Função para criar um "mundo" no Wumpus World com base na probabilidade de ter um poço
def mundo_wumpus(prob_poco):
    mundo = [False, False, False]  # Inicializa um mundo com 3 posições, todas sem poço (False)
    
    # Itera sobre as 3 posições no mundo e decide aleatoriamente se cada posição tem um poço
    for i in range(len(mundo)):
        prob = random.random()  # Gera um número aleatório entre 0 e 1
        if prob < prob_poco:  # Se o número for menor que a probabilidade de poço (prob_poco)...
            mundo[i] = True  # Marca a posição com um poço (True)
                
    return mundo  # Retorna o mundo gerado (lista com True/False indicando presença de poços)

# Função para verificar se há brisa no mundo, com base na posição dos poços
def verificar_brisa(mundo):
    # Regras para determinar se há brisa:
    if (mundo[0] and mundo[2]):  # Se houver poços nas posições 1 e 3 (index 0 e 2)...
        return True  # Há brisa
    elif (mundo[1]):  # Ou, se houver poço na posição 2 (index 1)...
        return True  # Há brisa
    else:
        return False  # Caso contrário, não há brisa

# Função para realizar a simulação, estimando probabilidades de poços
def simular(prob_poco=0.2):
    count_1_3 = 0  # Contador de poços na posição [1,3]
    count_2_2 = 0  # Contador de poços na posição [2,2]
    count_3_1 = 0  # Contador de poços na posição [3,1]
    mundos_validos = 0  # Contador de mundos válidos (aqueles que têm brisa)
    
    # Continua gerando mundos até que 10.000 mundos com brisa sejam encontrados
    while mundos_validos < 10000:
        mundo = mundo_wumpus(prob_poco)  # Gera um mundo com base na probabilidade de poço
        
        if verificar_brisa(mundo):  # Se o mundo gerado tiver brisa...
            mundos_validos += 1  # Incrementa o contador de mundos válidos
            if mundo[0]:  # Se a posição [1,3] tiver poço...
                count_1_3 += 1  # Incrementa o contador de poços na posição [1,3]
            if mundo[1]:  # Se a posição [2,2] tiver poço...
                count_2_2 += 1  # Incrementa o contador de poços na posição [2,2]
            if mundo[2]:  # Se a posição [3,1] tiver poço...
                count_3_1 += 1  # Incrementa o contador de poços na posição [3,1]
    
    # Calcula as probabilidades de poço para cada posição, dividindo o número de poços pelo número total de mundos válidos
    prob_1_3 = count_1_3 / mundos_validos  # Probabilidade de [1,3] ter um poço
    prob_2_2 = count_2_2 / mundos_validos  # Probabilidade de [2,2] ter um poço
    prob_3_1 = count_3_1 / mundos_validos  # Probabilidade de [3,1] ter um poço
    
    return prob_1_3, prob_2_2, prob_3_1  # Retorna as probabilidades calculadas

# Marca o tempo de início da simulação
inicio = time.time()

# Executa a simulação e obtém as probabilidades calculadas para cada posição
prob_1_3, prob_2_2, prob_3_1 = simular()

# Marca o tempo de término da simulação
fim = time.time()

# Calcula o tempo total de execução
tempo = fim - inicio

# Exibe as probabilidades formatadas com 3 casas decimais e o tempo total de execução
print(f"Probabilidade de [1,3] ter um poço: {prob_1_3:.3f}")
print(f"Probabilidade de [2,2] ter um poço: {prob_2_2:.3f}")
print(f"Probabilidade de [3,1] ter um poço: {prob_3_1:.3f}")
print(f"Tempo de execução: {tempo:.3f}")
