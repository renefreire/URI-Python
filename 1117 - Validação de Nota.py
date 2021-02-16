"""
1117 - Validação de Nota
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça
com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser
validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas
notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve
ser apresentado com duas casas após o ponto decimal.
"""

nota1 = float(input())
while (nota1 < 0)or(nota1 > 10):
    print("nota invalida")
    nota1 = float(input())

nota2 = float(input())
while (nota2 < 0)or(nota2 > 10):
    print("nota invalida")
    nota2 = float(input())

media = (nota1 + nota2)/2
print("media = %.2f" % media)
