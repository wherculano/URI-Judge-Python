"""
6+9=15 parece ok. Mas como pode estar certo 4+6=2?

Veja só. Mofiz trabalhou duro durante seu curso de Eletrônica Digital, mas quando lhe foi solicitado que implementasse um somador de 32 bits como exame
no laboratório, ele acabou fazendo algum erro na parte de projeto. Depois de vasculhar seu projeto por uma hora e meia, ele encontrou seu erro. 
Ele estava fazendo soma de bits, mas seu carregador de bit (carry) sempre apresentava como saída o valor zero. Portanto,

4  = 00000000 00000000 00000000 00000100
+6 = 00000000 00000000 00000000 00000110
----------------------------------------
2  = 00000000 00000000 00000000 00000010


Claro que já é uma boa coisa ele finalmente ter encontrado o seu erro, mas isso foi muito tarde. Considerando seu esforço durante o curso,
o instrutor deu a ele mais uma chance: Mofiz teria que escrever um programa eficiente que pegaria 2 valores decimais de 32 bits sem sinal como entrada
e deveria produzir um número de 32 bits sem sinal como saída, ou seja, somando do mesmo modo como o circuito faz.

Entrada
Em cada linha de entrada haverá um par de inteiros separado por um único espaço. A entrada termina com EOF.
4 6
6 9

Saída
Para cada linha de entrada, o programa deverá fornecer uma linha de saída, que é o valor após somar dois números no modo “Mofiz”.
2
15
"""


import sys

def mofiz_sum_easiest_way() -> None:
    """
    Objective: Calculate the sum of two integers in the "Mofiz" way, which is essentially a bitwise XOR operation.
    """
    for line in sys.stdin:
        n1, n2 = map(int, line.split())
        print(n1 ^ n2)


def mofiz_sum_hard_way() -> None:
    """
    Objective: Calculate the sum of two integers in the "Mofiz" way by manually performing bitwise addition without using built-in operators.
    """
    from itertools import zip_longest
    for line in sys.stdin:
        n1, n2 = map(int, line.split())
    
        n1_bits = bin(n1)[2:]
        n2_bits = bin(n2)[2:]
    
        result_bits = []
    
        for bit_1, bit_2 in zip_longest(reversed(n1_bits), reversed(n2_bits), fillvalue='0'):
            s = int(bit_1) + int(bit_2)
            result_bits.append(str(s % 2))
    
        result = int(''.join(reversed(result_bits)), 2)
    
        print(result)

if __name__ == "__main__":
    mofiz_sum_easiest_way()
    mofiz_sum_hard_way()