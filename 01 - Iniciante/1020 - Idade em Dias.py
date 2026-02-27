'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere os anos com 365 dias e os meses com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

    >>> converter_dias_em_anos(400)
    1 ano(s)
    1 mes(es)
    5 dia(s)

    >>> converter_dias_em_anos(800)
    2 ano(s)
    2 mes(es)
    10 dia(s)

    >>> converter_dias_em_anos(30)
    0 ano(s)
    1 mes(es)
    0 dia(s)
'''


def converter_dias_em_anos(valor):
    """
    Recebe um valor inteiro representando os dias e retorna uma string contendo o ano, mes e dias que o inteiro representa.
    :param valor: dias
    :return: ano, meses e dias
    """
    ano = valor // 365
    meses = (valor % 365) // 30
    dias = (valor % 365) % 30
    print('{} ano(s)'.format(ano))
    print('{} mes(es)'.format(meses))
    print('{} dia(s)'.format(dias))


N = int(input())
converter_dias_em_anos(N)
