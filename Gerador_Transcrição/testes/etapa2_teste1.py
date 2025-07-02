#como fazer a leitura do arquivo.txt

with open("lista.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

'''explicação:

"r" -> modo leitura
"with" -> abre e fecha o arquivo automaticamente
"utf-8" -> garante que acentos e caracteres especiais funcionem

.read() -> le tudo de uma vez como uma string

'''