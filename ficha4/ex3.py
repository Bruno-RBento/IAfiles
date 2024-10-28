import random  # Importa o módulo random para gerar números aleatórios
import time  # Importa o módulo time para medir o tempo de execução
import matplotlib.pyplot as plt  # Importa o módulo matplotlib para criar gráficos
import numpy as np  # Importa o módulo numpy (não utilizado diretamente neste código, mas comumente útil para cálculos)

# Função para criar um "mundo" no Wumpus World com base na probabilidade de ter um poço
def mundo_wumpus(prob_poco):
    mundo = [False, False, False]  # Inicializa um mundo com 3 posições, todas sem poço (False)
    
    # Itera sobre as 3 posições no mundo e decide aleatoriamente se cada posição tem um poço
    for i in range(len(mundo)):
        prob = random.random()  # Gera um número aleatório entre 0 e 1
        if prob < prob_poco:  # Se o número gerado for menor que a probabilidade de poço (prob_poco)...
            mundo[i] = True  # Coloca um poço (True) naquela posição
                
    return mundo  # Retorna o "mundo" gerado (lista com True/False indicando presença de poços)

# Função para verificar se há brisa no mundo, com base nas posições dos poços
def verificar_brisa(mundo):
    # Regras para determinar se há brisa:
    if (mundo[0] and mundo[2]):  # Se houver poços nas posições 1 e 3 (index 0 e 2)...
        return True  # Há brisa
    elif (mundo[1]):  # Ou, se houver poço na posição 2 (index 1)...
        return True  # Há brisa
    else:
        return False  # Caso contrário, não há brisa

# Função para simular mundos e calcular a probabilidade de poço na posição [2,2] condicionada à existência de brisa
def simular_poco_2_2(prob_poco):
    count_2_2 = 0  # Contador de poços na posição [2,2]
    mundos_validos = 0  # Contador de mundos válidos (aqueles que têm brisa)
    
    # Continua gerando mundos até que 10.000 mundos com brisa sejam encontrados
    while mundos_validos < 10000:
        mundo = mundo_wumpus(prob_poco)  # Gera um mundo com base na probabilidade de poço
        
        if verificar_brisa(mundo):  # Se o mundo tiver brisa...
            mundos_validos += 1  # Incrementa o contador de mundos válidos
            if mundo[1]:  # Se a posição [2,2] tiver um poço (index 1)...
                count_2_2 += 1  # Incrementa o contador de poços na posição [2,2]
   
    # Calcula a probabilidade de poço na posição [2,2] dividindo o número de poços pelo número total de mundos válidos
    prob_2_2 = count_2_2 / mundos_validos 
    
    return prob_2_2  # Retorna a probabilidade calculada

# Lista de probabilidades a priori de poço a serem testadas
probabilidades = [0.01, 0.2, 0.5, 0.8, 0.99]

# Lista que armazenará o tempo de execução para cada probabilidade
tempo_lista = []

# Itera sobre cada probabilidade a priori de poço
for i in probabilidades:
    inicio = time.time()  # Marca o tempo de início da simulação
    prob_2_2 = simular_poco_2_2(i)  # Executa a simulação para a probabilidade 'i'
    fim = time.time()  # Marca o tempo de fim da simulação
    tempo = fim - inicio  # Calcula o tempo total de execução
    tempo_lista.append(tempo)  # Armazena o tempo na lista

# Cria um gráfico do tempo de execução em função da probabilidade a priori de poço
plt.plot(probabilidades, tempo_lista)  
    
# Adiciona rótulo ao eixo X
plt.xlabel('Probabilidade a priori de poço')  

# Adiciona rótulo ao eixo Y
plt.ylabel('Tempo que demorou a correr a experiência [s]')  

# Exibe o gráfico
plt.show()  
