"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
    Salário	Percentual de Reajuste
        0 - 400.00          15%
        400.01 - 800.00     12%
        800.01 - 1200.00    10%
        1200.01 - 2000.00   7%
        Acima de 2000.00    4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice
reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho,
conforme exemplo abaixo.

    >>> novo_sal(400.00)
    Novo salario: 460.00
    Reajuste ganho: 60.00
    Em percentual: 15 %

    >>> novo_sal(800.01)
    Novo salario: 880.01
    Reajuste ganho: 80.00
    Em percentual: 10 %

    >>> novo_sal(2000.00)
    Novo salario: 2140.00
    Reajuste ganho: 140.00
    Em percentual: 7 %
"""


def novo_sal(sal):
    if 0 <= sal <= 400.00:
        tax = 15
    elif 400.00 < sal <= 800.00:
        tax = 12
    elif 800.00 < sal <= 1200.00:
        tax = 10
    elif 1200.00 < sal <= 2000.00:
        tax = 7
    elif sal > 2000.00:
        tax = 4
    novo_salario = (tax/100) * sal
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(sal+novo_salario, novo_salario, tax))


salario = float(input())
novo_sal(salario)
