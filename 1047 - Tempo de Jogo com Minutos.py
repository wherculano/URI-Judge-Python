"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

7 8 9 10
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

7 7 7 7
O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

7 10 8 9
O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
"""


hr_inicial, min_inicial, hr_final, min_final = map(int, input().split(' '))
hr_total = min_total = 0

if (hr_final - hr_inicial == 1) and (min_inicial > min_final):
    min_total = 60 - min_inicial
    min_total += min_final
elif (hr_inicial == hr_final) and (min_inicial == min_final):
    hr_total = 24
elif (hr_inicial < hr_final) and (min_inicial < min_final):
    hr_total = hr_final - hr_inicial
    min_total = min_final - min_inicial
elif (hr_inicial < hr_final) and (min_inicial > min_final):
    hr_total = (hr_final - hr_inicial) - 1
    min_total = 60 - min_inicial
    min_total += min_final
elif(hr_inicial == hr_final) and (min_inicial < min_final):
    min_total = min_final - min_inicial
elif hr_inicial > hr_final:
    hr_total = (24 - hr_inicial) + hr_final
    min_total = min_final - min_inicial
    if min_inicial > min_final:
        hr_total -= 1
        min_total = (60 - min_inicial) + min_final

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hr_total, min_total))
