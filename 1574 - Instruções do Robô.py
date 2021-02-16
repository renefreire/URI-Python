"""
1574 - Instruções do Robô
Você possui um robô na origem do eixo x. O robô receberá algumas instruções. Sua tarefa é predizer sua posição depois de
executar todas as instruções.
LEFT: move uma unidade para a esquerda (diminui p em 1, onde p é a posição do robô antes de mover)
RIGHT: move uma unidade para a direita (incrementa p em 1)
SAME AS i: executa a mesma ação que na i-ésima instrução. É garantido que i é um inteiro positivo não maior que o número de
instruções já executadas.

Entrada
A primeira linha contém o número de casos de testes T (T <= 100). Cada caso de teste inicia com um inteiro n ( 1 <= n <= 100),
o número de instruções. Cada uma das n linhas seguintes contém uma instrução.

Saída
Para cada caso de teste, imprima a posição final do robô. Note que após processar cada caso de teste, o robô deve ter sua
posição inicial resetada para a origem.
"""

T = int(input())

move = []
X = 0

for t in range(T):

    N = int(input())

    for n in range(N):
        
        instrucao = input()
        
        if instrucao == "LEFT":
            X -= 1
            move.append(-1)
        elif instrucao == "RIGHT":
            X += 1
            move.append(1)
        elif instrucao[:8] == "SAME AS ":
            s = int(instrucao[-2:]) - 1
            X += move[s]
            move.append(move[s])

    print(X)

    move = []
    X = 0
