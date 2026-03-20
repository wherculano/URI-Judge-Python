"""
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares.
Só que o tamanho de cada um dos dois vetores é de 5 posições.
Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos.
Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro 
os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.
1
3
4
-4
2
3
8
2
5
-7
54
76
789
23
98

Saída
Imprima a saída conforme o exemplo abaixo.
par[0] = 4
par[1] = -4
par[2] = 2
par[3] = 8
par[4] = 2
impar[0] = 1
impar[1] = 3
impar[2] = 3
impar[3] = 5
impar[4] = -7
impar[0] = 789
impar[1] = 23
par[0] = 54
par[1] = 76
par[2] = 98
"""

#################################################
# Resolvi assim primeiro para entender a logica #
#################################################
pares = []
impares = []
for indice in range(15):
    valor = int(input())
    if valor % 2 == 0:
        if len(pares) < 5:
            pares.append(valor)
        else:
            for indice_par, valor_par in enumerate(pares):
                print(f"par[{indice_par}] = {valor_par}")
            pares.clear()
            pares.append(valor)
    else:
        if len(impares) < 5:
            impares.append(valor)
        else:
            for indice_impar, valor_impar in enumerate(impares):
                print(f"impar[{indice_impar}] = {valor_impar}") 
            impares.clear()
            impares.append(valor)

if impares:
    for indice_impar, valor_impar in enumerate(impares):
        print(f"impar[{indice_impar}] = {valor_impar}") 
if pares:
    for indice_par, valor_par in enumerate(pares):
        print(f"par[{indice_par}] = {valor_par}")


#####################################
# Agora uma abordagem "mais senior" #
#####################################
def processar_numero(valor, lista, nome):
    """Adiciona valor à lista; imprime e limpa se atingir 5 elementos"""
    lista.append(valor)
    if len(lista) == 5:
        for i, v in enumerate(lista):
            print(f"{nome}[{i}] = {v}")
        lista.clear()

pares = []
impares = []

for _ in range(15):
    valor = int(input())
    if valor % 2 == 0:
        processar_numero(valor, pares, "par")
    else:
        processar_numero(valor, impares, "impar")

# Imprime o que sobrou
for i, v in enumerate(impares):
    print(f"impar[{i}] = {v}")
for i, v in enumerate(pares):
    print(f"par[{i}] = {v}")
