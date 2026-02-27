'''
Leia 4 valores inteiros A, B, C e D.
A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D,
ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

    >>> verify('5 6 7 8')
    'Valores nao aceitos'

    >>> verify('2 3 2 6')
    'Valores aceitos'
'''


def verify(numbers):
    a, b, c, d = map(int, numbers.strip().split(' '))
    return 'Valores aceitos' if (b > c) and (d > a) and ((c+d) > (a+b)) and (c > 0 and d > 0) and (a % 2 == 0) else 'Valores nao aceitos'


num = input()
print(verify(num))
