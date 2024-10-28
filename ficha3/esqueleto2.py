import copy
import random

# ------------------------------------------------------------------
def mostra_tabuleiro(T):
    # Exibe o tabuleiro de jogo da velha.
    for i, pos in enumerate(T):
        if pos == 0:
            print(" . ", end='')  # Espaço vazio
        elif pos == 1:
            print(" X ", end='')  # Jogador MAX (X)
        elif pos == -1:
            print(" O ", end='')  # Jogador MIN (O)
        
        # Imprime nova linha após cada 3 posições
        if i == 2 or i == 5 or i == 8:
            print("\n")

# ------------------------------------------------------------------
# Devolve a lista de ações (posições vazias) que se podem executar
def acoes(T):
    l = []
    for i, pos in enumerate(T):
        if pos == 0:  # Se a posição está vazia
            l.append(i)  # Adiciona a posição à lista de ações
    return l

# ------------------------------------------------------------------
# Devolve o estado que resulta de executar uma ação
def resultado(T, a, jog):
    aux = copy.copy(T)  # Cria uma cópia do tabuleiro original
    if aux[a] == 0:  # Se a posição está vazia
        if jog == "MAX":
            aux[a] = 1  # Jogador MAX (X)
        else:
            aux[a] = -1  # Jogador MIN (O)
    return aux

# ------------------------------------------------------------------
# Verifica se houve um vencedor
def utilidade(T):
    # Testa as linhas
    for i in (0, 3, 6):
        if T[i] == T[i + 1] == T[i + 2] != 0:  # Alinhamento
            return -1 if T[i] == -1 else 1  # Retorna -1 ou 1 dependendo do jogador
    
    # Testa as colunas
    for i in (0, 1, 2):
        if T[i] == T[i + 3] == T[i + 6] != 0:  # Alinhamento
            return -1 if T[i] == -1 else 1
    
    # Testa as diagonais
    if T[0] == T[4] == T[8] != 0:  # Diagonal principal
        return -1 if T[0] == -1 else 1
    if T[2] == T[4] == T[6] != 0:  # Diagonal secundária
        return -1 if T[2] == -1 else 1
    
    # Não é nodo folha ou dá empate
    return 0

# ------------------------------------------------------------------
# Devolve True se T é um estado terminal (fim do jogo)
def estado_terminal(T):
    # O jogo termina se há um vencedor ou se não há mais espaços
    return utilidade(T) in (1, -1) or 0 not in T

# ------------------------------------------------------------------
# Algoritmo Alpha-Beta para a escolha de jogadas
def alfabeta(T, alfa, beta, jog):
    if estado_terminal(T):  # Verifica se o estado é terminal
        return utilidade(T), -1, -1  # Retorna a utilidade, sem ação e estado
    
    if jog:  # Jogador MAX
        v = -10  # Inicializa o valor
        ba = -1  # Melhor ação
        for a in acoes(T):  # Para cada ação possível
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, False)
            if v1 > v:  # Guarda a melhor ação
                v = v1
                ba = a
            alfa = max(alfa, v)  # Atualiza alfa
            if v >= beta:  # Poda
                break
        return v, ba, resultado(T, ba, 'MAX')
    else:  # Jogador MIN
        v = 10  # Inicializa o valor
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MIN'), alfa, beta, True)
            if v1 < v:  # Guarda a melhor ação
                v = v1
                ba = a
            beta = min(beta, v)  # Atualiza beta
            if v <= alfa:  # Poda
                break
        return v, ba, resultado(T, ba, 'MIN')

# ------------------------------------------------------------------
def joga_max(T):
    v, a, e = alfabeta(T, -10, 10, True)
    print('MAX joga para', a)
    return e

# ------------------------------------------------------------------
def joga_min(T):
    v, a, e = alfabeta(T, 10, -10, False)
    print('MIN joga para:', a)
    return e

# ------------------------------------------------------------------
def jogo(p1, p2):
    # Cria um tabuleiro vazio
    T = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    mostra_tabuleiro(T)  # Mostra o tabuleiro inicial
    while acoes(T) != [] and not estado_terminal(T):  # Enquanto houver ações disponíveis
        T = p1(T)  # Jogador 1 faz a jogada
        mostra_tabuleiro(T)  # Mostra o tabuleiro após a jogada
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)  # Jogador 2 faz a jogada
            mostra_tabuleiro(T)  # Mostra o tabuleiro após a jogada

    # Fim do jogo, imprime o resultado
    if utilidade(T) == 1:
        print('Venceu o jog1')
    elif utilidade(T) == -1:
        print('Venceu o jog2')
    else:
        print('Empate')

# ------------------------------------------------------------------
# Jogador aleatório
def joga_rand(T):
    # Seleciona uma posição aleatória
    x = random.randint(0, 8)
    while True:
        if T[x] == 0:  # Se a posição está vazia
            print("Rand joga para", x)
            T[x] = -1  # Marca a jogada do jogador MIN
            break
    return T

# ------------------------------------------------------------------
# Main
# Para testar a função com diferentes jogadores
# deve ganhar sempre o max:
# jogo(joga_max, joga_rand) 
# devem empatar sempre:
jogo(joga_max, joga_min)
