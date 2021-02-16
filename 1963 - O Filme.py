"""
1963 - O Filme
E foi esperança que motivou a Vovó Zazá, uma senhora de 72 anos, a realizar seu sonho de começar um curso universitário.
Ela está fascinada com tudo o que diz respeito à Universidade: com as aulas, com a biblioteca, com os projetos de
pesquisa e extensão, com o restaurante universitário, mas especialmente com a carteirinha de estudante que ela pode
utilizar para pagar meia entrada no cinema. Semana passada, Vovó Zazá e seus colegas de turma foram ao cinema assistir a
um filme, mas ficaram estarrecidos com o aumento do preço do ingresso. Revoltados, eles decidiram fazer uma manifestação
contra o sistema capitalista opressor, agendada para amanhã na Praça General Bertaso. Vovó Zazá quer colaborar com o
movimento fazendo um cartaz com a seguinte palavra de ordem: QUE ABSURDO! O PREÇO DO CINEMA SUBIU … % !!

Entrada
A única linha da entrada consiste de dois valores A e B (0.00 < A ≤ B ≤ 1000.00), os quais, fornecidos com exatos dois
dígitos após o ponto separador decimal, representam respectivamente o valor antigo e o valor novo do ingresso do cinema.

Saída
A única linha da saída deve consistir unicamente de um valor, que represente como uma porcentagem o aumento do valor do
ingresso. O valor deve ser acompanhado do símbolo % e conter exatos dois dígitos após o ponto separador decimal.
"""

A, B = [float(x) for x in input().split()]

P = 100*(B - A)/A
print("%.2f" % P, end=""), print("%")
