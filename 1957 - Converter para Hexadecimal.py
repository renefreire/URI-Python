"""
1957 - Converter para Hexadecimal
Os dados armazenados no computador estão em binário. Uma forma econômica de ver estes números é usar a base 16
(hexadecimal).
Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em
hexadecimal.

Entrada
A entrada é um número inteiro positivo V na base 10 (1 ≤ V ≤ 2 x 10^9).

Saída
A saída é o mesmo número V na base 16 em uma única linha (não esqueça do caractere de fim-de-linha). Use letras
maiúsculas, conforme os exemplos.
"""

V = int(input())

r = V % 16
q = V//16
H = [r]
while q != 0:
    r = q % 16
    q = q // 16
    H.append(r)

for i in range(len(H)-1, -1, -1):
    if H[i] == 10:
        print("A", end="")
    elif H[i] == 11:
        print("B", end="")
    elif H[i] == 12:
        print("C", end="")
    elif H[i] == 13:
        print("D", end="")
    elif H[i] == 14:
        print("E", end="")
    elif H[i] == 15:
        print("F", end="")
    else:
        print("%d" % H[i], end="")

print("")
