"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Saída
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""

i=0
j=1
cont=0

while i <= 2:
    for _ in range(3):
        if i == 0 or i == 1:
            print('I={:.0f} J={:.0f}'.format(i, j+i))
        elif cont == 10:
            i = 2
            print('I={:.0f} J={:.0f}'.format(i, j+i))
        else:
            print('I={:.1f} J={:.1f}'.format(i, j+i))
        j+=1
    i+=0.2
    j=1
    cont+=1
