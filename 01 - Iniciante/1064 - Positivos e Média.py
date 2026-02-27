"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar
a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a
média dos valores positivos digitados.

7
-5
6
-3.4
4.6
12

4 valores positivos
7.4

"""

positivos = [float(input()) for _ in range(6)]
total_positivos = 0
soma_dos_positivos = 0

for n in positivos:
    if n > 0:
        total_positivos += 1
        soma_dos_positivos += n

print('{} valores positivos'.format(total_positivos))
print('{:.1f}'.format(soma_dos_positivos / total_positivos))
