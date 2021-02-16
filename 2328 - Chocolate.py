"""
2328 - Chocolate
Juliana é uma famosa doceira reconhecida internacionalmente pelos seus bombons, exportados para todo o mundo. Embora não
revele a ninguém as suas receitas, ela já deu entrevistas contando alguns de seus segredos. Sua fábrica de bombons
utiliza somente chocolates comprados de um único produtor suíço, que envia barras gigantescas que são cortadas por
grandes máquinas.
Dada uma barra grande de chocolate, Juliana realiza divisões sucessivas da barra até obter uma barra que contém a
quantidade exata de chocolate para aquela receita. Após cada divisão, ela seleciona um dos pedaços resultantes e
armazena os demais para uso futuro. As divisões são determinadas por critérios técnicos relacionados ao tamanho das
barras e aos equipamentos disponiveis em um dado momento.
Por exemplo, se ela deseja obter uma barra de 100g de chocolate a partir de uma barra de 3Kg, primeiro ela divide a
barra ao meio. Em seguida, um dos pedaços é dividido em cinco partes iguais e por fim, um desses pedaços de 300g é
dividido em 3 pedaços, resultando no pedaço de 100g necessário para a receita. Nesse processo, 1 pedaço é utilizado para
a receita e 7 pedaços de diferentes tamanhos serão guardados para uso futuro. A figura abaixo ilustra esse cenário.
Dada uma sequência de divisões realizadas por Juliana em uma barra de chocolate, determinar quantos pedaços serão
armazenados em estoque para uso futuro.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).
A primeira linha da entrada contém um inteiro N que indica o número de divisões feitas na barra de chocolate original
(1 ≤ N ≤ 1.000). A linha seguinte contém N inteiros I (2 ≤ I ≤ 10) representando o número de pedaços em que o pedaço
atual foi dividido. Sempre que é feita uma divisão, um pedaço é utilizado para a próxima divisão e os demais são
separados para serem armazenados em estoque.

Saída
Seu programa deve imprimir, na saída padrão, uma única linha, contendo o número de pedaços de chocolate que serão
armazenados em estoque.
"""

N = int(input())

P = [int(n) for n in input().split()]

pedacos = 0
for n in range(N):
    pedacos += (P[n] - 1)

print(pedacos)
