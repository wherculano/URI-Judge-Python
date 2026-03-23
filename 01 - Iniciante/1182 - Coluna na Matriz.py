"""
Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação
que será realizada, e todos os elementos de uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso.
A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser considerados na operação.

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|----|----|
| 0 |   |   |   |   |   | X |   |   |   |   |    |    |
| 1 |   |   |   |   |   | X |   |   |   |   |    |    |
| 2 |   |   |   |   |   | X |   |   |   |   |    |    |
| 3 |   |   |   |   |   | X |   |   |   |   |    |    |
| 4 |   |   |   |   |   | X |   |   |   |   |    |    |
| 5 |   |   |   |   |   | X |   |   |   |   |    |    |
| 6 |   |   |   |   |   | X |   |   |   |   |    |    |
| 7 |   |   |   |   |   | X |   |   |   |   |    |    |
| 8 |   |   |   |   |   | X |   |   |   |   |    |    |
| 9 |   |   |   |   |   | X |   |   |   |   |    |    |
| 10|   |   |   |   |   | X |   |   |   |   |    |    |
| 11|   |   |   |   |   | X |   |   |   |   |    |    |

Entrada
A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação.
A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos
da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.
5
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
n_coluna = int(input())
operacao = input().upper()
matriz = []  # Se quiser otimizacao, criar a lista é desnecessario.
total = 0.0

for linha in range(12):
    valores = []
    for coluna in range(12):
        num = float(input())
        valores.append(num)
        if coluna == n_coluna:
            total += num
    matriz.append(valores)

match operacao:
    case 'S':
        print(f"{total:.1f}")
    case 'M':
        media = total/12
        print(f"{media:.1f}")
    case _:
        print('Valor inválido')
