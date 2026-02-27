"""
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2,
o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha.
Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

3
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0

5.7
6.3
9.3

"""


def media_ponderada(medias):
    pesos = [2, 3, 5]
    notas = list(map(float, medias.split()))  # converte cada string da lista em float e depois salva na lista
    medias = [n*p for n, p in zip(notas, pesos)]  # multiplica as notas pelos pesos e salva na lista
    return round(sum(medias) / sum(pesos), 1)  # arredonda o float em uma casa decimal


x = int(input())
for media in range(x):
    nota = input()
    print(media_ponderada(nota))
