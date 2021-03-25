"""
Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.

Exemplo de Entrada
6

Exemplo de Saída
1
2
3
6
"""


def divisores(n):
    """
    >>> divisores(6)
    1
    2
    3
    6
    """
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


N = int(input())
divisores(N)
