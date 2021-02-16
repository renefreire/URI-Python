"""
1042 - Sort Simples
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em
branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""

a, b, c = [int(x) for x in input().split()]
sort = [a, b, c]

for i in range(len(sort)):
    for j in range(i + 1, len(sort)):
        if sort[i] > sort[j]:
            aux = sort[i]
            sort[i] = sort[j]
            sort[j] = aux

for i in range(len(sort)):
    print(sort[i])

print("")

print(a), print(b), print(c)
