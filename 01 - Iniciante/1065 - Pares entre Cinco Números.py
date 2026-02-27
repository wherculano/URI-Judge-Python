"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

7
-5
6
-4
12

3 valores pares

"""

positivos = [int(input()) for _ in range(5)]
total = [par for par in positivos if par % 2 == 0]
print('{} valores pares'.format(len(total)))
