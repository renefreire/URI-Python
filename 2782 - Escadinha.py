"""
2782 - Escadinha
Dizemos que uma sequência de números é uma escadinha, se a diferença entre números
consecutivos é sempre a mesma. Por exemplo, “2, 3, 4, 5” e “10, 7, 4” são escadinhas.
Note que qualquer sequência com apenas um ou dois números também é uma escadinha! Neste
problema estamos procurando escadinhas em uma sequência maior de números. Dada uma
sequência de números, queremos determinar quantas escadinhas existem. Mas só estamos
interessados em escadinhas tão longas quanto possível. Por isso, se uma escadinha é um
pedaço de outra, consideramos somente a maior. Por exemplo, na sequência “1, 1, 1, 3, 5,
4, 8, 12” temos 4 escadinhas diferentes: “1, 1, 1”, “1, 3, 5”, “5, 4” e “4, 8, 12”.

Entrada
A primeira linha da entra contém um inteiro N (1 ≤ N ≤ 1000) indicando o tamanho da
sequência de números. A segunda linha contém N inteiros definindo a sequência. O valor
dos números da sequência está entre −106 e 106 inclusive.

Saída
Imprima uma linha contendo um inteiro representando quantas escadinhas existem na
sequência.
"""

N = int(input())

S = [int(k) for k in input().split()]

escadinha = 1
if len(S) <= 2:
    print(escadinha)
else:
    dif = []
    for n in range(N-1):
        dif.append(S[n] - S[n+1])

    for n in range(N-2):
        if dif[n] != dif[n+1]:
            escadinha += 1

    print(escadinha)
