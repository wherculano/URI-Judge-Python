"""
Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral.
O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]).
Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1 ou 2)
indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida 
a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

Entrada
O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve ser lido um valor inteiro X.
O programa deve parar quando o valor lido para este X for igual a 2.

Saída
Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas, deve ser impressa a mensagem 
“media = ” seguido do valor do cálculo.

Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada novamente se o valor da entrada
padrão para X for menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.
-3.5
nota invalida
3.5
11.0
nota invalida
10.0
media = 6.75
novo calculo (1-sim 2-nao)
4
novo calculo (1-sim 2-nao)
1
8.0
9.0
media = 8.50
novo calculo (1-sim 2-nao)
2
"""

def calcula_media():
    sair = False
    while not sair:
        notas = []
        while len(notas) < 2:
            try:
                nota = float(input())
            except ValueError:
                print("nota invalida")
                continue
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("nota invalida")
        media = sum(notas) / len(notas)
        print(f"media = {media:.2f}")
        while True:
            print("novo calculo (1-sim 2-nao)")
            op = input()
            if op == "1":
                break
            elif op == "2":
                sair = True
                break

if __name__ == "__main__":
    calcula_media()