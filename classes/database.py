import sqlite3

#Conexão do banco de dados
def conectar():
    #Cria a conexão
    conecta = sqlite3.connect('database/banco.sqlite')
    return conecta