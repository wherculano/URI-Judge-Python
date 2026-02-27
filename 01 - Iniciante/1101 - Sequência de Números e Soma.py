"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior
e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N.
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada
5 2
6 3
5 0

Exemplo de Saída
2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""

while True:
    valores = [int(i) for i in input().split()]

    m = max(valores)
    n = min(valores)

    if m <= 0 or n <= 0:
        break

    soma = 0
    mensagem = ''
    for i in range(n, m+1):
        soma += i
        mensagem += str(i)+" "
    print('{}Sum={}'.format(mensagem, soma))
