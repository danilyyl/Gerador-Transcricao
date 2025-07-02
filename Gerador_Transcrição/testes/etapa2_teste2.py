nome_arquivo = input("Digite o nome do arquivo com (.txt): ")

contador = 1

#Isso adiciona o primeiro arquivo
texto = input("Digite o texto que irá no arquivo: ")
with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write(f"{contador} - {texto}\n")


# Pergunta se quer adicionar mais
addTexto = input("Deseja adicionar mais texto? (s/n): ")

while addTexto.lower() == "s":
    contador += 1 #incrementa o numero da linha
    maisTexto = input("Digite o novo texto: ")

    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{contador} - {maisTexto}\n")
    
    addTexto = input("Deseja adicionar mais texto? (s/n): ")


# Mostra o conteúdo final do arquivo
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("\n Todo o seu conteudo: ")
    print(conteudo)


#Perguntando ao usuario se deseja mostrar o conteudo novamente
printNovamente = input("Deseja mostrar todo o conteudo novamente? (s/n): ")

while printNovamente.lower() == "s":
    print(conteudo)
    printNovamente = input("Deseja mostrar o conteudo na tela novamente? (s/n): ")

if printNovamente.lower() == "n":
    print("Encerrando completamente...")


