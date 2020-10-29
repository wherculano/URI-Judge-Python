"""
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A para cada i com os valores
(0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos.
Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.

Exemplo de Entrada
3 2
3 -1 0 -2 2
Exemplo de Saída
7
7
"""
A = list(map(int, input().split()))
N = 1
soma = 0
while A[N] <= 0:
    if A[N] <= 0:
        N += 1
    if A[N] > 0:
        break
for x in range(A[N]):
    soma += A[0] + x
print('{}'.format(soma))

