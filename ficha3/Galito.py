
import copy, random
# ------------------------------------------------------------------
def mostra_tabuleiro(T):
    print("")
    j = 0
    symbols = {-1: "O", 0: " ", 1: "X"}
    for i in range(1,len(T)+1):
        if i % 3 == 1:
                    print("  ",end="")
        print(" " + symbols[T[i-1]] + " ", end="") 
        if i % 3 == 0:
            if j < 2:
                j +=1
                print("")
                print("  ____________")
        if i % 3 != 0:
            print("|", end="")
    print("")
    print("-----------------------------------------")

# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T): 
    mostra = False
    if(mostra):
        print("")
        print("Possible Moves: ")

    P =[]
    for i in range(0,len(T)):
        if T[i] == 0:
            P.append(i)
    if(mostra):
        print(P)

    return P
# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T, a, jogador):
    aux = T
    aux = copy.copy(T) # para não modificar o original
    if jogador == 'MAX':
        aux[a] = 1
    else:
        aux[a] = -1
    return aux

# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador. retorna 1 se o MAX ganha, -1 se o MIN ganha e 0 se ninguém ganha
def utilidade(T):
    """for i in range(0,5,3):
        if T[i] == T[i+1] == T[i+2] != 0:
            return T[i]
        if T[i] == T[i+3] == T[i+6] != 0:
            return T[i]
        if T[0] == T[4] == T[8] != 0:
            return T[i]
        if T[2] == T[4] == T[6] != 0:
            return T[2]
    return 0"""
    # Rows
    for i in range(0, 9, 3):
        if T[i] == T[i+1] == T[i+2] != 0:
            return T[i]
    # Columns
    for i in range(3):
        if T[i] == T[i+3] == T[i+6] != 0:
            return T[i]
    # Diagonals
    if T[0] == T[4] == T[8] != 0:
        return T[0]
    if T[2] == T[4] == T[6] != 0:
        return T[2]
    
    return 0


# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
def estado_terminal(T):
    if utilidade(T) != 0:
        return True
    else:
        return False


# ------------------------------------------------------------------
# algoritmo da wikipedia (fail-soft version adaptada)
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta(T, alfa, beta, jogador):
    if estado_terminal(T):
        return utilidade(T),-1,-1
    if jogador == 'MAX':
        v = -100  
        ba=-1   # best action
        for a in acoes(T):  
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, 'MIN') #v1 é o valor, ac é a ação e es é o estado
            if v1 > v: # guardo a ação que corresponde ao melhor
                v = v1 
                ba = a # best action
            alfa = max(alfa, v) # atualizo o alfa
            if v >= beta: # se o valor for maior ou igual ao beta, corto
                break
        return v, ba, resultado(T, ba, 'MAX')
    else:
        v = 100
        ba=-1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MIN'), alfa, beta, 'MAX')
            if v1 < v:
                v = v1
                ba = a
            beta = min(beta, v)
            if v <= alfa:
                break
        return v, ba, resultado(T, ba, 'MIN')
        

# ------------------------------------------------------------------
def joga_max(T):
    # passamos o tabuleiro e valores iniciais para alfa e beta
    v, a, e = alfabeta(T, -10, 10, 'MAX')
    print('MAX joga para ', a)
    return e

# ------------------------------------------------------------------
def joga_min(T):
    v, a, e = alfabeta(T, -10, 10, 'MIN')
    print('MIN joga para ', a)
    return e

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):
    P = acoes(T)    
    a = random.choice(P)
    print("RAND joga para ", a)
    T[a] = -1
    
    return T

# ------------------------------------------------------------------
def jogo(p1, p2):
    # cria tabuleiro vazio
    T = [0,0,0,0,0,0,0,0,0]
    #T = [0, -1, 1, 0, -1, 0, 1, -1, 0]
    mostra_tabuleiro(T)
    
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)  # MAX plays
        mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)  # MIN plays
            mostra_tabuleiro(T)

    # fim
    if utilidade(T) == 1:
        return 'MAX'
    elif utilidade(T) == -1:
        return 'MIN'
    else:
        return 'DRAW'

# ------------------------------------------------------------------
def iterate():
    jogos_count = 0
    Max_win = 0
    Min_win = 0
    Draw = 0

    while jogos_count < 100:
        result = jogo(joga_max, joga_rand)
        if result == 'MAX':
            Max_win += 1
        elif result == 'MIN':
            Min_win += 1
        else:
            Draw += 1

        jogos_count += 1

    print('Final Results after 100 games:')
    print('Max wins: ', Max_win)
    print('Min wins: ', Min_win)
    print('Draws: ', Draw)

# Execute the iteration
iterate()


