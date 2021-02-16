"""
1142 - PUM
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na
execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
"""

N = int(input())

for i in range(N):
    a = 4*i + 1
    b = a + 1
    c = a + 2
    print(a, b, c, "PUM")
