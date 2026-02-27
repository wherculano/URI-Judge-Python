'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula:
MaiorAB  = (a + b + abs(a-b)) / 2

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

    >>> 7 14 106
    106 eh o maior

    >>> 217 14 6
    217 eh o maior
'''
def MaiorAB(x,y):
    num = (x + y + abs(x-y) ) // 2
    return num

a, b, c = map(int, input().strip().split())
print('{} eh o maior'.format(MaiorAB(a,MaiorAB(b,c))))
