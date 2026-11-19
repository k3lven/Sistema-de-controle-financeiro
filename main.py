# MENU PRINCIPAL
from funcoes.receitas import *

def menu_principal():

    while True:

        print("\n===== SISTEMA FINANCEIRO =====")
        print("1 - Receitas")
        print("2 - Despesas")
        print("3 - Transações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                menu_receitas()
            case '2':
                menu_despesas()
            case '3':
                menu_transacoes()
            case '0':
                print("Programa encerrado!")
                break
            case _:
                print("Opção inválida! Digite um número de 0 a 3.")
        input('Pressione "ENTER" para continuar.')

# MENU DE RECEITAS

def menu_receitas():

    while True:

        print("\n===== MENU DE RECEITAS =====")
        print("1 - Cadastrar receita")
        print("2 - Listar receitas")
        print("3 - Atualizar receita")
        print("4 - Excluir receita")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                criar_tabela_receitas()
                cadastrar_receita()
            case '2':
                listar_receitas()
            case '3':
                atualizar_receita()
            case '4':
                excluir_receita()
            case '0':
                break 
            case _:
                 print("Opção inválida! Digite um número de 0 a 4.")
        input('Pressione "ENTER" para continuar.')


# MENU DE DESPESAS

def menu_despesas():

    while True:

        print("\n===== MENU DE DESPESAS =====")
        print("1 - Cadastrar despesa")
        print("2 - Listar despesas")
        print("3 - Atualizar despesa")
        print("4 - Excluir despesa")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '0':
                break
            case _:
                 print("Opção inválida! Digite um número de 0 a 4.")
        input('Pressione "ENTER" para continuar.')
        


# MENU DE TRANSAÇÕES

def menu_transacoes():

    while True:

        print("\n===== MENU DE TRANSAÇÕES =====")
        print("1 - Listar transações")
        print("2 - Consultar transação")
        print("3 - Consultar saldo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '0':
                break
            case _:
                print("Opção inválida! Digite um número de 0 a 3.") # Ajustado para 0 a 3
                    
        input('Pressione "ENTER" para continuar.')

if __name__ == "__main__":
    menu_principal()