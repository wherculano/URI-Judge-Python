"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.
Imprima sempre o final de linha após cada mensagem.

    >>> bhaskara('10.0 20.1 5.1')
    R1 = -0.29788
    R2 = -1.71212

    >>> bhaskara('0.0 20.0 5.0')
    Impossivel calcular

    >>> bhaskara('10.3 203.0 5.0')
    R1 = -0.02466
    R2 = -19.68408

    >>> bhaskara('10.0 3.0 5.0')
    Impossivel calcular
"""


def bhaskara(numbers):
    a, b, c = map(float, numbers.strip().split(' '))
    delta = pow(b, 2) - 4 * a * c
    if a == 0 or delta < 0:
        print('Impossivel calcular')
    else:
        try:
            x1 = (-b + pow(delta, 0.5)) / (2 * a)
            x2 = (-b - pow(delta, 0.5)) / (2 * a)
            print('R1 = {:.5f}'.format(x1))
            print('R2 = {:.5f}'.format(x2))
        except:
            print('Impossivel calcular')


n = input()
bhaskara(n)
