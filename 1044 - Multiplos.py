"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

6 24
Sao Multiplos

6 25
Nao sao Multiplos
"""

A, B = list(map(int, input().split()))
print('Sao Multiplos' if (B % A == 0 or A % B == 0) else 'Nao sao Multiplos')
