"""
Ler um valor N.
Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.

Entrada:
4
Saída:
24
"""


def fatorial(n):
    """
    >>> fatorial(5)
    120
    >>> fatorial(4)
    24
    """
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


if __name__ == '__main__':
    n = int(input())
    print(fatorial(n))
