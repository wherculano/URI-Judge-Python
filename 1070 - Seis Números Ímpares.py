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
cont = 0
while cont <= 11:
    if impares % 2 != 0:
        print(impares)
    cont += 1
    impares += 1
