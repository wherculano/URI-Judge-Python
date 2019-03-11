'''
Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem,
ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa.
Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em velocidade_media_em_km/h).
Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas)
e o segundo é a velocidade média durante a mesma (em velocidade_media_em_km/h).

Saída
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

    >>> 10
    >>> 85
    70.833

    >>> 2
    >>> 92
    15.333

    >>> 22
    >>> 67
    122.833
'''
tempo_gasto_em_horas = int(input())
velocidade_media_em_km = int(input())
km_por_litro = 12
quantidade_em_littros = (tempo_gasto_em_horas * velocidade_media_em_km) / km_por_litro
print('{:.3f}'.format(quantidade_em_littros))