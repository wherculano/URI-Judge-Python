"""
Leia um valor X. Coloque este valor na primeira posição de um vetor N[100].
Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior,
conforme o exemplo abaixo. Imprima o vetor N.

Entrada
A entrada contem um valor de dupla precisão com 4 casas decimais.
200.0000

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela
posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.

N[0] = 200.0000
N[1] = 100.0000
N[2] = 50.0000
N[3] = 25.0000
N[4] = 12.5000
...
"""
value = float(input())
n=[]
for i in range(100):
    n.append(value)
    print(f"N[{i}] = {n[i]:.4f}")
    value /= 2
