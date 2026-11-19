import sqlite3

def conectar_banco():
    """Conecta ao banco de dados SQLite e retorna a conexão."""
    conexao = sqlite3.connect("banco.db")
    return conexao

def criar_tabela_receitas():
    """Cria a tabela de receitas no banco de dados, se não existir."""
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            categoria TEXT NOT NULL)
    ''')
    conexao.commit()
    conexao.close()
    #Cria a tabela de receitas no banco de dados, caso ela não exista. A tabela possui os campos id, descricao, valor, data e categoria.

def cadastrar_receita():
    """Cadastra uma nova receita no banco de dados."""
    print("\n=== CADASTRAR RECEITA ===")

    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    data = input("Data (DD-MM-AAAA): ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO receitas (descricao, valor, data, categoria)
        VALUES (?, ?, ?, ?)
    """, (descricao, valor, data, "Receita")) #Insere os dados da nova receita na tabela

    conexao.commit()
    conexao.close()

    print("\nReceita cadastrada com sucesso!")


def listar_receitas():
    """Lista todas as receitas cadastradas no banco de dados."""

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM receitas")

    receitas = cursor.fetchall() #Armazena todas as receitas cadastradas no banco de dados em uma lista de tuplas

    conexao.close()

    print("\n=== LISTA DE RECEITAS ===")

    if not receitas:
        print("Nenhuma receita cadastrada.")
        return

    for receita in receitas: #Itera sobre a lista de receitas
        print(f"""
        ID: {receita[0]}
        Descrição: {receita[1]}
        Valor: R$ {receita[2]:.2f}
        Data: {receita[3]}
        Categoria: {receita[4]}
        --------------------------
        """)

def atualizar_receita():
    """Atualiza uma receita existente no banco de dados."""
    print("\n=== ATUALIZAR RECEITA ===")
    id_receita = int(input("Digite o ID da receita que deseja atualizar: ")) #Pega o ID da receita que o usuário deseja atualizar

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM receitas WHERE id = ?", (id_receita,)) #Pega a receita com o ID informado pelo usuário
    receita = cursor.fetchone() #Armazena a receita encontrada

    if receita is None:
        print("Receita não encontrada.")
        conexao.close()
        return

    descricao = input("Nova descrição: ")
    valor = float(input("Novo valor: "))
    data = input("Nova data (DD-MM-AAAA): ")

    cursor.execute("""UPDATE receitas
        SET descricao = ?, valor = ?, data = ?
        WHERE id = ?""", (descricao, valor, data, id_receita))
    conexao.commit()
    conexao.close()
    print("Receita atualizada com sucesso!")
    #Atualiza a receita de acordo com os dados informados pelo usuário

def excluir_receita():
    #Exclui uma receita existente no banco de dados.
    print("\n=== EXCLUIR RECEITA ===")
    id_receita = int(input("Digite o ID da receita que deseja excluir: ")) #Pega o ID da receita que o usuário deseja excluir

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM receitas WHERE id = ?", (id_receita,)) #Pega a receita com o ID informado pelo usuário

    receita = cursor.fetchone() #Armazena a receita encontrada

    if receita is None:
        print("Receita não encontrada.")
        conexao.close()
        return
    
    cursor.execute("DELETE FROM receitas WHERE id = ?", (id_receita,)) #
    conexao.commit()
    conexao.close()
    print("Receita excluída com sucesso!")