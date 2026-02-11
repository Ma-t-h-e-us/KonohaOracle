#importacao de biblitecas

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

#criacao conexao direta com o bd mysql

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=str(os.getenv("host")),
        user=str(os.getenv("user")),
        port = int(os.getenv("port")),
        password=str(os.getenv("password")),
        database=str(os.getenv("database"))
    )

    if conn.is_connected():
        cursor = conn.cursor()

except Error as e:
    print("Erro ao conectar:", e)