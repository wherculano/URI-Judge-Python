"""
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci.
Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores.
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada:
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída:
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco.
Não deve haver espaço após o último valor.

Exemplo de Entrada
5
Exemplo de Saída
0 1 1 2 3
"""

first = 0
second = 1
fib = [first, second]
num = int(input())
for n in range(2, num):
    next_num = second + first
    first = second
    second = next_num
    fib.append(next_num)
print(' '.join([str(i) for i in fib]))

