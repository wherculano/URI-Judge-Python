"""
Faça um programa que leia as notas referentes às duas avaliações de um aluno.
Calcule e imprima a média semestral.
Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]).
Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos.
O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo.
O valor deve ser apresentado com duas casas após o ponto decimal.

Exemplo de Entrada
-3.5
3.5
11.0
10.0

Exemplo de Saída
nota invalida
nota invalida
media = 6.75
"""

while True:
    try:
        n1 = float(input())
        if n1 < 0 or n1 > 10:
            print("nota invalida")
        else:
            break
    except ValueError:
        print("nota invalida")
while True:
    try:
        n2 = float(input())
        if n2 < 0 or n2 > 10:
            print("nota invalida")
        else:
            break
    except ValueError:
        print("nota invalida")

media = (n1+n2)/2
print("media = {:.2f}".format(media))
