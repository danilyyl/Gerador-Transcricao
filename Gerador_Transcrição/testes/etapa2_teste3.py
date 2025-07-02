nome_arquivo = input("Digite o nome do arquivo  com .txt: ")

with open (nome_arquivo, "r", encoding="utf-8" ) as arquivo:
    linhas = arquivo.readlines()

while True:
    numero = int(input("Qual linha voçe deseja visualizar? "))

    indice = numero - 1
    if 0 <= indice < len(linhas):
        print(linhas[indice])
    else:
        print("Essa linha não existe!")

    continuar = input("Deseja ver outra linha? (s/n): ").lower()
    if continuar != "s":
        break

