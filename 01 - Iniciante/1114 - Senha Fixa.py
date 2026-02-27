"""
Escreva um programa que repita a leitura de uma senha até que ela seja válida.
Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida".
Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado.
Considere que a senha correta é o valor 2002. 

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.

Exemplo de Entrada	
2200
1020
2022
2002
Exemplo de Saída
Senha Invalida
Senha Invalida
Senha Invalida
Acesso Permitido
"""
senha = 2002
while True:
    while True:
        try:
            entrada = int(input())
            break
        except ValueError:
            print("Senha Invalida")
    if entrada == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
