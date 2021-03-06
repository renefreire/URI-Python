"""
2287 - Proteja sua Senha
Por questões de segurança, muitos bancos hoje em dia estão alterando a forma como seus clientes digitam as senhas nos
caixas eletrônicos, pois alguém pode postar-se atrás do cliente e ver as teclas à medida em que ele as digita.
Uma alternativa bastante utilizada tem sido associar os dez dígitos a cinco letras, de forma que cada letra esteja
associada a dois dígitos.
As associações entre números e letras são mostradas como botões numa tela sensível ao toque, permitindo que o cliente
selecione os botões correspondentes à senha. Considerando a disposição dos botões da figura acima, a senha 384729 seria
digitada como BCEAEB (note que a mesma seqüência de letras seria digitada para outras senhas, como por exemplo 982123).
Cada vez que o cliente usa o caixa eletrônico, as letras utilizadas são as mesmas (de ‘A’ a ‘E’), com os botões nas
mesmas posições, mas os dígitos são trocados de lugar. Assim, caso um intruso veja (mesmo que mais de uma vez) a
seqüência de letras digitada, não é possível notar facilmente qual a senha do cliente do banco.
Dada uma seqüência de associações entre letras e números, e as letras digitadas pelo cliente do banco para cada uma
dessas associações, você deve escrever um programa para determinar qual é a senha do cliente.

Entrada
A entrada é composta de vários conjuntos de testes. A primeira linha de um conjunto de testes contém um inteiro N, que
indica o número de associações entre letras e números e as senhas digitadas (2 ≤ N ≤ 10). As N linhas seguintes contêm
as entradas da seguinte forma: 10 dígitos, em ordem de associação, para as letras de ‘A’ a ‘E’ (2 dígitos para a letra
A, 2 para a B e assim sucessivamente) e 6 letras que representam a senha codificada conforme os dígitos anteriores. As N
associações fornecidas em um conjunto de testes serão sempre suficientes para definir univocamente a senha do cliente. O
final da entrada é indicado por N = 0.

Saída
Para cada conjunto de teste da entrada, seu programa deve produzir três linhas na saída. A primeira linha deve conter um
identificador do conjunto de teste, no formato “Teste n”, onde n é numerado seqüencialmente a partir de 1. A segunda
linha deve conter a senha do cliente, com um espaço após cada dígito. A terceira linha deve ser deixada em branco. A
grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.
"""

N = int(input())
teste = 0
senha = 0
entradas = []
digitos = []
cont = 10*[0]

while N != 0:

    teste += 1

    for n in range(N):
        entradas.append(input().split())

    print("Teste %d" % teste)

    for s in range(6):
        for n in range(N):
            if entradas[n][s+10] == "A":
                digitos.append(entradas[n][0])
                digitos.append(entradas[n][1])
            elif entradas[n][s+10] == "B":
                digitos.append(entradas[n][2])
                digitos.append(entradas[n][3])
            elif entradas[n][s+10] == "C":
                digitos.append(entradas[n][4])
                digitos.append(entradas[n][5])
            elif entradas[n][s+10] == "D":
                digitos.append(entradas[n][6])
                digitos.append(entradas[n][7])
            elif entradas[n][s+10] == "E":
                digitos.append(entradas[n][8])
                digitos.append(entradas[n][9])

        for i in range(10):
            for d in range(len(digitos)):
                if str(i) == digitos[d]:
                    cont[i] += 1

        senha = cont.index(max(cont))
        print(senha, end=" ")
        digitos = []
        cont = 10*[0]

    print("\n")

    entradas = []

    N = int(input())
