"""
Faça um programa que leia um vetor N[20]. 
Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc.,
até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.
0
-5
...
63
230

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.
N[0] = 230
N[1] = 63
...
N[18] = -5
N[19] = 0
"""
vetor = []
for i in range(20):
    while True:
        try:
            vetor.append(int(input()))
            break
        except ValueError:
            continue

for i in range(len(vetor)//2):
    vetor[i], vetor[-1-i] = vetor[-1-i], vetor[i]

for i, valor in enumerate(vetor):
    print(f"N[{i}] = {valor}")
