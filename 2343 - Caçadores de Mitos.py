"""
2343 - Caçadores de Mitos
Jorge é um apresentador de televisão que comanda a versão brasileira do grande sucesso Caçadores de Mitos, onde se
estuda um mito para descobrir se é fato ou apenas um boato.
No próximo episódio, Jorge deverá apresentar o mito que diz que ”os raios não caem duas vezes no mesmo lugar”,
referindo-se aos raios das tempestades de chuva.
Para isso, foi até a cidade de Eletrolândia, que é a cidade com maior ocorrência de raios no mundo. O prefeito tem tanto
orgulho desse título que mandou criar um sistema para registrar os raios. Jorge conseguiu um relatório com as
ocorrências de cada raio que caiu na cidade nos últimos anos.
O mapa de Eletrolândia é um retângulo. Para o sistema de registro a cidade é subdividida em quadrados de um metro de
lado, denominados quadrantes. Assim, se a cidade tem 300 metros de largura e 1000 de comprimento, ela será subdividida
em 300.000 quadrantes. O sistema de registro armazena o quadrante em que o raio caiu. Cada quadrante é identificado
pelas suas coordenadas X e Y, conforme ilustra a figura abaixo, que exemplifica um mapa de uma cidade com oito metros de
comprimento por cinco metros de largura (quarenta quadrantes).
Como os quadrantes são relativamente pequenos, Jorge decidiu que se dois raios caíram no mesmo quadrante, pode-se
considerar que caíram no mesmo lugar.
Sua missão é escrever um programa que receba as coordenadas dos raios que caíram em Eletrolândia nos últimos anos e
determine se o mito estudado é realmente apenas um mito ou pode ser considerado verdade.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o
teclado).
A primeira linha da entrada contém um número inteiro N (2 ≤ N ≤ 500.000) representando o número de registros de raios no
relatório. Cada uma das N linhas seguintes contém 2 números inteiros X, Y (0 ≤ X, Y ≤ 500), representando o registro de
um raio que caiu no quadrante cujas coordenadas são (X, Y).

Saída
Seu programa deve imprimir, na saída padrão, o número 0 se nenhum raio caiu no mesmo lugar, ou o número 1 caso
contrário. Note que você deve imprimir o número 1 mesmo que haja mais do que 1 par de raios que caíram no mesmo lugar.
"""

N = int(input())
raio = 0
quad = [[0]*501 for k in range(501)]

for n in range(N):
    X, Y = [int(i) for i in input().split()]
    if raio == 0:
        if quad[X][Y] == 0:
            quad[X][Y] = 1
        else:
            raio = 1

print(raio)
