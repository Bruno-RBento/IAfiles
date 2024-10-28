import copy
import random

# ------------------------------------------------------------------
def mostra_tabuleiro(T):
    for i, pos in enumerate(T):
        if pos == 0:
            print(" . ", end= '')
        elif pos == 1:
            print(" X ", end= '')
        elif pos == -1:
            print(" O ", end= '')
        if i == 2:
            print("\n")
        elif i == 5:
            print("\n")
        elif i == 8:
            print("\n")


def acoes(T):
    l = []
    for i, pos in enumerate(T):
        if pos == 0:
            l.append(i)
    return l

def resultado(T,a,jog):
    aux = copy.copy(T)
    if aux[a] == 0:
        if jog == "MAX":
             aux[a] = 1
        else:
            aux[a] = -1
    return aux

def utilidade(T):
    # testa as linhas
    for i in (0,3,6):
         if T[i] == T[i + 1] == T[i + 2] != 0:
              if T[i] == -1:
                   return -1
              elif T[i] == 1:
                   return 1
    # testa as colunas
    for i in (0, 1, 2):
         if T[i] == T[i+3] == T[i+6] != 0:
              if T[i] == -1:
                   return -1
              elif T[i] == 1:
                   return 1
	# testa as diagonais
    for i in (0, 2):
        if T[i] == T[4] == T[i+6] != 0:
             if T[i] == -1:
                 return -1
             elif T[i] == 1:
                 return 1
	# não é nodo folha ou dá empate
    return 0

t = [-1, 0, 0, 1, -1, 1, -1, 0, -1]
mostra_tabuleiro(t)
print(acoes(t))
# print(mostra_tabuleiro(resultado(t, 4, "MAX")))
print(utilidade(t))




def alfabeta(T,alfa,beta,jog):
	if estado_terminal(T):
		return utilidade(T),-1,-1
	if jog:
		v = -10
		ba=-1
		for a in acoes(T):
			v1,ac,es = alfabeta(resultado(T,a,'MAX'),alfa,beta,False)
			if v1 > v: # guardo a ação que corresponde ao melhor
				v = v1
				ba=a
			alfa = max(alfa,v)
			if v >= beta:
				break
		return v,ba,resultado(T,ba,'MAX')
	else:
		v = 10
		ba=-1
		for a in acoes(T):
			v1,ac,es = alfabeta(resultado(T,a,'MIN'),alfa,beta,True)
			if v1 < v:
				v = v1
				ba=a
			beta = min(beta,v)
			if v <= alfa:
				break
		return v,ba,resultado(T,ba,'MIN')
     



def alfabeta(T,alfa,beta,jog):
    if estado_terminal(T):
         return utilidade(T),-1,-1
    if jog:
        v = -10
        ba=-1
        for a in acoes(T):
            v1,ac,es = alfabeta(resultado(T,a,'MAX'),alfa,beta,False)
            if v1 > v: # guardo a ação que corresponde ao melhor
                v = v1
                ba=a
            alfa = max(alfa,v)
            if v >= beta:
                 break
            return v,ba,resultado(T,ba,'MAX')
        else:
             v = 10
             ba= -1
             for a in acoes(T):
                  v1,ac,es = alfabeta(resultado(T,a,'MIN'),alfa,beta,True)
                  if v1 < v:
                       v = v1
                       ba = a
                  beta = min(beta,v)
                  if v <= alfa:
                       break
                  return v, ba, resultado(T,ba,'MIN')