# Conexão ao MySQL
import mysql.connector
from mysql.connector import Error

# Inserir dados em um banco de dados MySQL

print('--' * 40)
print('                       CADASTRO DE LIVROS ao BANCO de DADOS')
print('--' * 40)
print('Entre com os dados conforme solicitado.')
print('--' * 40)
while True:
    Id = input('ID: ')
    titulo = input('Nome: ')
    autor = input('Autor: ')
    assunto = input('Assunto: ')
    editora = input('Editora: ')
    modelo = input('Modelo: ')
    anoPubli = input('Ano Publicação: ')
    qtdePa = input('Quantidade de Páginas: ')
    idioma = input('Idioma: ')
    dados = ('\'' + Id + '\'' + ',\'' + titulo + '\',' + '\'' + autor + '\'' + ',\'' + assunto + '\',' + '\'' + editora +
             '\'' + ''+',\'' + modelo + '\',' + '\'' + anoPubli + '\'' + ',\'' + qtdePa + '\',' + '\'' +idioma + '\'' + ')')
    declaracao = '''insert into livros
    (id, título, autor, assuntos, editora, modelo, anoPublicação, qtdePaginas, idioma)
    values ('''
    sql = declaracao + dados

    try:
        con = mysql.connector.connect(
            host= 'localhost',
            database= 'meus_livros',
            user= 'root',
            password= 'Sanfran49ers')
        inserir_produtos = sql
        cursor = con.cursor()
        cursor.execute(inserir_produtos)
        con.commit()
        print(cursor.rowcount, 'registros inseridos na tabela!')
        cursor.close()
    except Error as erro:
        print(f'Falha ao inserir dados no MySQL: {erro}')
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão ao MySQL encerrada.')
    resp = str(input('Deseja cadastrar outro livro?(S/N) ')).strip().upper()[0]
    if resp == 'N':
        break
print('Até a proxima.')
