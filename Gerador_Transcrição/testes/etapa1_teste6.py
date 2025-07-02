texto = input("Digite um texto: ")

with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(texto + "\n")

addTexto = input("Deseja adicionar mais texto? (s/n): ")

while addTexto.lower() == "s":
    maisTexto = input("Digite outro texto: ")
    with open("arquivo.txt", "a", encoding="utf-8") as arquivo:  # corrigido aqui
        arquivo.write(maisTexto + "\n")
    addTexto = input("Deseja adicionar mais texto? (s/n): ")

if addTexto.lower() == "n":
    print("Encerrando...")