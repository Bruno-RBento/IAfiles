import copy  # Importa a biblioteca copy para fazer cópias do tabuleiro
import random  # Importa a biblioteca random para gerar jogadas aleatórias
# ------------------------------------------------------------------
# Função para mostrar o estado atual do tabuleiro
def mostra_tabuleiro(T):
    for i, pos in enumerate(T):
        # Imprime " . " se a posição estiver vazia
        if pos == 0:
            print(" . ", end= '')
        # Imprime " X " se for uma jogada do jogador MAX
        elif pos == 1:
            print(" X ", end= '')
        # Imprime " O " se for uma jogada do jogador MIN
        elif pos == -1:
            print(" O ", end= '')
        # Controla a formatação para quebrar as linhas após cada 4 posições
        if i == 3:
            print("\n")
        elif i == 7:
            print("\n")
        elif i == 11:
            print("\n")
# ------------------------------------------------------------------
# Função que devolve uma lista de ações possíveis no tabuleiro
# Ações possíveis são posições vazias (0) nas últimas 4 posições (índices 8, 9, 10 e 11)
def acoes(T):
    l = []  # Lista para armazenar ações válidas
    for i, pos in enumerate(T):
        if (i == 8 or i == 9 or i == 10 or i == 11) and pos == 0:
            l.append(i)
    return l  # Retorna as posições disponíveis
# ------------------------------------------------------------------
# Função que devolve o estado resultante após uma jogada
def resultado(T, a, jog):
    aux = copy.copy(T)  # Cria uma cópia do tabuleiro
    if aux[a] == 0:  # Se a posição estiver vazia
        # Se for a vez do jogador MAX, coloca 1 na posição
        if jog == "MAX":
            aux[a] = 1
        # Se for a vez do jogador MIN, coloca -1 na posição
        else:
            aux[a] = -1
    return aux  # Retorna o novo estado do tabuleiro
# ------------------------------------------------------------------
# Função para calcular a utilidade do estado (se alguém venceu)
def utilidade(T):
    # Testa as linhas (0-2, 4-6, 8-10)
    for i in (0, 4, 8):
        if (T[i] == T[i + 1] == T[i + 2] != 0) or (T[i + 1] == T[i + 2] == T[i + 3] != 0):
            if T[i] == -1:
                return -1  # Vitória do jogador MIN
            elif T[i] == 1:
                return 1  # Vitória do jogador MAX
    # Testa as colunas (0,1,2,3) comparando os elementos de cada coluna
    for i in (0, 1, 2, 3):
        if T[i] == T[i + 4] == T[i + 8] != 0:
            if T[i] == -1:
                return -1  # Vitória do jogador MIN
            elif T[i] == 1:
                return 1  # Vitória do jogador MAX
    # Testa as diagonais
    if (T[0] == T[5] == T[10] != 0) or (T[1] == T[6] == T[11] != 0) or (T[2] == T[5] == T[8] != 0) or (T[3] == T[6] == T[9] != 0):
        if T[0] == -1 or T[1] == -1 or T[2] == -1 or T[3] == -1:
            return -1  # Vitória do jogador MIN
        elif T[0] == 1 or T[1] == 1 or T[2] == 1 or T[3] == 1:
            return 1  # Vitória do jogador MAX
    # Se não há vitória, devolve 0 (empate ou jogo ainda em andamento)
    return 0
# ------------------------------------------------------------------
# Função que verifica se o estado do tabuleiro é terminal (fim de jogo)
def estado_terminal(T):
    if utilidade(T) == 1 or utilidade(T) == -1:  # Se há um vencedor
        return True
    if 0 not in T:  # Se não há mais espaços vazios, o jogo empatou
        return True
    return False  # Caso contrário, o jogo continua
# ------------------------------------------------------------------
# Algoritmo de poda Alpha-Beta (retirado da Wikipedia)
# Ele devolve o valor do estado, a melhor ação e o estado resultante
def alfabeta(T, alfa, beta, jog):
    if estado_terminal(T):  # Se o estado é terminal, devolve a utilidade
        return utilidade(T), -1, -1
    if jog:  # Se é a vez do MAX
        v = -10  # Valor inicial (mínimo possível para o MAX)
        ba = -1  # Melhor ação inicial
        for a in acoes(T):  # Para cada ação possível
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, False)  # Chamada recursiva para MIN
            if v1 > v:  # Se encontrou um valor melhor
                v = v1
                ba = a  # Atualiza a melhor ação
            alfa = max(alfa, v)  # Atualiza alfa (poda)
            if v >= beta:  # Se o valor ultrapassa beta, poda o resto
                break
        return v, ba, resultado(T, ba, 'MAX')  # Devolve o valor, a ação e o estado resultante
    else:  # Se é a vez do MIN
        v = 10  # Valor inicial (máximo possível para o MIN)
        ba = -1  # Melhor ação inicial
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MIN'), alfa, beta, True)  # Chamada recursiva para MAX
            if v1 < v:
                v = v1
                ba = a  # Atualiza a melhor ação
            beta = min(beta, v)  # Atualiza beta (poda)
            if v <= alfa:  # Se o valor ultrapassa alfa, poda o resto
                break
        return v, ba, resultado(T, ba, 'MIN')  # Devolve o valor, a ação e o estado resultante
# ------------------------------------------------------------------
# Função para o jogador MAX jogar
def joga_max(T):
    v, a, e = alfabeta(T, -10, 10, True)  # Chama o algoritmo Alpha-Beta
    print('MAX joga para ', a)  # Exibe a ação escolhida
    return e  # Retorna o estado resultante
# ------------------------------------------------------------------
# Função para o jogador MIN jogar
def joga_min(T):
    v, a, e = alfabeta(T, 10, -10, False)  # Chama o algoritmo Alpha-Beta
    print('MIN joga para:', a)  # Exibe a ação escolhida
    return e  # Retorna o estado resultante
# ------------------------------------------------------------------
# Função que controla o jogo entre dois jogadores (MAX e MIN)
def jogo(p1, p2):
    # Cria um tabuleiro vazio
    T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mostra_tabuleiro(T)  # Mostra o tabuleiro inicial
    # Loop do jogo até não haver mais ações ou o estado ser terminal
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)  # Jogador 1 (MAX) joga
        mostra_tabuleiro(T)  # Mostra o tabuleiro
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)  # Jogador 2 (MIN) joga
            mostra_tabuleiro(T)  # Mostra o tabuleiro
    # Fim do jogo, verifica quem venceu ou se houve empate
    if utilidade(T) == 1:
        print('Venceu o jog1')
    elif utilidade(T) == -1:
        print('Venceu o jog2')
    else:
        print('Empate')
# ------------------------------------------------------------------
# Jogador aleatório que joga em uma posição vazia
def joga_rand(T):
    x = random.randint(0, 8)  # Escolhe uma posição aleatória
    while True:
        if T[x] == 0:  # Se a posição estiver vazia
            print("Rand joga para", x)  # Exibe a jogada
            T[x] = -1  # Preenche a posição com -1 (MIN)
            break
    return T  # Retorna o novo estado do tabuleiro
# ------------------------------------------------------------------
# Função principal que inicia o jogo
# Deve ganhar sempre o jogador MAX:
jogo(joga_max, joga_rand)
# Devem empatar sempre
