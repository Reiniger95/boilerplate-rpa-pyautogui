from datetime import date, datetime
import pymysql.cursors
from decouple import config

SERVIDOR = config('SERVIDOR')
USER = config('USER')
PASSWORD = config('PASSWORD')
DB = config('DB')

def InsertExemple(value):
    conexao = pymysql.connect(
    host=SERVIDOR,
    user=USER,
    password=PASSWORD,
    db=DB,
    cursorclass=pymysql.cursors.DictCursor,
)
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO TabelaNome (ColunaNome) VALUES (%s)'
        cursor.execute(sql, value)
    conexao.commit()


def SelectExemple(whereValue):
    conexao = pymysql.connect(
    host=SERVIDOR,
    user=USER,
    password=PASSWORD,
    db=DB,
    cursorclass=pymysql.cursors.DictCursor,
)
    data_atual = datetime.now()
    with conexao.cursor() as cursor:
        sql = 'SELECT TabelaNome from ColunaNome where nome = %s'
        valores = whereValue
        cursor.execute(sql, valores)
        data = cursor.fetchone()