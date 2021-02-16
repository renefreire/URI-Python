"""
1847 - Bem-vindos e Bem-vindas ao Inverno
O inverno é uma estação maravilhosa, não é mesmo? Todos nós amamos vestir um poncho, participar de uma roda de
chimarrão, assar pinhões no fogão a lenha… Mas nem todos gostam do inverno, especialmente em lugares onde o inverno
costuma ser muito cruel. Em Westeros, por exemplo, o humor das pessoas é definido de acordo com as tendências
climáticas. Com base nas temperaturas dos três últimos dias, as pessoas podem ficar tristes ou felizes, ficando mais
propensas a fazer guerra ou fazer amor, respectivamente. E, sejamos sinceros, é justamente por causa das cenas de amor e
de guerra que amamos Game of Thrones!
Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, as pessoas ficam felizes
(primeira figura).
Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, as pessoas ficam tristes
(segunda figura).
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que subira do 1º para o
2º, as pessoas ficam tristes (terceira figura).
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que subira do
1º para o 2º, as pessoas ficam felizes (quarta figura).
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que descera do 1º
para o 2º, as pessoas ficam felizes (quinta figura).
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º no mínimo o tanto que descera
do 1º para o 2º, as pessoas ficam tristes (sexta figura).
Se a temperatura permaneceu constante do 1º para o 2º dia, as pessoas ficam felizes se subiu do 2º para o 3º dia ou
tristes caso contrário (respectivamente, sétima e oitava figuras).

Entrada
A entrada consiste apenas de três inteiros, A, B e C (-100 ≤ A, B, C ≤ 100), os quais representam respectivamente as
temperaturas registradas no 1º, no 2º e no 3º dias.

Saída
Imprima uma linha contendo uma carinha feliz ou triste, representando como fica o humor do povo de Westeros de acordo
com as tendências climáticas.
"""

A, B, C = [int(x) for x in input().split()]

if (A > B)and(B <= C):
    print(":)")
elif (A < B)and(B >= C):
    print(":(")
elif (A < B)and(B < C)and(C - B < B - A):
    print(":(")
elif (A < B)and(B < C)and(C - B >= B - A):
    print(":)")
elif (A > B)and(B > C)and(B - C < A - B):
    print(":)")
elif (A > B)and(B > C)and(B - C >= A - B):
    print(":(")
elif (A == B)and(B < C):
    print(":)")
elif (A == B)and(B >= C):
    print(":(")
