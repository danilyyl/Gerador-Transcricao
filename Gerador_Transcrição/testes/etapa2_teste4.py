contador = 1

'''Faz o menu em forma de lista'''
opcoes = [
    "Adicionar nova linha",
    "Ler todas as linhas",
    "Ler linha específica",
    "Editar linha específica",
    "Apagar linha específica",
    "Sair"
]

''' adiciona a lista ao arquivo menu.txt numerando as linhas '''
with open("menu.txt", "w", encoding="utf-8") as arquivo:
    for opcao in opcoes:
        arquivo.write(f"{contador} - {opcao}\n")
        contador += 1

''' abre o arquivo, le e imprime o menu completo '''
with open("menu.txt", "r", encoding="utf-8") as arquivo:
    menu = arquivo.read()

print("=== MENU ===")
print(menu)

''' abre o arquivo e le linha por linha '''
with open ("menu.txt", "r", encoding="utf-8" ) as arquivo:
    linhas = arquivo.readlines()

''' codigo para mostrar e alterar linhas desejadas '''
while True:
    numero = int(input("Qual linha voçe deseja vizualizar: "))
    
    ''' mostra linha desejada '''
    indice = numero - 1
    if 0 <= indice < len(linhas):
        print(linhas[indice])
        
        ''' pergunta se deseja alterar alguma linha '''
        Pergunta = input("Deseja alterar essa linha?(s/n) ")
        
        '''se sim, adiciona novo texto e atualiza linha'''
        if Pergunta.lower() == "s":
            novoTexto = input("Digite novo texto: ")
            linhas[indice] = f"{numero} - {novoTexto}\n"

            ''' adiciona linha nova ao arquivo '''
            with open("menu.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(linhas)

            ''' le linha nova no arquivo e mostra ao usuario a linha atualizada '''
            with open("menu.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            print("Linha atualizada:", linhas[indice].strip())           

            print("\n=== MENU ATUALIZADO ===")
            for i, linha in enumerate(linhas, start=1):
                 print(linha.strip())

    else:
        print("Essa linha não existe!")
    ''' se a linha não estiver no menu mostra esse aviso '''

    ''' pergunta ao usuario se ele deseja ver outra linha, se não encerra o programa '''
    continuar = input("Deseja ver outra linha? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando...")
        break
