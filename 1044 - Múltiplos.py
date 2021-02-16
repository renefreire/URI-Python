"""
1044 - Múltiplos
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
"""

A, B = [int(x) for x in input().split()]

mult = [A, B]
mult.sort()
if mult[1] % mult[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
