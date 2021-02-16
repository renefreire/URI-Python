"""
1049 - Animal
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda
para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas
as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
"""

filo = str(input())

if filo == "vertebrado":
    classe = str(input())
    if classe == "ave":
        alimentacao = str(input())
        if alimentacao == "carnivoro":
            print("aguia")
        elif alimentacao == "onivoro":
            print("pomba")
    elif classe == "mamifero":
        alimentacao = str(input())
        if alimentacao == "onivoro":
            print("homem")
        elif alimentacao == "herbivoro":
            print("vaca")
elif filo == "invertebrado":
    classe = str(input())
    if classe == "inseto":
        alimentacao = str(input())
        if alimentacao == "hematofago":
            print("pulga")
        elif alimentacao == "herbivoro":
            print("lagarta")
    elif classe == "anelideo":
        alimentacao = str(input())
        if alimentacao == "hematofago":
            print("sanguessuga")
        elif alimentacao == "onivoro":
            print("minhoca")
