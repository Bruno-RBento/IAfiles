import copy, random

def mostra_tabuleiro(T):
    # IMPLEMENTAR
    simbolos = {1: "X", -1: "O", 0: " "}
    for i in range(3):
        print("-------------")
        print("|", end="")
        for j in range(3):
            print(f" {simbolos[T[i * 3 + j]]} |", end="")
        print()
    print("-------------")
    
    # devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T, a, jogador):
    aux= []
    aux = copy.copy(T)
    # aux fica com cópia do tabuleiro
    if(jogador == "MAX"):
        aux[a] = 1
    elif(jogador == "MIN"):
        aux[a] = -1
    # COMPLETAR
    return aux

# ------------------------------------------------------------------
def acoes(T):
    empty_places = []
    
    for i in range(9):
        if T[i] == 0:
            empty_places.append(i)
    return empty_places

def utilidade(T):
    
    # testa as linhas
    for i in range(3):
        if T[i * 3] == T[i * 3 + 1] ==  T[i * 3 + 2] == 1:
            return 1  # X ganhou
        elif T[i * 3] == T[i * 3 + 1] == T[i * 3 + 2] == -1:
            return -1
    
    # testa as colunas
    for i in range(3):
        if(T[i] == T[i+3] == T[i+6] == 1): 
            return 1
        elif(T[i] == T[i+3] ==  T[i+6] == -1):
            return -1
        
    
    # testa as diagonais
    if(T[0] == T[4] == T[8] == 1): 
        return 1
    elif(T[0] == T[4] == T[8] == -1):
        return -1
    # COMPLETAR
    # não é nodo folha ou dá empate

def estado_terminal(T):
    if(utilidade(T) == 0):
        return False
    else:
        return True
    # IMPLEMENTAR

def alfabeta(T, alfa, beta, jogador):
    if estado_terminal(T):
        return utilidade(T),-1,-1
    if jogador == 'MAX':
        v = -10
        ba=-1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, 'MIN')
            if v1 > v: # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            alfa = max(alfa, v)
            if v >= beta:
                break
        return v, ba, resultado(T, ba, 'MAX')
    else:
        v = 10
        ba=-1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MIN'), alfa, beta, 'MAX')
            if v1 < v: # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            alfa = max(alfa, v)
            if v >= beta:
                break
        return v, ba, resultado(T, ba, 'MIN')
        # COMPLETAR
        return()




tabuleiro =[0,-1,-1,0,-1,1,-1,-1,-1]
mostra_tabuleiro(tabuleiro)

print("-------------------\n ")
print("-------------------\n ")

novo_tabuleiro = resultado(tabuleiro, 3, "MIN")
mostra_tabuleiro(novo_tabuleiro)