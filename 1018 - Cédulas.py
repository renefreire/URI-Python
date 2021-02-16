"""
1018 - Cédulas
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser
decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas
necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem:
“Presentation Error”.
"""

N = int(input())

nota100 = N//100
N = N - 100*nota100
nota50 = N//50
N = N - 50*nota50
nota20 = N//20
N = N - 20*nota20
nota10 = N//10
N = N - 10*nota10
nota5 = N//5
N = N - 5*nota5
nota2 = N//2
N = N - 2*nota2
nota1 = N

N = 100*nota100 + 50*nota50 + 20*nota20 + 10*nota10 + 5*nota5 + 2*nota2 + nota1

print(N)
print("%d nota(s) de R$ 100,00" % nota100)
print("%d nota(s) de R$ 50,00" % nota50)
print("%d nota(s) de R$ 20,00" % nota20)
print("%d nota(s) de R$ 10,00" % nota10)
print("%d nota(s) de R$ 5,00" % nota5)
print("%d nota(s) de R$ 2,00" % nota2)
print("%d nota(s) de R$ 1,00" % nota1)
