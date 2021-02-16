"""
2316 - Autorama
Seu Diniz possui uma pista de autorama profissional. Nessa pista a marcação de tempo é feita com sensores que fazem leitura da
passagem de cada cada carrinho pelo ponto onde o sensor está instalado. K sensores são distribuídos ao longo da pista nos
chamados postos de checagem.
Durante uma corrida, os carrinhos devem passar pelos postos de checagem na ordem pré-estabelecida, ou seja, primeiro no posto
de checagem 1, depois no 2, até o posto de checagem K, quando ele deve retornar ao posto de checagem 1 para completar uma volta.
Entretanto, às vezes, quando os carrinhos saem da pista os competidores os recolocam mais à frente na pista, pulando alguns
postos de checagem. Nesse caso, todas as passagens daquele carrinho por postos de checagem devem ser ignoradas até que ele passe
pelo posto de checagem correto.
A posição de um carrinho na corrida é determinada pelo número de postos de checagem que ele passou na ordem correta. Caso dois
carrinhos tenham passado pelo mesmo número de postos de checagem, a ordem utilizada é a ordem cronológica, ou seja, está mais à
frente o carrinho que passou pelo último posto de checagem primeiro.
A pista de autorama do Seu Diniz possui um computador central que recebe os sinais lidos pelos sensores, mas ainda não possui
um programa que permita determinar a posição dos carrinhos ao final da corrida.
Escreva um programa que, dado uma lista de leituras feitas pelos sensores, determine a classificação dos carrinhos na corrida.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A
primeira linha da entrada contêm três inteiros, K, N e M. K representa o número de postos de checagem (1 ≤ K ≤ 100), N o número
de carrinhos (1 ≤ N ≤ 100) e M o número de leituras feitas pelos sensores (1 ≤ M ≤ 10000). Os carrinhos são identificados por
inteiros de 1 a N e os postos de checagem por inteiros de 1 a K. As M linhas seguintes contêm cada uma dois inteiros X e Y,
separados por espaço. Eles indicam que o carrinho número X (1 ≤ X ≤ N) passou pelo posto de checagem Y (1 ≤ Y ≤ K). Os eventos
são apresentados na ordem cronológica. Sempre é possível determinar a classificação de todos os pilotos com os dados fornecidos.

Saída
Seu programa deve imprimir, na saída padrão, uma linha contendo N inteiros, sendo que o i-ésimo inteiro representa o carrinho
que ocupa a posição i na corrida. Ou seja, o primeiro inteiro é o que ocupa o primeiro lugar, o segundo inteiro é o carrinho
que ocupa o segundo lugar, e assim por diante.
Cada inteiro I contendo o número do carrinho que ocupa a posição de número I na corrida: o primeiro colocado ocupa a posição de
número 1, o segundo colocado a posição de número 2, etc.
"""

K, N, M = [int(k) for k in input().split()]

corrida = []
for n in range(N):
    corrida.append([0,0,0])

for m in range(M):
    
    X, Y = [int(k) for k in input().split()]

    if Y == corrida[X-1][1] + 1:
        corrida[X-1][1] = Y
        corrida[X-1][2] = m
    elif (corrida[X-1][1] == K)and(Y == 1):
        corrida[X-1][0] += 1
        corrida[X-1][1] = Y
        corrida[X-1][2] = m

posicoes = list(range(1,N+1))
for i in range(N-1):
    for j in range((i+1),N):
        A = posicoes[i] - 1
        B = posicoes[j] - 1
        if corrida[A][0] < corrida[B][0]:
            aux = posicoes[i]
            posicoes[i] = posicoes[j]
            posicoes[j] = aux
        elif corrida[A][0] == corrida[B][0]:
            if corrida[A][1] < corrida[B][1]:
                aux = posicoes[i]
                posicoes[i] = posicoes[j]
                posicoes[j] = aux
            elif corrida[A][1] == corrida[B][1]:
                if corrida[A][2] > corrida[B][2]:
                    aux = posicoes[i]
                    posicoes[i] = posicoes[j]
                    posicoes[j] = aux

for n in range(N):
    if n < N-1:
        print(posicoes[n],end=" ")
    else:
        print(posicoes[n])
