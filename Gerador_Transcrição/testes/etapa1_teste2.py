nome_arquivo = input("Digite um nome o arquivo com '.txt': ")
texto = input("Digite o texto para o arquivo: ")

with open (nome_arquivo, "a", encoding='utf-8') as arquivo:
    arquivo.write(texto + "\n")