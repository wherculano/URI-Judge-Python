"""
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo.
O último dado, que não entrará nos cálculos, contém o valor de idade negativa.
Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada:
A entrada contém um número indeterminado de inteiros.
A entrada será encerrada quando um valor negativo for lido.

Saída:
A saída contém um valor correspondente à média de idade dos indivíduos.
A média deve ser impressa com dois dígitos após o ponto decimal.

Exemplo de Entrada
34
56
44
23
-2

Exemplo de Saída
39.25
"""

soma = media = cont = 0
while True:
    age = int(input())
    if age < 0:
        break
    else:
        soma += age
        cont += 1
try:
    media = soma / cont
except ZeroDivisionError:
    print('0.00')
print('{:.2f}'.format(media))
