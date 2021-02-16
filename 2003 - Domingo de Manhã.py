"""
2003 - Domingo de Manhã
Domingo é dia de feira. Logo de manhã muitas pessoas se deslocam para o polo de lazer da Parangaba, onde acontece uma
feira, conhecida por ser a maior da cidade. Na feira da Parangaba você pode encontrar de tudo.
Todos os domingos, Bino faz compras na feira. Ele sempre marca com seu amigo Cino de se encontrarem no terminal de
ônibus da Parangaba às 8h, para irem juntos comprar na feira. Porém, muitas vezes Bino acorda muito tarde e se atrasa
para o encontro com seu amigo.
Sabendo que Bino leva de 30 a 60 minutos para chegar ao terminal. Diga o atraso máximo de Bino.

Entrada
A entrada consiste em múltiplos casos teste. Cada caso de tese contém uma única linha contendo um horário H
(5:00 ≤ H ≤ 9:00) que Bino acordou. A entrada termina com final de arquivo (EOF -> Ctrl + D).

Saída
Para cada caso de teste, imprima "Atraso maximo: X" (sem aspas), X indica o atraso maximo (em minutos) de Bino no
encontro com Cino.
"""

while True:
    try:
        h, m = input("").split(":")
        h = int(h)
        m = int(m)

        minutos = h*60 + m
        if minutos <= 7*60:
            atraso = 0
            print("Atraso maximo:", atraso)
        else:
            atraso = (minutos + 60) - 8*60
            print("Atraso maximo:", atraso)

    except EOFError:
        break
