"""
1066 - Pares, Ímpares, Positivos e Negativos
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
"""
par = 0
impar = 0
pos = 0
neg = 0

for i in range(5):

    N = int(input())

    if N % 2 == 0:
        par += 1
    else:
        impar += 1

    if N > 0:
        pos += 1
    elif N < 0:
        neg += 1

print("%d valor(es) par(es)" % par)
print("%d valor(es) impar(es)" % impar)
print("%d valor(es) positivo(s)" % pos)
print("%d valor(es) negativo(s)" % neg)
