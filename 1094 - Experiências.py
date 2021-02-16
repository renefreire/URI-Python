"""
1094 - Experiências
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os
experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram
utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela
sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias
utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de
teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo
('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação
ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
"""

N = int(input())

Total_Ratos = 0
Total_Sapos = 0
Total_Coelhos = 0
for i in range(N):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)
    if Tipo == "R":
        Total_Ratos += Quantia
    elif Tipo == "S":
        Total_Sapos += Quantia
    elif Tipo == "C":
        Total_Coelhos += Quantia

Total_Cobaias = Total_Ratos + Total_Sapos + Total_Coelhos

Perc_Ratos = 100*Total_Ratos/Total_Cobaias
Perc_Sapos = 100*Total_Sapos/Total_Cobaias
Perc_Coelhos = 100*Total_Coelhos/Total_Cobaias

print("Total: %d cobaias" % Total_Cobaias)
print("Total de coelhos: %d" % Total_Coelhos)
print("Total de ratos: %d" % Total_Ratos)
print("Total de sapos: %d" % Total_Sapos)
print("Percentual de coelhos: %.2f" % Perc_Coelhos, "%")
print("Percentual de ratos: %.2f" % Perc_Ratos, "%")
print("Percentual de sapos: %.2f" % Perc_Sapos, "%")
