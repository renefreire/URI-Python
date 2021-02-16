"""
1048 - Aumento de Salário
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
Salário             Percentual de Reajuste
0 - 400.00                  15%
400.01 - 800.00             12%
800.01 - 1200.00            10%
1200.01 - 2000.00           7%
Acima de 2000.00            4%
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice
reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo
abaixo.
"""

salario = float(input())
reajuste = 0

if (salario >= 0)and(salario <= 400.00):
    reajuste = 15
elif (salario >= 400.01)and(salario <= 800.00):
    reajuste = 12
elif (salario >= 800.01)and(salario <= 1200.00):
    reajuste = 10
elif (salario >= 1200.01)and(salario <= 2000):
    reajuste = 7
elif salario > 2000.00:
    reajuste = 4

novo_salario = salario*(1 + reajuste/100)
reajuste_ganho = salario*reajuste/100

print("Novo salario: %.2f" % novo_salario)
print("Reajuste ganho: %.2f" % reajuste_ganho)
print("Em percentual:", reajuste, "%")
