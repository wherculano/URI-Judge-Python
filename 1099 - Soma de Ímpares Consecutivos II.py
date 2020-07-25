"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8

Exemplo de Saída
0
11
5
0
0
0
12
"""

def soma(a, b):
	if a > b:
		a, b = b, a
	return sum([i for i in range(a+1,b) if i%2 != 0])

n = int(input())
for i in range(n):
	x,y = list(map(int, input().split()))
	print(soma(x, y))
