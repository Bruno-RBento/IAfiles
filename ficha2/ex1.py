
#1 numeros impares entre 10 e 34
def use_range(a, b):
    for i in range(a, b, 2):
        print(i)
        
#use_range(11, 34)
      
def use_range2(a, b):
    for i in range(a, b):
        if i % 2 != 0:
            print(i)

#use_range2(11, 34)


#2 Escreva um programa que peça ao utilizador um número inteiro positivo
# menor que 100 e mostre no ecrã quantas dezenas e quantas unidades tem o
# número lido.

def dezenas_unidades():
    num = int(input("Digite um número inteiro positivo menor que 100: "))
    if num < 100:
        dezenas = num // 10
        unidades = num % 10
        if(dezenas == 0):
            print("Unidades: %d" % unidades)
        else:
            print("Dezenas: %d" % dezenas)
            print("Unidades: %d" % unidades)
        
#dezenas_unidades()


#3 

#ler do teclado
def ler_teclado():
    nome = input("Digite o texto: ")
    print("O texto %s" % nome)
    return nome

#ler_teclado()

def criarFile(a, b):
    f = open(a, "w")
    f.write(b)
    f.close()
    
#criarFile("texto.txt", "Hello World")

def conta_vogais(a):
    vogais = "aeiou"
    count = 0
    for i in a.lower():
        if i in vogais:
            count += 1
    print(count)
    return count

#conta_vogais("hello world")

def allPrograms():
    a = ler_teclado()

    b = ler_teclado()
    aV = conta_vogais(a)
    bV = conta_vogais(b)
    if(aV >= bV):
        criarFile("texto.txt", a)
    elif(aV < bV):
        criarFile("texto.txt", b)

#allPrograms()

#4 ler lista de inteiros positivos no teclado se negativo para de ler
def ler_lista():
    lista = []
    while True:
        num = int(input("Digite um número inteiro positivo: "))
        if num < 0:
            break
        lista.append(num)
    print(lista)
    
#ler_lista()

# numerso que esta em ambas as listas

def lista_comum(a,b):
    lista = []
    for i in a:
        if i in b:
            lista.append(i)
    print(lista)
    
lista_comum([1,2,3,4,5], [3,4,5,6,7])


#5 matriz 2x2
def matriz2x2_input(matrix1, matrix2):
    npMatrix1 = np.array(matrix1)
    npMatrix2 = np.array(matrix2)
    print(npMatrix1)
    print(npMatrix2)
    #o produto elemento a elemento
    #print(npMatrix1 * npMatrix2)
    
    #produto matricial
    #print(np.dot(npMatrix1, npMatrix2))
    


#d6 menu
def mostrarMenu():
    print("\nMenu:")
    print("1. Inserir nova UC e nota")
    print("2. Alterar nota de uma UC")
    print("3. Mostrar todas as UCs e notas")
    print("4. Mostrar nota média")
    print("5. Sair")
    

def menu():
    usc = {}
    while True:
        mostrarMenu()
        op = int(input("Escolha uma opção: "))
        if op == 1:
            uc = input("Digite o nome da UC: ")
            nota = float(input("Digite a nota: "))
            usc[uc] = nota
        elif op == 2:#how this works?
            uc = input("Digite o nome da UC: ")
            nota = float(input("Digite a nota: "))
            usc[uc] = nota
        elif op == 3:
            print(usc)
        elif op == 4:
            print(np.mean(list(usc.values())))
        elif op == 5:
            break

#menu()

#7
def lerFrase():
    frase = input("Digite uma frase: ")
    return frase

def letrasNas2(frase1, frase2):
    #verificar se a letra esta nas duas frases e colocar em uma lista
    lista = []
    for i in frase1:
            if i in frase2 and i not in lista:
                lista.append(i)
            
    print(lista)
    
def letrasSoNa1(frase1, frase2):
    #verificar se a letra esta na frase1 e nao esta na frase2
    lista = []
    for i in frase1:
            if i not in frase2 and i not in lista:
                lista.append(i)
    print(lista);

#fix this
def letrasSimultaneamente(frase1, frase2):
    for i in frase1:
        for j in frase2:
            if i == j:
                print(i)
                break
