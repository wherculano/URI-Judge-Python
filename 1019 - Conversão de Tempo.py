'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.


    >>> converter_segundos(556)
    0:9:16

    >>> converter_segundos(1)
    0:0:1

    >>> converter_segundos(140153)
    38:55:53
'''

def converter_segundos(tempo):
    """
    Recebe um inteiro que representa o tempo em segundos e retorna um string em formato de hora
    :param tempo: Tempo em segundos
    :return: hora:min:seg
    """
    hora = tempo // 3600
    minut = (tempo % 3600) // 60
    seg = (tempo % 3600) % 60
    return f'{hora}:{minut}:{seg}'


N = int(input())
print(converter_segundos(N))
