"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X,
um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

8

9
11
13
15
17
19

"""

impares = int(input())

for i in range(impares, impares+12):  # se quero 6 números, então fui até o dobro (12)
    if i % 2 != 0:
        print(i)
