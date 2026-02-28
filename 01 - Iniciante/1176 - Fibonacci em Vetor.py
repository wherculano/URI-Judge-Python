"""
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido.
Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele.
Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste.
Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.
3
0
4
2

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.
Fib(0) = 0
Fib(4) = 3
Fib(2) = 1
"""
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041]

times = int(input())
fib = [0, 1]
for _ in range(times):
    n = int(input())
    if 0 <= n <= 60:
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
    print(f"Fib({n}) = {fib[n]}")
