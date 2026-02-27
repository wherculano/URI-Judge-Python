"""
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano.
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
                    Q2 | Q1
                    --------
                    Q3 | Q4

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

    >>> coord('4.5 -2.2')
    'Q4'

    >>> coord('0.1 0.1')
    'Q1'

    >>> coord('0.0 0.0')
    'Origem'
"""

x, y = map(float, input().strip().split(' '))

if x > 0 and y > 0:
    print('Q1')
elif x > 0 > y:
    print('Q4')
elif x < 0 < y:
    print('Q2')
elif x <0 and y <0:
    print('Q3')
elif x > 0 or x < 0 and y == 0:
    print('Eixo X')
elif x == 0 and y > 0 or y < 0:
    print('Eixo Y')
elif x == 0 and y == 0:
    print('Origem')

# def coord(numbers):
#     x, y = map(float, numbers.strip().split(' '))
#     pontos = {x > 0 and y > 0: 'Q1', x > 0 > y: 'Q4', x < 0 < y: 'Q2', x < 0 and y < 0: 'Q3',
#               x > 0 > x and y == 0: 'Eixo X', x == 0 and y > 0 > y: 'Eixo Y', x == 0 and y == 0: 'Origem'}
#
#     for ponto, saida in pontos.items():
#         if ponto:
#             return saida
#
# num = input()
# coord(num)