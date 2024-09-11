import mysql.connector

# Inicializa a conexão com o banco de dados
def criarConexao(endereco, usuario, senha, bancodedados):
    try:
        return mysql.connector.connect(
            host=endereco,
            user=usuario,
            password=senha,
            database=bancodedados
        )
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

# Encerra a conexão com o banco de dados
def encerrarConexao(connection):
    if connection:
        connection.close()

# Insere dados no banco de dados com prepared statements e tratamento de exceções
def insertNoBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        id = cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erro ao inserir no banco de dados: {err}")
        connection.rollback()  # Reverte a transação em caso de erro
        return None
    finally:
        cursor.close()
    return id

# Lista dados do banco de dados com tratamento de exceções
def listarBancoDados(connection, sql, params=None):
    try:
        cursor = connection.cursor(prepared=True)
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao listar do banco de dados: {err}")
        return []
    finally:
        cursor.close()
    return results

# Atualiza dados no banco de dados com tratamento de exceções
def atualizarBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar o banco de dados: {err}")
        connection.rollback()  # Reverte a transação em caso de erro
        return 0
    finally:
        cursor.close()
    return linhasAfetadas

# Exclui dados no banco de dados com tratamento de exceções
def excluirBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao excluir do banco de dados: {err}")
        connection.rollback()  # Reverte a transação em caso de erro
        return 0
    finally:
        cursor.close()
    return linhasAfetadas
