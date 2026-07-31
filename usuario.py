def cadastrar():
    # Função para cadastrar um novo usuário
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    # Aqui você pode adicionar a lógica para salvar os dados do usuário em um banco de dados ou arquivo
    print(f"Usuário {nome} cadastrado com sucesso!")

    f = open("usuarios.txt", "a") # cria e abre o arquivo
    # parametros do open:
    # "a" = append (adiciona no final do arquivo)
    # "w" = write (sobrescreve o arquivo)
    # "r" = read (apenas lê o arquivo)
    f.write(f"{nome},{email},{senha}\n") # escreve no arquivo
    f.close() # fecha o arquivo

def listar():
    f = open("usuarios.txt", "r") # lê o arquivo

    for linha in f.readlines(): # percorre cada linha do arquivo
        print(linha) # mostra a linha na tela