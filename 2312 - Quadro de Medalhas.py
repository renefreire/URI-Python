"""
2312 - Quadro de Medalhas
Alguém deixou o quadro de medalhas das olimpíadas fora de ordem. Seu programa deve colocá-lo
na ordem correta. A ordem dos países no quadro de medalhas é dada pelo número de medalhas de
ouro. Se há empate em medalhas de ouro, a nação que tiver mais medalhas de prata fica a frente
. Havendo empate em medalhas de ouro e prata, fica mais bem colocado o país com mais medalhas
de bronze. Se dois ou mais países empatarem nos três tipos de medalhas, seu programa deve
mostrá-los em ordem alfabética.

Entrada
A entrada é dada pelo número de países participantes N (0 ≤ N ≤ 500) seguido pela lista dos
países, com suas medalhas de ouro O (0 ≤ O ≤ 10000), prata P (0 ≤ P ≤ 10000) e bronze B
(0 ≤ B ≤ 10000).

Saída
A saída deve ser a lista de países, com suas medalhas de ouro, prata e bronze, na ordem
correta do quadro de medalhas, com as nações mais premiadas aparecendo primeiro.
"""

def troca(x1,x2):
    tmp = x1
    x1 = x2
    x2 = tmp
    return x1, x2

N = int(input())
lista = []
for n in range(N):
    
    C, O, P, B = input().split()

    O = int(O)
    P = int(P)
    B = int(B)

    lista.append([C, O, P, B])

for i in range(N-1):
    for j in range(i+1,N):
        if lista[i][1] < lista[j][1]:
            lista[i][:], lista[j][:] = troca(lista[i][:],lista[j][:])
        elif lista[i][1] == lista[j][1]:
            if lista[i][2] < lista[j][2]:
                lista[i][:], lista[j][:] = troca(lista[i][:],lista[j][:])
            elif lista[i][2] == lista[j][2]:
                if lista[i][3] < lista[j][3]:
                    lista[i][:], lista[j][:] = troca(lista[i][:],lista[j][:])
                elif lista[i][3] == lista[j][3]:
                    if lista[i][0] > lista[j][0]:
                        lista[i][:], lista[j][:] = troca(lista[i][:],lista[j][:])
                
for i in range(N):
    for j in range(4):
        if j < 3:
            print(lista[i][j],end=" ")
        else:
            print(lista[i][j])
    
