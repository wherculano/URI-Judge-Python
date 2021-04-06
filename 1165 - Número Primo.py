"""
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste.
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada.
Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”,
de acordo com a especificação fornecida.

Exemplo de Entrada
3
8
51
7

Exemplo de Saída
8 nao eh primo
51 nao eh primo
7 eh primo
"""

def eh_primo(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return f'%d nao eh primo' % x
    return f'%d eh primo' % x


n = int(input())
for i in range(n):
    x = int(input())
    print(eh_primo(x))
