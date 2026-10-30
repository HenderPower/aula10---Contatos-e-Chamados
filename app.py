import sqlite3

def conectar_banco():

    conn = sqlite3.connect('contatos.db')

    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL
            )'''
    cursor.execute(sql)
    conn.commit()
    return conn



def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()
    print("Contato adicionado com sucesso!")

def listar_contatos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conn.close()
    print("-" * 60)

    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        for contato in contatos:
            print(f"ID: {contato[0]:<5} | Nome: {contato[1]:<20} | Telefone: {contato[2]:<15} | Email: {contato[3]:<20}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conn.close()
    print("-" * 60)

    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        for contato in contatos:
            print(f"ID: {contato[0]:<5} | Nome: {contato[1]:<20} | Telefone: {contato[2]:<15} | Email: {contato[3]:<20}")
                
def atualizar_contato():
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    nome = input("Digite o novo nome do contato: ")
    telefone = input("Digite o novo telefone do contato: ")
    email = input("Digite o novo email do contato: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?", (nome, telefone, email, id_contato))
    conn.commit()
    conn.close()
    print("Contato atualizado com sucesso!")

def excluir_contato():
    id_contato = input("Digite o ID do contato que deseja excluir: ")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    conn.commit()
    conn.close()
    print("Contato excluído com sucesso!")

def menu(): 
    while True:
        print("Tabela de Contatos")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Atualizar contato")
        print("5 - Excluir contato")
        print("6 - Sair")


        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            atualizar_contato()
        elif opcao == "5": 
            excluir_contato()
        elif opcao == "6":
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    menu()
