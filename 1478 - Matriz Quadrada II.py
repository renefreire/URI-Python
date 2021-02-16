"""
1478 - Matriz Quadrada II
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa
a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas.
O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. (os valores das matrizes devem
ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada
linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.
"""

N = int(input())

while N != 0:
    for i in range(N):
        for j in range(N):
            if j == 0:
                print("%3d" % (abs(i - j) + 1), end="")
            else:
                print("%4d" % (abs(i - j) + 1), end="")
        print("\n", end="")
    print("\n", end="")
    N = int(input())
