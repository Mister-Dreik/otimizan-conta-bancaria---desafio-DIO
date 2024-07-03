# Estrutura para armazenar usuários e contas
usuarios = []
contas = []

def login():
    print('Olá, Entre com seu Usuário e senha\n')
    usuario = input('Seu usuário: ')
    senha = int(input('Insira sua senha: '))
    print(f'Olá {usuario}, Escolha uma opção abaixo')
    return usuario

def mostrar_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [u] Novo Usuário
    [q] Sair

    => """
    return input(menu)

def encontrar_conta(numero_conta):
    for conta in contas:
        if conta['conta'] == numero_conta:
            return conta
    return None

def depositar():
    numero_conta = int(input("Informe o número da conta para depósito: "))
    conta = encontrar_conta(numero_conta)
    if conta:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            conta['saldo'] += valor
            conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Conta não encontrada.")

def sacar():
    numero_conta = int(input("Informe o número da conta para saque: "))
    conta = encontrar_conta(numero_conta)
    if conta:
        valor = float(input("Informe o valor do saque: R$ "))
        excedeu_saldo = valor > conta['saldo']
        excedeu_limite = valor > 500  # Limite diário
        excedeu_saques = conta.get('numero_saques', 0) >= 3  # Limite de saques diários

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            conta['saldo'] -= valor
            conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
            conta['numero_saques'] = conta.get('numero_saques', 0) + 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Conta não encontrada.")

def exibir_extrato():
    numero_conta = int(input("Informe o número da conta para exibir o extrato: "))
    conta = encontrar_conta(numero_conta)
    if conta:
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
        print(f"\nSaldo: R$ {conta['saldo']:.2f}")
        print("===========================================")
    else:
        print("Conta não encontrada.")

def nova_conta(usuario):
    conta = len(contas) + 1  # Gerar número da conta automaticamente
    contas.append({"usuario": usuario, "conta": conta, "saldo": 0, "extrato": ""})
    print(f"Conta {conta} criada para o usuário {usuario} com sucesso!")

def listar_contas():
    if contas:
        print("\n=============== LISTA DE CONTAS ===============")
        for conta in contas:
            print(f"Usuário: {conta['usuario']}, Conta: {conta['conta']}")
        print("===============================================")
    else:
        print("Nenhuma conta encontrada.")

def novo_usuario():
    nome = input("Informe o nome do usuário: ")
    if nome in [usuario['nome'] for usuario in usuarios]:
        print("Usuário já existente!")
    else:
        usuarios.append({"nome": nome})
        print(f"Usuário {nome} criado com sucesso!")

def inicializar_contas():
    contas.append({"usuario": "user1", "conta": 1, "saldo": 1000, "extrato": ""})
    contas.append({"usuario": "user2", "conta": 2, "saldo": 2000, "extrato": ""})
    contas.append({"usuario": "user3", "conta": 3, "saldo": 3000, "extrato": ""})

def main():
    inicializar_contas()
    usuario = login()

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            exibir_extrato()
        elif opcao == "n":
            nova_conta(usuario)
        elif opcao == "l":
            listar_contas()
        elif opcao == "u":
            novo_usuario()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
