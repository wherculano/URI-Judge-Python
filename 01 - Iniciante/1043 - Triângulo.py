"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro
do triângulo e apresente a mensagem:
Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

    >>> verifica_triangulo('6.0 4.0 2.0')
    Area = 10.0

    >>> verifica_triangulo('6.0 4.0 2.1')
    Perimetro = 12.1
"""


def verifica_triangulo(valores):
    x, y, z = list(map(float, valores.split()))
    if ((x + y) > z) and ((x + z) > y) and ((y + z) > x):
        perim = x + y + z
        print('Perimetro = {:.1f}'.format(perim))
    else:
        area = ((x + y) / 2) * z
        print('Area = {:.1f}'.format(area))


n = input()

verifica_triangulo(n)
