"""
Esqueleto para o exercício 1 da ficha 3.
IA -- UBI
"""
import copy, random

# ------------------------------------------------------------------
def mostra_tabuleiro(T):
    # IMPLEMENTAR

# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T):
    # IMPLEMENTAR

# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T, a, jogador):
    # aux fica com cópia do tabuleiro
    aux = copy.copy(T)
    # COMPLETAR
    return aux

# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador
def utilidade(T):
    # testa as linhas
    # COMPLETAR
    # testa as colunas
    # COMPLETAR
    # testa as diagonais
    # COMPLETAR
    # não é nodo folha ou dá empate
    return 0

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
def estado_terminal(T):
    # IMPLEMENTAR


# ------------------------------------------------------------------
# algoritmo da wikipedia (fail-soft version adaptada)
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
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
        # COMPLETAR

# ------------------------------------------------------------------
def joga_max(T):
    # passamos o tabuleiro e valores iniciais para alfa e beta
    v, a, e = alfabeta(T, -10, 10, 'MAX')
    print('MAX joga para ',a)
    return e

# ------------------------------------------------------------------
def joga_min(T):
    # IMPLEMENTAR

# ------------------------------------------------------------------
def jogo(p1, p2):
    # cria tabuleiro vazio
    T = [0,0,0,0,0,0,0,0,0]
    # podemos partir de um estado mais "avançado"
    #T = [1,-1,0,0,-1,0,1,0,0]
    mostra_tabuleiro(T)
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)
        mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print('Venceu o MAX')
    elif utilidade(T) == -1:
        print('Venceu o MIN')
    else:
        print('Empate')

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):
    x = random.randint(0,8)
    # COMPLETAR
    return T

# ------------------------------------------------------------------
# main

# deve ganhar (quase) sempre o max:
jogo(joga_max,joga_rand)

# devem empatar sempre:
#jogo(joga_max,joga_min)


