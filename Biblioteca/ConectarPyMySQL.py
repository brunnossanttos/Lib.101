import mysql.connector

#  Objeto de conexão
con = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='Sanfran49ers')
if con.is_connected():
    cadastro_info = con.get_server_info()
    print(f'Conectado ao servidor MySQL versão:  {cadastro_info}')
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print(f'Conectado ao Banco de Dados {linha}')

#  Fechando conexão
if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL encerrada...')
