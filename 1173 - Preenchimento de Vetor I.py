"""
Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10].
Em cada posição subsequente, coloque o dobro do valor da posição anterior.
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente.
Mostre o vetor em seguida.

Entrada
A entrada contém um valor inteiro (V<=50).

Saída
Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i.
O primeiro número do vetor N (N[0]) irá receber o valor de V.

"""


def inserir_valor(valor):
    """
    >>> inserir_valor(1)
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    >>> inserir_valor(3)
    [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]
    """
    n = [0] * 10
    n[0] = valor
    for i in range(1, len(n)):
        n[i] = 2 * n[i - 1]
    return n


v = int(input())
n = inserir_valor(v)
for i, v in enumerate(n):
    print('N[{}] = {}'.format(i, v))
