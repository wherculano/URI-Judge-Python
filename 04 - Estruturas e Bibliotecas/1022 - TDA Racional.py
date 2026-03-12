"""
Tipo de Dado Abstrato Racional: é um tipo de dado abstrato números racionais (frações).
A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação.
Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere,
número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a
resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)

Entrada
A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste
que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).
4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4

Saída
A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor.
No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade.
10/8 = 5/4
-2/8 = -1/4
12/18 = 2/3
4/6 = 2/3

"""
def mdc(x: int, y: int):
    """
    Calcula o Máximo Divisor Comum entre dois números utilizando o algoritmo de Euclides.
    Enquanto y for diferente de zero, substitui x por y e y por x mod y.
    Por exemplo, se x for 12 e y for 18, a sequência de operações seria:
        x = 18, y = 12, (12 mod 18 é 12)
        x = 12, y = 6 ,(18 mod 12 é 6)
        x = 6, y = 0, (12 mod 6 é 0)
    Quando y se torna zero, x é o máximo divisor comum, que é retornado.
    """
    while y:
        x, y = y, x % y
    return x


def simplificar(numerador: int, denominador: int):
    """
    Simplifica uma fração dividindo o numerador e o denominador pelo máximo divisor comum.
    """
    divisor = mdc(numerador, denominador)
    return numerador // divisor, denominador // divisor


def main():
    operacoes = {
        '+': lambda n1, d1, n2, d2: (((n1 * d2) + (n2 * d1)), (d1 * d2)),
        '-': lambda n1, d1, n2, d2: (((n1 * d2) - (n2 * d1)), (d1 * d2)),
        '*': lambda n1, d1, n2, d2: ((n1 * n2), (d1 * d2)),
        '/': lambda n1, d1, n2, d2: ((n1 * d2), (n2 * d1))
    }
    n = int(input())
    for _ in range(n):
        n1,_,d1,op,n2,_,d2 = input().split()
        n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
        numerador, denominador = operacoes[op](n1, d1, n2, d2)
        numerador_simplificado, denominador_simplificado = simplificar(numerador, denominador)
        print(f"{numerador}/{denominador} = {numerador_simplificado}/{denominador_simplificado}")

if __name__ == "__main__":
    main()