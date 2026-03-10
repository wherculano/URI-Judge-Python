"""
Solicitaram para que você construisse um programa simples de criptografia.
Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: 
letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida.
Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII.
Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”.
O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”.
Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar.
As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.
4
Texto #3
abcABC1
vxpdylY .ph
vv.xwfxo.fd

Saída
Para cada entrada, deve-se apresentar a mensagem criptografada.
3# rvzgV
1FECedc
ks. \n{frzx
gi.r{hyz-xx

>>> criptografia("Texto #3")
'3# rvzgV'
>>> criptografia("abcABC1")
'1FECedc'
>>> criptografia("vxpdylY .ph")
'ks. \\n{frzx'
>>> criptografia("vv.xwfxo.fd")
'gi.r{hyz-xx'
"""
def criptografia(texto: str) -> str:
    # Primeira passada: deslocar letras 3 posições para a direita (ou nao)
    chars = [chr(ord(char) + 3) if char.isalpha() else char for char in texto]

    # Segunda passada: inverter a linha (texto)
    chars.reverse()

    # Terceira passada: deslocar caracteres da metade em diante 1 posição para a esquerda
    metade = len(chars) // 2
    for i in range(metade, len(chars)):
        chars[i] = chr(ord(chars[i]) - 1)
    return ''.join(chars)


def main():
    vezes = int(input())
    for _ in range(vezes):
        texto = input()
        print(criptografia(texto))


if __name__ == "__main__":
    main()
