"""
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N.
Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal,
ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Exemplo de Entrada
3
3 -2
-8 0
0 8

Exemplo de Saída
-1.5
divisao impossivel
0.0
"""

cont = int(input())
for i in range(cont):
    x, y = list(map(float, input().split()))
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print('divisao impossivel')


