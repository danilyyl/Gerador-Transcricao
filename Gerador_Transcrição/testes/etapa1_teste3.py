nome_arquivo = input("Digite o nome do arquivo com '.txt': ")
texto = input("Digite o texto do arquivo: ")

with open (nome_arquivo, "a", encoding='utf-8') as arquivo:
    arquivo.write(texto + "\n")

addTexto = input("Deseja adicionar mais texto? (s/n): ")
if addTexto == "s":
    maisTexto = input("Digite outro texto: ")
    with open (nome_arquivo, "a", encoding='utf-8') as arquivo:
        arquivo.write(maisTexto + "\n")
elif addTexto == "n":
    print("Encerrando")
