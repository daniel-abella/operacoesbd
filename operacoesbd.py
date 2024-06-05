import mysql.connector

def criarConexao(endereco,usuario, senha, bancodedados):
      return mysql.connector.connect(
  host=endereco,user=usuario, password=senha,database=bancodedados)

def encerrarConexao(connection):
      connection.close()

def insertNoBancoDados(connection,sql,dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      id = cursor.lastrowid
      cursor.close()
      return id

def listarBancoDados(connection, sql, params=None):
    cursor = connection.cursor()
    if params is None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, params)
    results = cursor.fetchall()
    cursor.close()
    return results

def atualizarBancoDados(connection,sql, dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      linhasAfetadas = cursor.rowcount
      cursor.close()
      return linhasAfetadas

def excluirBancoDados(connection,sql,dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      linhasAfetadas = cursor.rowcount
      cursor.close()
      return linhasAfetadas
