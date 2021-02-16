"""
2321 - Detectando Colisões
Detecção de colisão é uma das operações mais comuns (e importantes) em jogos eletrônicos. O objetivo, basicamente, é
verificar se dois objetos quaisquer colidiram, ou seja, se a interseção entre eles é diferente de vazio. Isso pode ser usado
para saber se duas naves colidiram, se um monstro bateu numa parede, se um personagem pegou um item, etc.
Para facilitar as coisas, muitas vezes os objetos são aproximados por figuras geométricas simples (esferas, paralelepípedos,
triângulos etc). Neste problema, os objetos são aproximados por retângulos num plano 2D.
Escreva um programa que, dados dois retângulos, determine se eles se interceptam ou não.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).
Cada caso de teste contém duas linhas. Cada linha contém quatro inteiros (x0, y0, x1, y1, sendo 0 ≤ x0 < x1 ≤ 1.000.000 e
0 ≤ y0 < y1 ≤ 1.000.000) separados por um espaço em branco representando um retângulo. Os lados do retângulo são sempre para
lelos aos eixos x e y.

Saída
Seu programa deve imprimir, na saída padrão, uma única linha para cada caso de teste, contendo o número 0 (zero) caso não
haja interseção ou o número 1 (um) caso haja.
"""

X0, Y0, X1, Y1 = [int(i) for i in input().split()]
X2, Y2, X3, Y3 = [int(j) for j in input().split()]

result = 0

cx = not((X1 < X2)or(X3 < X0))
cy = not((Y1 < Y2)or(Y3 < Y0))

if cx and cy:
    result = 1

print (result)
