import pyAgrum as gum  # Importa a biblioteca pyAgrum, que é usada para trabalhar com redes bayesianas

# Função para mostrar o resultado de uma consulta (query) com base em evidências observadas
def mostra(d, q):
    # "d" são as observações (evidências) e "q" é a variável da qual queremos inferir a probabilidade
    global ie  # "ie" é um objeto de inferência global
    ie.setEvidence(d)  # Define as evidências observadas
    ie.makeInference()  # Realiza a inferência com base nas evidências
    print(ie.posterior(q))  # Mostra a distribuição posterior da variável "q"

# Função que define as probabilidades de o Monty abrir cada porta, 
# sabendo quem é o convidado (guest) e onde está o prêmio (prize)
def prob_monty(guest, prize):
    p = []  # Lista para armazenar as probabilidades de o Monty abrir cada porta
    for monty in ['A', 'B', 'C']:  # Itera sobre as 3 portas possíveis
        if guest == monty or prize == monty:
            # Se o Monty escolher a mesma porta que o convidado ou a porta onde está o prêmio,
            # ele não abrirá essa porta, então a probabilidade é 0
            p.append(0)
        elif guest != monty and prize != monty and guest != prize:
            # Se o convidado e o prêmio escolheram portas diferentes de Monty, o Monty abrirá essa porta com certeza
            p.append(1)
        elif guest != monty and prize != monty and guest == prize:
            # Se o convidado escolheu a porta onde está o prêmio, o Monty tem 50% de chance de abrir uma das outras
            p.append(0.5)

    return p  # Retorna a lista de probabilidades

# Criação da rede bayesiana para o problema de Monty Hall
bn = gum.BayesNet('MontyHall')

# Adiciona variáveis (nodos) à rede: guest (convidado), prize (prêmio), monty (porta escolhida por Monty)
guest = bn.add(gum.LabelizedVariable('guest', 'guest', ['A', 'B', 'C']))
prize = bn.add(gum.LabelizedVariable('prize', 'prize', ['A', 'B', 'C']))
monty = bn.add(gum.LabelizedVariable('monty', 'monty', ['A', 'B', 'C']))

# Define as dependências entre as variáveis (arestas da rede bayesiana)
bn.addArc(guest, monty)  # A escolha do Monty depende da escolha do convidado
bn.addArc(prize, monty)  # A escolha do Monty também depende da porta onde está o prêmio

# Define as tabelas de probabilidade para cada variável na rede
# Probabilidade de o convidado escolher uma porta aleatoriamente
bn.cpt(guest)[{}] = [1./3, 1./3, 1./3]
# Probabilidade de o prêmio estar em qualquer porta (é igualmente provável estar em A, B ou C)
bn.cpt(prize)[{}] = [1./3, 1./3, 1./3]
# A tabela de probabilidades para Monty depende tanto da escolha do convidado quanto da localização do prêmio
for i in ['A', 'B', 'C']:
    for j in ['A', 'B', 'C']:
        bn.cpt(monty)[{'guest': i, 'prize': j}] = prob_monty(i, j)

# Usa inferência atrasada (lazy propagation) para a rede bayesiana
ie = gum.LazyPropagation(bn)

# Exemplo de consulta: 
# Mostra a probabilidade de Monty escolher várias portas, dado que o convidado escolheu 'B' e o prêmio está em 'A'
mostra({'guest': 'B', 'prize': 'A'}, 'monty')

# Probabilidade de vencer o prêmio se o convidado escolheu a porta 'A' e Monty abriu a porta 'B' (sem trocar de porta)
mostra({'guest': 'A', 'monty': 'B'}, 'prize')

# Probabilidade de vencer o prêmio se o convidado escolheu a porta 'C' e Monty abriu a porta 'B' (após trocar de porta)
mostra({'guest': 'C', 'monty': 'B'}, 'prize')
