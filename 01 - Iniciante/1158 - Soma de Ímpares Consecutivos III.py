"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y.
Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar.

Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.

Exemplo de Entrada
2
4 3
11 2

Exemplo de Saída
21
24
"""


n = int(input())
for _ in range(n):
    soma = 0
    x, y = list(map(int, input().split()))
    for _ in range(y * 2):
        if x % 2 != 0:
            soma += x
            x += 1
        else:
            x += 1
    print(soma)

