from usuario import cadastrar, listar

print("MENU")
print("Digite o número da opção desejada")
print("1. Listar usuários")
print("2. Cadastrar usuário")

opcao = int(input())

if opcao == 1:
    listar()
elif opcao == 2:
    cadastrar()