'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a variável MEDIA conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade.
Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

    >>> 5.0
    >>> 6.0
    >>> 7.0
    MEDIA = 6.3

    >>> 5.0
    >>> 10.0
    >>> 10.0
    MEDIA = 9.0

    >>> 10.0
    >>> 10.0
    >>> 5.0
    MEDIA = 7.5
'''
A = float(input())
B = float(input())
C = float(input())
p1 = 2
p2 = 3
p3 = 5
MEDIA = ((A*p1)+(B*p2)+(C*p3))/ (p1+p2+p3)
print('MEDIA = {:.1f}'.format(MEDIA))
