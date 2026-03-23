"""
Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo,
indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso.
A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|----|----|
| 0 |   |   |   |   |   |   |   |   |   |   |    |    |
| 1 |   |   |   |   |   |   |   |   |   |   |    |    |
| 2 | X | X | X | X | X | X | X | X | X | X | X  | X  |
| 3 |   |   |   |   |   |   |   |   |   |   |    |    |
| 4 |   |   |   |   |   |   |   |   |   |   |    |    |
| 5 |   |   |   |   |   |   |   |   |   |   |    |    |
| 6 |   |   |   |   |   |   |   |   |   |   |    |    |
| 7 |   |   |   |   |   |   |   |   |   |   |    |    |
| 8 |   |   |   |   |   |   |   |   |   |   |    |    |
| 9 |   |   |   |   |   |   |   |   |   |   |    |    |
| 10|   |   |   |   |   |   |   |   |   |   |    |    |
| 11|   |   |   |   |   |   |   |   |   |   |    |    |

Entrada
A primeira linha de entrada contem um número L (0 ≤ L ≤ 11) indicando a linha que será considerada para operação.
A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os
elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz, sendo que a mesma é preenchida linha por linha, da linha 0 até a linha 11,
sempre da esquerda para a direita.
2
S
0.0
-3.5
2.5
4.1
...

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
12.6

"""
matriz = []

linha = int(input())
operacao = input().upper()

for _ in range(12):
    valores = []
    for _ in range(12):
        numero = float(input())
        valores.append(numero)
    matriz.append(valores)

linha_escolhida = matriz[linha]
total = sum(linha_escolhida)

match operacao:
    case 'S':
        print(f"{total:.1f}")
    case 'M':
        media = total/len(linha_escolhida)
        print(f"{media:.1f}")
    case _:
        print('Valor inválido')
