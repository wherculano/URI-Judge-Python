"""
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N].
A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor,mostrando esta informação.

Entrada
A primeira linha de entrada contem um único inteiro N (1 < N < 1000), indicando o número de elementos que deverão ser lidos em seguida para o vetor X[N] de inteiros.
A segunda linha contém cada um dos N valores, separados por um espaço. Vale lembrar que nenhuma entrada haverá números repetidos.
10
1 2 3 4 -5 6 7 8 9 10

Saída
A primeira linha apresenta a mensagem “Menor valor:” seguida de um espaço e do menor valor lido na entrada.
A segunda linha apresenta a mensagem “Posicao:” seguido de um espaço e da posição do vetor na qual se encontra o menor valor lido, lembrando que o vetor inicia na posição zero.
Menor valor: -5
Posicao: 4
"""

def menor_valor_e_posicao(vetor: list) -> tuple[int, int]:
    menor = vetor[0]
    menor_pos = vetor[0]
    for indice, num in enumerate(vetor):
        if num <= menor:
            menor = num
            menor_pos = indice
    return menor, menor_pos

if __name__ == "__main__":
    N = int(input())  # em python isso nao servirá para nada
    valores = list(map(int, input().split()))
    menor, posicao = menor_valor_e_posicao(valores)
    print(f"Menor valor: {menor}")
    print(f"Posicao: {posicao}")