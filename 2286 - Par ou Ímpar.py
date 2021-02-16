"""
2286 - Par ou Ímpar
Muitas crianças gostam de decidir todas as disputas através do famoso jogo de Par ou Ímpar. Nesse jogo, um dos
participantes escolhe Par e o outro Ímpar. Após a escolha, os dois jogadores mostram, simultaneamente, uma certa
quantidade de dedos de uma das mãos. Se a soma dos dedos das mãos dos dois jogadores for par, vence o jogador que
escolheu Par inicialmente, caso contrário vence o que escolheu Ímpar.
Dada uma seqüência de informações sobre partidas de Par ou Ímpar (nomes dos jogadores e números que os jogadores
escolheram), você deve escrever um programa para indicar o vencedor de cada uma das partidas.

Entrada
A entrada é composta de vários conjuntos de testes. A primeira linha de um conjunto de testes contém um inteiro N
(0 ≤ N ≤ 1000), que indica o número de partidas de Par ou Ímpar que aconteceram. As duas linhas seguintes contêm cada
uma um nome de jogador. Um nome de jogador é uma cadeia de no mínimo um e no máximo dez letras (maiúsculas e
minúsculas), sem espaços em branco. As N linhas seguintes contêm cada uma dois inteiros A e B que representam o número
de dedos que cada jogador mostrou em cada partida (0 ≤ A ≤ 5 e 0 ≤ B ≤ 5). Em todas as partidas, o primeiro jogador
sempre escolhe Par. O final da entrada é indicado por N = 0.

Saída
Para cada conjunto de teste da entrada, seu programa deve produzir a saída da seguinte forma. A primeira linha deve
conter um identificador do conjunto de teste, no formato “Teste n”, onde n é numerado seqüencialmente a partir de 1. As
próximas N linhas devem indicar o nome do vencedor de cada partida. A próxima linha deve ser deixada em branco. A grafia
mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.
"""

N = int(input())
p = []
teste = 0

while N != 0:

    teste += 1

    J1 = input()
    J2 = input()

    for n in range(N):
        A, B = [int(x) for x in input().split()]
        p.append([A, B])

    print("Teste %d" % teste)
    for n in range(N):
        if(p[n][0] + p[n][1]) % 2 == 0:
            print(J1)
        else:
            print(J2)

    print("")

    p = []

    N = int(input())
