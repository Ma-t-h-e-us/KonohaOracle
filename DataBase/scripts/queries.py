from ..databaseConfig import cursor, conn

cursor.execute("SELECT DATABASE();")
db = cursor.fetchone()
print("Banco conectado:", db[0])