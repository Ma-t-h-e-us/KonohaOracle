# importacao de bibliotecas
import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

# criacao conexao direta com o bd postgresql
load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        port=int(os.getenv("port")),
        password=os.getenv("password"),
        dbname=os.getenv("database") 
    )

    cursor = conn.cursor()
    print("Conectado ao PostgreSQL com sucesso!")

except OperationalError as e:
    print("Erro ao conectar:", e)