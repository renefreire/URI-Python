"""
2306 - Escada Perfeita
Uma construtora, durante a criação de um parque temático, encontrou no terreno um conjunto de vários pilhas de cubos de
pedra. Ao invés de pagar pela remoção dos cubos de pedras, um dos arquitetos da empresa achou interessante utilizar as
pedras para decoração do parque, determinando que as pedras fossem rearranjadas no formato de “escada”. Para isso, os
funcionários deveriam mover alguns cubos para formar os degraus das escadas. Só que o arquiteto decidiu que, entre uma
pilha e outra de pedras deveria haver exatamente uma pedra de diferença, formando o que ele chamou de escada perfeita. O
exemplo abaixo mostra um conjunto de cinco pilhas de pedras encontradas e as cinco pilhas como ficaram ap´os a arrumação
em escada perfeita.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o
teclado). A primeira linha contém um inteiro N que indica o número de pilhas de pedras. A segunda linha contém N números
inteiros que indicam a quantidade de cubos de pedras em cada uma das pilhas, da esquerda para a direita.

Saída
Seu programa deve imprimir, na saída padrão, uma única linha, contendo um inteiro: o número mínimo de cubos de pedras
que devem ser movidos para transformar o conjunto de pilhas em uma escada perfeita, conforme calculado pelo seu
programa. Caso não seja possível efetuar a transformação em escada perfeita, imprima como resultado o valor -1.
"""

N = int(input())
pilhas = [int(k) for k in input().split()]

cubos = sum(pilhas)
pilhaN = int(((2*cubos/N) + N - 1)/2)
pilha1 = 1 + pilhaN - N

moves = 0
aux = 0
for n in range(N):
    aux += (pilhas[n] - (pilha1 + n))
    if pilhas[n] > (pilha1 + n):
        moves += (pilhas[n] - (pilha1 + n))

if aux != 0:
    print(-1)
else:
    print("%d" % moves)
