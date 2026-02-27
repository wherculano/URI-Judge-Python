"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em
branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

7 21 -14
-14
7
21

7
21
-14

-14 21 7
-14
7
21

-14
21
7
"""


lista = list(map(int, input().strip().split()))
for v in sorted(lista):
    print(v)
print()
for v in lista:
    print(v)
