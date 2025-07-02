texto = input("Digite um texto: ")

with open ("meu_arquivo.txt", "w", encoding='utf-8' ) as arquivo:
    arquivo.write(texto)