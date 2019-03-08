'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C.
Em seguida, calcule e mostre: 
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. 
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser
apresentado com 3 dígitos após o ponto decimal.

    >>> 3.0 4.0 5.2
    TRIANGULO: 7.800
    CIRCULO: 84.949
    TRAPEZIO: 18.200
    QUADRADO: 16.000
    RETANGULO: 12.000

    >>> 12.7 10.4 15.2
    TRIANGULO: 96.520
    CIRCULO: 725.833
    TRAPEZIO: 175.560
    QUADRADO: 108.160
    RETANGULO: 132.080
'''
t = input().split(' ')
a = float(t[0])
b = float(t[1])
c = float(t[2])

tri = (a*c)/2
cir = 3.14159 * (c**2)
trap = ((a + b) * c) / 2
quad = b * b
ret = a * b


print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}'.format(tri,cir))
print('TRAPEZIO: {:.3f}\nQUADRADO: {:.3f}'.format(trap, quad))
print('RETANGULO: {:.3f}'.format(ret))
