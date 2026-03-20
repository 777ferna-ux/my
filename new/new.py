users = {}
print("Bem-vindo ao Banco Central")
def main():
    print("\nBanco Central")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")
    
    while True:
        resposta = input("Escolha uma opção: ")
        if resposta == "1":
            login()
            break
        elif resposta == "2":
            register()
            break
        elif resposta == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def banco():
    print("\nBanco Central")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Transferir")
    print("4 - Sair")
    what = input("Escolha uma opção: ")
    # Add logic for banking operations here

def login():
    while True:
        login_cpf = input("Digite seu CPF: ")
        if login_cpf in users:
            break
        else:
            print("CPF não encontrado.")

    while True:
        senha = input("Digite sua senha: ")
        if users[login_cpf] == senha:
            print("\nLogin realizado com sucesso!")
            banco()
            break
        else:
            print("Senha incorreta.")

def register():
    while True:
        cpf = input("Digite seu CPF (11 dígitos): ")
        if len(cpf) == 11 and cpf.isdigit():
            if cpf in users:
                print("CPF já cadastrado.")
            else:
                break
        else:
            print("CPF inválido. Deve conter 11 dígitos numéricos.")

    while True:
        senha = input("Digite sua senha: ")
        senha2 = input("Confirme sua senha: ")
        if senha == senha2:
            break
        else:
            print("As senhas não conferem. Tente novamente.")
            
    users[cpf] = senha
    print("\nCadastro realizado com sucesso!")
    print("Por favor, faça o login.")
    login()

if __name__ == "__main__":
    main()
