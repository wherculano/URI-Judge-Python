"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos
 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre
 escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.

    >>> verifica_triangulos('7.0 5.0 7.0')
    TRIANGULO ACUTANGULO
    TRIANGULO ISOSCELES

    >>> verifica_triangulos('6.0 6.0 10.0')
    TRIANGULO OBTUSANGULO
    TRIANGULO ISOSCELES

    >>> verifica_triangulos('6.0 6.0 6.0')
    TRIANGULO ACUTANGULO
    TRIANGULO EQUILATERO

    >>> verifica_triangulos('5.0 7.0 2.0')
    NAO FORMA TRIANGULO

    >>> verifica_triangulos('6.0 8.0 10.0')
    TRIANGULO RETANGULO
"""


def verifica_triangulos(valores):
    a, b, c = list(map(float, valores.split()))
    if b > c and b > a:
        a, b = b, a
    elif c > b and c > a:
        a, c = c, a

    while a > 0 and b > 0 and c > 0:
        if a >= (b + c):
            print('NAO FORMA TRIANGULO')
            break
        if (a ** 2) == ((b ** 2) + (c ** 2)):
            print('TRIANGULO RETANGULO')
        if (a ** 2) > ((b ** 2) + (c ** 2)):
            print('TRIANGULO OBTUSANGULO')
        if (a ** 2) < ((b ** 2) + (c ** 2)):
            print('TRIANGULO ACUTANGULO')
        if a == b and b == c:
            print('TRIANGULO EQUILATERO')
        if (a == b and b != c) or (c == a and a != b) or (b == c and c != a):
            print('TRIANGULO ISOSCELES')
        break


n = input()
verifica_triangulos(n)
