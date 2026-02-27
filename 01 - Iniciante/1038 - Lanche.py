"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.

CODIGO    ESPECIFICACAO      PRECO
  1       Cachorro Quente   R$ 4.00
  2       X-Salada          R$ 4.50
  3       X-Bacon           R$ 5.00
  4       Torrada Simples   R$ 2.00
  5       Refrigerante      R$ 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código
e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem 'Total: R$ ' seguido pelo valor a ser pago,
com 2 casas após o ponto decimal.

    >>> pedido('3 2')
    'Total: R$ 10.00'

    >>> pedido('4 3')
    'Total: R$ 6.00'

    >>> pedido('2 3')
    'Total: R$ 13.50'
"""

prod = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}


def pedido(numbers):
    n1, n2 = map(int, numbers.strip().split(' '))
    cod, val = prod.get(n1), n2
    tot = cod * val
    return 'Total: R$ {:.2f}'.format(tot)


num = input()
print(pedido(num))
