from logging import exception
from classes import database
from classes.funcionario import Funcionario

lista = []


def insert(funcionario):  # INSERE
    try:  # TENTA EXECUTAR
        con = database.conectar()  # conecta
        cursor = con.cursor()  # se move no banco
        sql = """INSERT INTO Funcionarios (nome, profissão, cpf, endereco)
                VALUES (?,?,?,?);"""
        cursor.execute(sql, funcionario.getFunc())
        con.commit()  # GRAVA OS DADOS NO BANCO

    except Exception as e:  # EM CASO DE ERRO
        print('Erro!')
        print(e)

    finally:  # OBRIGATORIAMENTE SERÁ EXECUTADO
        con.close()  # FECHA CONEXÃO


def update_lista(funcionario):  # ATUALIZA
    try:
        con = database.conectar()
        cursor = con.cursor()
        sql = """UPDATE Funcionarios SET nome=?, profissão=?, cpf=?, endereco=? WHERE id = ?;"""
        l = funcionario.getFunc()
        # INSERE O ID NO FINAL DA LISTA PARA FICAR IGUAL A SEQUENCIA DO SQL
        l.append(funcionario.id)
        cursor.execute(sql, l)
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()


def update_lixeira(id, deletado):
    try:
        con = database.conectar()
        cursor = con.cursor()
        sql = """UPDATE Funcionarios SET deletado=? WHERE id=?;"""
        cursor.execute(sql, [deletado, id])
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()


def selectLixeira():  # SELECIONA FUNCIONARIOS PARA LIXEIRA
    lista = []
    try:
        con = database.conectar()
        cursor = con.cursor()
        sql = """SELECT * FROM Funcionarios WHERE deletado = 1 ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall()  # RETORNA UMA LISTA COM OS DADOS DE CADA FUNCIONARIO
        for r in result:
            novo_funcionario = Funcionario(r[0], r[1], r[2], r[3], r[4], r[5])
            lista.append(novo_funcionario)

    except Exception as e:
        print(e)

    finally:

        con.close()
    return lista


def delete(id):  # DELETA
    try:
        con = database.conectar()
        cursor = con.cursor()
        sql = """DELETE FROM Funcionarios WHERE id = ?;"""
        cursor.execute(sql, [id])
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()


def selectAll(txt_pesquisa):  # PEGA TUDO
    lista = []
    try:
        con = database.conectar()
        cursor = con.cursor()
        sql = """SELECT * FROM Funcionarios f WHERE nome like ? or cpf like ? and deletado = 0 ORDER BY upper(nome);"""
        cursor.execute(sql, ['%'+txt_pesquisa+'%','%'+txt_pesquisa+'%'])
        result = cursor.fetchall()  # RETORNA UMA LISTA COM OS DADOS DE CADA FUNCIONARIO
        for r in result:
            novo_funcionario = Funcionario(r[0], r[1], r[2], r[3], r[4], r[5])
            lista.append(novo_funcionario)

    except Exception as e:
        print(e)

    finally:

        con.close()
    return lista
