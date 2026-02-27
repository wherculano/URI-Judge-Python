'''
Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo,
com um espaço em branco antes e depois da igualdade.
    >>> 5
    >>> 6
    >>> 7
    >>> 8
    DIFERENCA = -26

    >>> 0
    >>> 0
    >>> 7
    >>> 8
    DIFERENCA = -56

    >>> 5
    >>> 6
    >>> -7
    >>> 8
    DIFERENCA = 86
'''
A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = (A*B) - (C*D)
print('DIFERENCA = {}'.format(DIFERENCA))
