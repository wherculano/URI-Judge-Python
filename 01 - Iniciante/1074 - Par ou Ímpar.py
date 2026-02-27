"""
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido,
mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE)
ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL),
pois por definição zero é par, seu programa deverá imprimir apenas NULL.

Entrada
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser
maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.


>>> n = 4
>>> par_ou_impar(-5)
ODD NEGATIVE
>>> par_ou_impar(0)
NULL
>>> par_ou_impar(3)
ODD POSITIVE
>>> par_ou_impar(-4)
EVEN NEGATIVE

"""


def par_ou_impar(n):
    if n == 0:
        print('NULL')
    elif n % 2 == 0:
        if n > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if n > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')


x = int(input())
for i in range(x):
    n = int(input())
    par_ou_impar(n)
