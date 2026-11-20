
import sqlite3


def conectar_banco():
    """Conecta ao banco de dados SQLite e retorna a conexão."""

    conexao = sqlite3.connect("banco.db")
    return conexao


def criar_tabela_despesas():
    """Cria a tabela de despesas no banco de dados, se não existir."""

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            categoria TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()


def cadastrar_despesa():
    """Cadastra uma nova despesa no banco de dados."""

    print("\n=== CADASTRAR DESPESA ===")

    descricao = input("Descrição: ")
    valor = float(input("Valor: ").replace(',', '.'))
    data = input("Data (DD-MM-AAAA): ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO despesas (descricao, valor, data, categoria)
        VALUES (?, ?, ?, ?)
    """, (descricao, valor, data, "Despesa"))

    conexao.commit()
    conexao.close()

    print("\nDespesa cadastrada com sucesso!")


def listar_despesas():
    """Mostra todas as despesas existentes no banco."""

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM despesas")

    despesas = cursor.fetchall()

    conexao.close()

    print("\n=== LISTAGEM DE DESPESAS ===")

    if not despesas:
        print("Nenhuma despesa está cadastrada!")
        return

    for despesa in despesas:
        print(f"""
        ID: {despesa[0]}
        Descrição: {despesa[1]}
        Valor: R$ {despesa[2]:.2f}
        Data: {despesa[3]}
        Categoria: {despesa[4]}
        _________________________________
        """)


def atualizar_despesa():
    """Atualiza uma despesa selecionada pelo usuário."""

    print("\n=== ATUALIZAÇÃO DE DESPESA ===")

    id_despesa = int(input("Digite o ID da despesa que deseja atualizar: "))

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM despesas WHERE id = ?",
        (id_despesa,)
    )

    despesa = cursor.fetchone()

    if despesa is None:
        print("Despesa não encontrada.")
        conexao.close()
        return

    descricao = input("Nova descrição: ")
    valor = float(input("Novo valor: ").replace(',', '.'))
    data = input("Nova data (DD-MM-AAAA): ")

    cursor.execute("""
        UPDATE despesas
        SET descricao = ?, valor = ?, data = ?
        WHERE id = ?
    """, (descricao, valor, data, id_despesa))

    conexao.commit()
    conexao.close()

    print("\nDespesa atualizada com sucesso!")


def excluir_despesa():
    """Exclui uma despesa existente no banco de dados."""

    print("\n=== EXCLUSÃO DE DESPESA ===")

    id_despesa = int(input("Digite o ID da despesa que deseja excluir: "))

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM despesas WHERE id = ?",
        (id_despesa,)
    )

    despesa = cursor.fetchone()

    if despesa is None:
        print("Despesa não encontrada.")
        conexao.close()
        return

    cursor.execute(
        "DELETE FROM despesas WHERE id = ?",
        (id_despesa,)
    )

    conexao.commit()
    conexao.close()

    print("\nDespesa excluída com sucesso!")
