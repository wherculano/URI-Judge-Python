"""
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística
do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio
em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta.
Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times
em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor",
caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e
pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)".
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima.
Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

Exemplo de Entrada
3 2
1
2 3
1
3 1
2
Exemplo de Saída
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
3 grenais
Inter:2
Gremio:1
Empates:0
Inter venceu mais
"""
grenal = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
while True:
    inter, gremio = [int(gol) for gol in input().split()]
    if inter > gremio:
        vitorias_inter += 1
    elif gremio > inter:
        vitorias_gremio += 1
    else:
        empates += 1
    grenal += 1
    print("Novo grenal (1-sim 2-nao)")
    jogo = int(input())
    if jogo == 1:
        continue
    else:
        break

print("{} grenais".format(grenal))
print("Inter:{}".format(vitorias_inter))
print("Gremio:{}".format(vitorias_gremio))
print("Empates:{}".format(empates))

if vitorias_inter > vitorias_gremio:
    print("Inter venceu mais")
elif vitorias_inter < vitorias_gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")

