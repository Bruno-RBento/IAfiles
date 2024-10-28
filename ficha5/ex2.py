import pyAgrum as gum  # Importa a biblioteca pyAgrum, que é usada para redes bayesianas

# Função para mostrar o resultado de uma consulta (query) com base nas observações
def mostra(d, q):
    # "d" são as evidências observadas, e "q" é a variável para a qual queremos inferir a probabilidade
    global ie  # "ie" é o objeto global de inferência
    ie.setEvidence(d)  # Define as evidências na inferência (passa as observações)
    ie.makeInference()  # Realiza a inferência com base nas evidências
    print(ie.posterior(q))  # Exibe a distribuição posterior da variável consultada

# Função que calcula a probabilidade de Monty abrir cada uma das portas, dado o convidado e o prêmio
def prob_monty(guest, prize):
    # "guest" é a porta escolhida pelo convidado, e "prize" é a porta onde o prêmio está
    p = []  # Lista para armazenar as probabilidades de Monty abrir cada porta
    for monty in ['A', 'B', 'C', 'D']:  # Itera sobre todas as 4 portas (A, B, C, D)
        if guest == monty or prize == monty:
            # Monty não abre a porta escolhida pelo convidado, nem a porta onde está o prêmio
            p.append(0)
        else:
            # Se Monty pode abrir a porta, atribuímos 1 (inicialmente todas as portas abertas são igualmente prováveis)
            p.append(1)
    total = sum(p)  # Soma as probabilidades para normalizar (pois Monty pode abrir mais de uma porta)
    return [x / total for x in p]  # Retorna as probabilidades normalizadas para que a soma seja 1

# Criação da rede bayesiana (BayesNet) para o problema de Monty Hall com 4 portas
bn = gum.BayesNet('MontyHall')

# Adiciona variáveis (nodos) à rede: guest (convidado), prize (prêmio), monty (porta que Monty escolhe abrir)
guest = bn.add(gum.LabelizedVariable('guest', 'guest', ['A', 'B', 'C', 'D']))  # Convidado escolhe uma porta
prize = bn.add(gum.LabelizedVariable('prize', 'prize', ['A', 'B', 'C', 'D']))  # Prêmio está em uma das portas
monty = bn.add(gum.LabelizedVariable('monty', 'monty', ['A', 'B', 'C', 'D']))  # Monty escolhe uma porta para abrir

# Adiciona as dependências (arestas) entre as variáveis: Monty depende do convidado e do prêmio
bn.addArc(guest, monty)  # Monty depende da porta escolhida pelo convidado
bn.addArc(prize, monty)  # Monty depende da porta onde está o prêmio

# Define as tabelas de probabilidades condicionais (CPT - Conditional Probability Table) para as variáveis
# O convidado escolhe uma porta aleatoriamente, então as probabilidades são uniformes (1/4 para cada porta)
bn.cpt(guest)[{}] = [1./4, 1./4, 1./4, 1./4]

# A porta onde está o prêmio também é escolhida aleatoriamente (probabilidade uniforme)
bn.cpt(prize)[{}] = [1./4, 1./4, 1./4, 1./4]

# A escolha de Monty depende das escolhas do convidado e da localização do prêmio
# Para cada combinação de portas (convidado e prêmio), Monty escolhe a porta com base nas probabilidades calculadas
for i in ['A', 'B', 'C', 'D']:  # Itera sobre as portas do convidado
    for j in ['A', 'B', 'C', 'D']:  # Itera sobre as portas do prêmio
        bn.cpt(monty)[{'guest': i, 'prize': j}] = prob_monty(i, j)  # Define a CPT de Monty para essa combinação

# Configura o método de inferência utilizando propagação preguiçosa (lazy propagation)
ie = gum.LazyPropagation(bn)

# Exemplos de inferências

# Exemplo: Qual a probabilidade de Monty escolher cada porta, dado que o convidado escolheu a porta B e o prêmio está na porta A?
mostra({'guest': 'B', 'prize': 'A'}, 'monty')

# Probabilidade de vencer o prêmio se o convidado escolheu a porta B e Monty abriu a porta C, sem trocar de porta
mostra({'guest': 'B', 'monty': 'C'}, 'prize')

# Probabilidade de vencer o prêmio se o convidado escolheu a porta B e Monty abriu a porta C, considerando a troca de porta
mostra({'guest': 'B', 'monty': 'C'}, 'prize')
