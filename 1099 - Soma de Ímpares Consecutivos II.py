"""
1099 - Soma de Ímpares Consecutivos II
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois
inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste
consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
"""

N = int(input())
soma = 0
for i in range(N):
    X, Y = [int(x) for x in input().split()]
    if X > Y:
        aux = X
        X = Y
        Y = aux
    for j in range(X+1, Y):
        if j % 2 != 0:
            soma += j
    print(soma)
    soma = 0
