"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
 quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

-5
0
-3
-4
12

3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)

"""

inteiros = [int(input()) for _ in range(5)]
pares = impares = positivos = negativos = 0


def par_ou_impar(n):
    global pares
    global impares
    if n % 2 == 0:
        pares += 1
        return pares
    else:
        impares += 1
        return impares


for n in inteiros:
    if n >= 0:
        par_ou_impar(n)
        if n != 0:
            positivos += 1
    else:
        negativos += 1
        par_ou_impar(n)

print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivos))
print('{} valor(es) negativo(s)'.format(negativos))
