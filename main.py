
# =================================
# MENU DE RECEITAS
# =================================

def menu_receitas():

    while True:

        print("\n===== MENU DE RECEITAS =====")
        print("1 - Cadastrar receita")
        print("2 - Listar receitas")
        print("3 - Atualizar receita")
        print("4 - Excluir receita")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break


# =================================
# MENU DE DESPESAS
# =================================

def menu_despesas():

    while True:

        print("\n===== MENU DE DESPESAS =====")
        print("1 - Cadastrar despesa")
        print("2 - Listar despesas")
        print("3 - Atualizar despesa")
        print("4 - Excluir despesa")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break


# =================================
# MENU DE TRANSAÇÕES
# =================================

def menu_transacoes():

    while True:

        print("\n===== MENU DE TRANSAÇÕES =====")
        print("1 - Listar transações")
        print("2 - Consultar transação")
        print("3 - Consultar saldo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break


# =================================
# MENU PRINCIPAL
# =================================

def menu_principal():

    while True:

        print("\n===== SISTEMA FINANCEIRO =====")
        print("1 - Receitas")
        print("2 - Despesas")
        print("3 - Transações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_receitas()

        elif opcao == "2":
            menu_despesas()

        elif opcao == "3":
            menu_transacoes()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


menu_principal()
