import pyAgrum as gum  # Importa a biblioteca pyAgrum, que é usada para redes bayesianas

# Função para mostrar o resultado de uma consulta (query) com base em observações
def mostra(d, q):
    # "d" são as observações (evidências), e "q" é a variável para a qual queremos inferir a probabilidade
    global ie  # "ie" é o objeto global de inferência
    ie.setEvidence(d)  # Define as evidências observadas
    ie.makeInference()  # Realiza a inferência com base nas evidências
    print(ie.posterior(q))  # Exibe a distribuição posterior da variável consultada

# Criação da rede bayesiana (BayesNet) para o problema "Relva Molhada"
bn = gum.BayesNet('RelvaMolhada')

# Adiciona variáveis (nodos) à rede: chuva (se está a chover), aspersor (se está ligado), e relva (se está molhada)
chuva = bn.add(gum.LabelizedVariable('chuva', 'chuva', ['F', 'V']))  # Variável booleano: 'F' (falso) e 'V' (verdadeiro)
aspersor = bn.add(gum.LabelizedVariable('aspersor', 'aspersor ligado', ['F', 'V']))  # Aspersor pode estar 'F' ou 'V'
relva = bn.add(gum.LabelizedVariable('relva', 'relva molhada', ['F', 'V']))  # Relva pode estar molhada ou não

# Adiciona as dependências (arestas) entre as variáveis:
# A variável aspersor depende da chuva (aspersor é ligado ou não dependendo se está a chover)
bn.addArc(chuva, aspersor)

# A variável relva depende tanto da chuva quanto do aspersor (relva pode estar molhada pela chuva ou pelo aspersor)
bn.addArc(aspersor, relva)
bn.addArc(chuva, relva)

# Definição das tabelas de probabilidades condicionais (CPT - Conditional Probability Table) para cada variável

# Probabilidade de estar a chover:
# Existe uma probabilidade de 80% de não estar a chover ('F') e 20% de estar a chover ('V')
bn.cpt(chuva)[{}] = [0.8, 0.2]

# Probabilidade do aspersor estar ligado, condicionado ao estado da chuva:
# - Se não estiver a chover ('chuva' = F), há uma chance de 40% do aspersor estar ligado
bn.cpt(aspersor)[{'chuva': 0}] = [0.6, 0.4]

# - Se estiver a chover ('chuva' = V), quase sempre o aspersor está desligado (99% desligado)
bn.cpt(aspersor)[{'chuva': 1}] = [0.99, 0.01]

# Probabilidade de a relva estar molhada, condicionado ao estado da chuva e do aspersor:
# - Se não estiver a chover e o aspersor estiver desligado, a relva certamente não estará molhada (100% seco)
bn.cpt(relva)[{'chuva': 0, 'aspersor': 0}] = [1, 0]

# - Se estiver a chover e o aspersor estiver desligado, há 80% de chance da relva estar molhada (somente pela chuva)
bn.cpt(relva)[{'chuva': 1, 'aspersor': 0}] = [0.2, 0.8]

# - Se não estiver a chover mas o aspersor estiver ligado, há 90% de chance da relva estar molhada
bn.cpt(relva)[{'chuva': 0, 'aspersor': 1}] = [0.1, 0.9]

# - Se tanto estiver a chover quanto o aspersor estiver ligado, a relva está quase certamente molhada (99%)
bn.cpt(relva)[{'chuva': 1, 'aspersor': 1}] = [0.01, 0.99]

# Cria o objeto de inferência usando propagação preguiçosa (lazy propagation) para a rede bayesiana
ie = gum.LazyPropagation(bn)

# Consultas específicas:

# 3a: Qual é a probabilidade de a relva não estar molhada?
# Aqui não há evidências fornecidas, então queremos a probabilidade da variável 'relva' sem qualquer observação
mostra({}, 'relva')  # Resultado: distribuição das probabilidades para 'relva'

# 3b: Qual é a probabilidade de estar a chover, dado que observamos a relva molhada?
# Neste caso, estamos a observar que a relva está molhada ('relva' = 'V') e queremos inferir se está a chover
mostra({'relva': 'V'}, 'chuva')  # Resultado: probabilidade de 'chuva' (F ou V), dado que a relva está molhada

# 3c: Qual é a probabilidade de o aspersor estar desligado, dado que a relva não está molhada e não está a chover?
# Aqui observamos que a relva não está molhada ('relva' = 'F') e que não está a chover ('chuva' = 'F').
# Queremos inferir se o aspersor estava desligado.
mostra({'relva': 'F', 'chuva': 'F'}, 'aspersor')  # Resultado: probabilidade de o 'aspersor' estar ligado ou não
