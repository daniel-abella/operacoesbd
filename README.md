
# OperaçõesBD

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 📄 Descrição

**OperaçõesBD** é uma biblioteca utilitária em Python desenvolvida para simplificar operações básicas com um banco de dados MySQL. Ela fornece métodos fáceis de usar para **inserir**, **listar**, **atualizar** e **excluir** registros, garantindo interações seguras e confiáveis com o banco de dados. O projeto segue boas práticas, como o uso de **prepared statements** para prevenir injeções de SQL e **tratamento de exceções** para lidar com erros de forma eficiente.

## 🚀 Funcionalidades

- **Inserir Dados**: Insere novos registros no banco de dados MySQL.
- **Listar Dados**: Recupera todos os registros das tabelas do banco de dados.
- **Atualizar Dados**: Modifica registros existentes no banco de dados.
- **Excluir Dados**: Remove registros de forma segura.
- **Tratamento de Exceções**: Gerencia erros no banco de dados de forma eficaz.
- **Prepared Statements**: Garante a execução segura de consultas SQL, protegendo contra injeções de SQL.

## 📦 Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/operacoesbd.git
    ```
2. Instale as dependências necessárias:
    ```bash
    pip install mysql-connector-python
    ```

## 🛠 Uso

### 1. Criar uma Conexão com o Banco de Dados

Utilize a função `criarConexao()` para estabelecer uma conexão com o banco de dados MySQL.

```python
from operacoesbd import criarConexao, encerrarConexao

# Cria uma conexão com o banco de dados
conexao = criarConexao('localhost', 'root', 'senha', 'meubancodedados')
```

### 2. Inserir Dados

Use a função `insertNoBancoDados()` para inserir novos dados em uma tabela.

```python
sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
dados = ("João Silva", "joao@example.com")

id_usuario = insertNoBancoDados(conexao, sql, dados)
print(f"Usuário inserido com ID: {id_usuario}")
```

### 3. Listar Dados

Use a função `listarBancoDados()` para buscar todos os registros de uma tabela.

```python
sql = "SELECT * FROM usuarios"
usuarios = listarBancoDados(conexao, sql)

for usuario in usuarios:
    print(usuario)
```

### 4. Atualizar Dados

Utilize `atualizarBancoDados()` para modificar um registro existente.

```python
sql = "UPDATE usuarios SET nome = %s WHERE id = %s"
dados = ("Maria Silva", 1)

linhas_atualizadas = atualizarBancoDados(conexao, sql, dados)
print(f"Linhas atualizadas: {linhas_atualizadas}")
```

### 5. Excluir Dados

Use `excluirBancoDados()` para remover um registro da tabela.

```python
sql = "DELETE FROM usuarios WHERE id = %s"
dados = (1,)

linhas_excluidas = excluirBancoDados(conexao, sql, dados)
print(f"Linhas excluídas: {linhas_excluidas}")
```

### 6. Encerrar a Conexão

Ao finalizar as operações, sempre encerre a conexão com o banco de dados.

```python
encerrarConexao(conexao)
```

## 🛡️ Segurança

Esta biblioteca utiliza **prepared statements** para garantir a segurança das consultas e prevenir **SQL Injection**. Além disso, todas as operações são envoltas em tratamento de exceções para lidar com erros de forma adequada.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar **pull requests** e reportar **issues** no repositório.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
