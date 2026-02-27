""""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores
fornecidos na entrada que deverá caber em um inteiro.

x=6
y=-5
5

x=15
y=12
13

x=12
y=12
0

"""

x = int(input())
y = int(input())
soma = 0

for impar in range(min(x,y)+1, max(x,y)):
    if impar % 2 != 0:
        soma += impar

print(soma)
