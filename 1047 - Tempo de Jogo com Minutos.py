"""
1047 - Tempo de Jogo com Minutos
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
"""

HI, MI, HF, MF = [int(x) for x in input().split()]

minutos = (HF*60 + MF) - (HI*60 + MI)
if minutos <= 0:
    minutos += 24*60

horas = minutos // 60
minutos -= horas*60

jogo = "O JOGO DUROU {} HORA(S) E {} MINUTO(S)"
print(jogo.format(horas, minutos))
