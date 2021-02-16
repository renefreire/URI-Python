"""
1012 - Área
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com
mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos
após o ponto decimal.
"""

A, B, C = [float(x) for x in input().split()]
pi = 3.14159

TRIANGULO = A*C/2
CIRCULO = pi*C**2
TRAPEZIO = (A + B)*C/2
QUADRADO = B**2
RETANGULO = A*B

print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)
