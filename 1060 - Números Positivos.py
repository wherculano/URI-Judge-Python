"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
 A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

    7
    -5
    6
    -3.4
    4.6
    12
    4 valores positivos
"""

positivos = 0

for _ in range(6):
    n = float(input())
    if n > 0:
        positivos += 1

print('{} valores positivos'.format(positivos))
