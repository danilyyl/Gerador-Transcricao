nome_arquivo = input("Digite o nome do arquivo com '.txt': ")

# Começa com contador 1
contador = 1

# Primeiro texto
texto = input("Digite o texto do arquivo: ")

# Cria ou abre o arquivo e escreve o primeiro texto numerado
with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{contador} - {texto}\n")

# Incrementa o contador
contador += 1

# Pergunta se quer adicionar mais texto
addTexto = input("Deseja adicionar mais texto? (s/n): ")

# Enquanto a resposta for "s" (sim)
while addTexto.lower() == "s":
    texto = input("Digite outro texto: ")

    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{contador} - {texto}\n")
    
    contador += 1

    addTexto = input("Deseja adicionar mais texto? (s/n): ")

# Se o usuário disser "n" (não), encerra
if addTexto.lower() == "n":
    print("Encerrando...")