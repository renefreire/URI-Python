"""
1837 - Prefácio
Desenvolva um programa que calcule o quociente e o resto da divisão de dois números inteiros, pode ser? Lembre que o
quociente e o resto da divisão de um inteiro a por um inteiro não-nulo b são respectivamente os únicos inteiros q e r
tais que 0 ≤ r < |b| e:
a = b × q + r
Caso você não saiba, o teorema que garante a existência e a unicidade dos inteiros q e r é conhecido como ‘Teorema da
Divisão Euclidiana’ ou ‘Algoritmo da Divisão’.

Entrada
A entrada é composta por dois números inteiros a e b (-1.000 ≤ a, b < 1.000).

Saída
Imprima o quociente q seguido pelo resto r da divisão de a por b.
"""

a, b = [int(x) for x in input().split()]

q = a // b
r = a % b
if r < 0:
    if q >= 0:
        q = q + 1
    else:
        if a > b:
            q = q + 1
        elif a < b:
            q = q - 1
    r = a - b*q

print(q, r)
