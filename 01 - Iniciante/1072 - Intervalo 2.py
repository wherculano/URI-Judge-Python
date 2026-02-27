"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).


Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.


4
14
123
10
-25

2 in
2 out

"""

x = int(input())
_in = _out = 0
for num in range(x):
    n = int(input())
    if 0 <= n <= 20:
        _in += 1
    else:
        _out += 1

print('{} in'.format(_in))
print('{} out'.format(_out))
