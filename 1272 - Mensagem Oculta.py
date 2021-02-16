"""
1272 - Mensagem Oculta
Textos podem conter mensagens ocultas. Neste problema a mensagem oculta em um texto é composto pelas primeiras letras de
cada palavra do texto, na ordem em que aparecem.
É dado um texto composto apenas por letras minúsculas ou espaços. Pode haver mais de um espaço entre as palavras. O texto
pode iniciar ou terminar em espaços, ou mesmo conter somente espaços.

Entrada
A entrada contém vários casos de testes. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de
teste que vem a seguir. Cada caso de teste consiste de uma única linha contendo de um a 50 caracteres, formado por letras
minúsculas (‘a’-‘z’) ou espaços (‘ ’). Atenção para possíveis espaços no início ou no final do texto!
Nota: No exemplo de entrada os espaços foram substituídos por pequenos pontos (‘·’) para facilitar o entendimento dos
exemplos.

Saída
Para cada caso de teste imprima a mensagem oculta no texto de entrada.
"""

N = int(input())
mensagem = ""

for n in range(N):
    
    texto = input()
    
    for k in range(len(texto)):
        if k == 0:
            if texto[k] != " ":
                mensagem += texto[k]
        else:
            if (texto[k-1] == " ")and(texto[k] != " "):
                mensagem += texto[k]
        
    if mensagem == "":
        mensagem = " "

    print(mensagem)

    mensagem = ""
