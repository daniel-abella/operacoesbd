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
