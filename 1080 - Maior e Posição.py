"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

2
113
45
34565
6
...
8


34565
4

"""

maior = 0
lista = dict()

for i in range(100):
    valor = int(input())
    if valor > maior:
        maior = valor
        lista[valor] = i  # adicionará o valor como key  do dict e guardará a posição como value

print(maior)
print(lista[maior]+1)  # imprime o valor da posição (se indice 0 = posição 1, por isso a soma de 1 ao fim)
