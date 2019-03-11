'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

    >>> converter_notas_e_moedas(576.73)
    NOTAS:
    5 nota(s) de R$ 100.00
    1 nota(s) de R$ 50.00
    1 nota(s) de R$ 20.00
    0 nota(s) de R$ 10.00
    1 nota(s) de R$ 5.00
    0 nota(s) de R$ 2.00
    MOEDAS:
    1 moeda(s) de R$ 1.00
    1 moeda(s) de R$ 0.50
    0 moeda(s) de R$ 0.25
    2 moeda(s) de R$ 0.10
    0 moeda(s) de R$ 0.05
    3 moeda(s) de R$ 0.01

    >>> converter_notas_e_moedas(4.00)
    NOTAS:
    0 nota(s) de R$ 100.00
    0 nota(s) de R$ 50.00
    0 nota(s) de R$ 20.00
    0 nota(s) de R$ 10.00
    0 nota(s) de R$ 5.00
    2 nota(s) de R$ 2.00
    MOEDAS:
    0 moeda(s) de R$ 1.00
    0 moeda(s) de R$ 0.50
    0 moeda(s) de R$ 0.25
    0 moeda(s) de R$ 0.10
    0 moeda(s) de R$ 0.05
    0 moeda(s) de R$ 0.01

    >>> converter_notas_e_moedas(91.01)
    NOTAS:
    0 nota(s) de R$ 100.00
    1 nota(s) de R$ 50.00
    2 nota(s) de R$ 20.00
    0 nota(s) de R$ 10.00
    0 nota(s) de R$ 5.00
    0 nota(s) de R$ 2.00
    MOEDAS:
    1 moeda(s) de R$ 1.00
    0 moeda(s) de R$ 0.50
    0 moeda(s) de R$ 0.25
    0 moeda(s) de R$ 0.10
    0 moeda(s) de R$ 0.05
    1 moeda(s) de R$ 0.01
'''


def converter_notas_e_moedas(valor):
    valor += 0.001
    notas = (100, 50, 20, 10, 5, 2)
    moedas = (1, 0.5, 0.25, 0.1, 0.05, 0.01)
    print('NOTAS:')
    for i in range(len(notas)):
        qt_notas = valor // notas[i]
        print('{} nota(s) de R$ {:.2f}'.format(int(qt_notas), notas[i]))
        valor %= notas[i]
    print('MOEDAS:')
    for i in range(len(moedas)):
        qt_moedas = valor // moedas[i]
        print('{} moeda(s) de R$ {:.2f}'.format(int(qt_moedas), moedas[i]))
        valor %= moedas[i]


N = float(input())
converter_notas_e_moedas(N)
